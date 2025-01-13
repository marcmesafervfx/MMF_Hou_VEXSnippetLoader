from PySide2 import QtGui
import re
from PySide2.QtGui import QSyntaxHighlighter


# Base class for VEX syntax highlighting
class VEXSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.formats = self.get_vex_formats()
        
        # Import syntax definitions
        from vex_syntax import VEX_KEYWORDS, VEX_FUNCTIONS
        
        # Create regex patterns for better performance
        keyword_pattern = r'\b(?:' + '|'.join(re.escape(k) for k in VEX_KEYWORDS) + r')\b'
        function_pattern = r'\b(?:' + '|'.join(re.escape(f) for f in VEX_FUNCTIONS) + r')\b(?=\s*\()'
        
        # Compile regex patterns for syntax elements
        self.patterns = {
            'keyword': re.compile(keyword_pattern),
            'function': re.compile(function_pattern),
            'double_slash_comment': re.compile(r'//.*$'),
            'hash_comment': re.compile(r'^[ ]*#[^\n]*'),
            'multi_comment_start': re.compile(r'/\*'),
            'multi_comment_end': re.compile(r'\*/'),
            'triple_quotes': re.compile(r'""".*?"""|\'\'\'.*?\'\'\'', re.DOTALL),
            'string_start': re.compile(r'["\']'),
            'attribute': re.compile(r'(?<!\w)(?:[fiuvdps234]\s*(?:\[\])?)?@[\w]+')
        }

    # Define color formats for different syntax elements
    def get_vex_formats(self):
        formats = {}
        
        # Pink for keywords
        formats['keyword'] = QtGui.QTextCharFormat()
        formats['keyword'].setForeground(QtGui.QColor("#fc33ff"))
        
        # Blue for functions
        formats['function'] = QtGui.QTextCharFormat()
        formats['function'].setForeground(QtGui.QColor("#44e5f5"))
        
        # Green for strings
        formats['string'] = QtGui.QTextCharFormat()
        formats['string'].setForeground(QtGui.QColor("#2ecc71"))
        
        # Orange for attributes
        formats['attribute'] = QtGui.QTextCharFormat()
        formats['attribute'].setForeground(QtGui.QColor("#ffa500"))
        
        # Yellow for comments
        formats['comment'] = QtGui.QTextCharFormat()
        formats['comment'].setForeground(QtGui.QColor("#f3ec52"))
        
        return formats

    # Main highlighting logic for text blocks
    def highlightBlock(self, text):
        self.setFormat(0, len(text), QtGui.QTextCharFormat())
        skip_ranges = []
        start_index = 0
        
        # Get state from previous block
        previous_state = self.previousBlockState()
        in_multiline_comment = previous_state == 1
        in_string = previous_state in [2, 3]
        string_char = '"' if previous_state == 2 else "'" if previous_state == 3 else None
        
        # Handle triple-quoted strings first
        for match in self.patterns['triple_quotes'].finditer(text):
            if not any(start <= match.start() < end for start, end in skip_ranges):
                self.setFormat(match.start(), match.end() - match.start(), self.formats['string'])
                skip_ranges.append((match.start(), match.end()))
                if match.group().endswith('"""') or match.group().endswith("'''"):
                    start_index = match.end()
                else:
                    self.setCurrentBlockState(2 if '"""' in match.group() else 3)
                    return

        # Check if position is within a valid string
        def is_in_valid_string(pos):
            if any(start <= pos < end for start, end in skip_ranges):
                return True
            
            single_quotes = text[:pos].count("'")
            double_quotes = text[:pos].count('"')
            first_quote = min(text.find("'"), text.find('"')) if "'" in text[:pos] or '"' in text[:pos] else -1
            first_comment = text.find("//")

            if first_quote == -1:
                return False
            if first_comment != -1 and first_comment < first_quote:
                return False
            return (single_quotes % 2 == 1) or (double_quotes % 2 == 1)

        # Process single-line comments
        for match in self.patterns['double_slash_comment'].finditer(text):
            comment_start = match.start()
            if previous_state in [2, 3]:
                continue
            if not is_in_valid_string(comment_start):
                comment_end = match.end()
                self.setFormat(comment_start, comment_end - comment_start, self.formats['comment'])
                skip_ranges.append((comment_start, comment_end))

        # Handle continuing strings from previous block
        if in_string and string_char:
            end_quote = text.find(string_char)
            if end_quote != -1:
                if not any(start <= 0 < end for start, end in skip_ranges):
                    self.setFormat(0, end_quote + 1, self.formats['string'])
                    skip_ranges.append((0, end_quote + 1))
                start_index = end_quote + 1
                self.setCurrentBlockState(0)
            else:
                if not any(start <= 0 < end for start, end in skip_ranges):
                    self.setFormat(0, len(text), self.formats['string'])
                    skip_ranges.append((0, len(text)))
                self.setCurrentBlockState(2 if string_char == '"' else 3)
                return

        # Process regular strings
        i = start_index
        while i < len(text):
            if any(start <= i < end for start, end in skip_ranges):
                i += 1
                continue
            
            try:
                match = self.patterns['string_start'].search(text, i)
                if not match:
                    break
                    
                quote_char = match.group(0)
                start_pos = match.start()
                
                if any(start <= start_pos < end for start, end in skip_ranges):
                    i = start_pos + 1
                    continue
                    
                i = start_pos + 1
                found_end = False
                while i < len(text):
                    if text[i] == quote_char and text[i-1] != '\\':
                        self.setFormat(start_pos, i - start_pos + 1, self.formats['string'])
                        skip_ranges.append((start_pos, i + 1))
                        i += 1
                        found_end = True
                        break
                    i += 1
                    
                if not found_end:
                    self.setFormat(start_pos, len(text) - start_pos, self.formats['string'])
                    skip_ranges.append((start_pos, len(text)))
                    self.setCurrentBlockState(2 if quote_char == '"' else 3)
                    return
                    
            except Exception as e:
                print(f"Error in string highlighting: {e}")
                i += 1
                continue

        # Process hash comments
        hash_format = QtGui.QTextCharFormat()
        hash_format.setForeground(QtGui.QColor(255, 140, 0))
        for match in self.patterns['hash_comment'].finditer(text):
            if not any(start <= match.start() < end for start, end in skip_ranges):
                self.setFormat(match.start(), match.end() - match.start(), hash_format)
                skip_ranges.append((match.start(), match.end()))

        # Apply formatting for attributes, keywords, and functions
        for pattern_type in ['attribute', 'keyword', 'function']:
            for match in self.patterns[pattern_type].finditer(text):
                if not any(start <= match.start() < end for start, end in skip_ranges):
                    self.setFormat(match.start(), match.end() - match.start(), self.formats[pattern_type])

        # Handle multiline comments
        if in_multiline_comment:
            end_match = self.patterns['multi_comment_end'].search(text)
            if end_match:
                self.setFormat(0, end_match.end(), self.formats['comment'])
                start_index = end_match.end()
                self.setCurrentBlockState(0)
            else:
                self.setFormat(0, len(text), self.formats['comment'])
                self.setCurrentBlockState(1)
                return

        # Process new multiline comments in current block
        start_index = 0
        while True:
            start_match = self.patterns['multi_comment_start'].search(text, start_index)
            if not start_match or any(start <= start_match.start() < end for start, end in skip_ranges):
                break
            
            end_match = self.patterns['multi_comment_end'].search(text, start_match.end())
            if end_match:
                length = end_match.end() - start_match.start()
                self.setFormat(start_match.start(), length, self.formats['comment'])
                start_index = end_match.end()
                skip_ranges.append((start_match.start(), end_match.end()))
            else:
                length = len(text) - start_match.start()
                self.setFormat(start_match.start(), length, self.formats['comment'])
                skip_ranges.append((start_match.start(), len(text)))
                self.setCurrentBlockState(1)
                return

        # Reset block state if no multiline elements exist
        if not any((
            text.find('/*') != -1,
            text.find('"""') != -1,
            text.find("'''") != -1,
            self.previousBlockState() in [1, 2, 3]
        )):
            self.setCurrentBlockState(0)

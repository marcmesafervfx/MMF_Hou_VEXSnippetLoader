import os
import json
import requests
import re

# Get snippets for a specific category from the JSON file
def get_snippets_for_library(workgroup):
    try:
        # Always fetch fresh data
        sections = fetch_github_readme()
        
        if sections and workgroup in sections:
            return sections[workgroup]
        return {}
            
    except Exception:
        return {}

# Fetch and parse GitHub README content
def fetch_github_readme():
    raw_url = "https://raw.githubusercontent.com/marcmesafervfx/MMF_Hou_VEXSnippets/main/README.md"
    
    try:
        response = requests.get(raw_url)
        response.raise_for_status()
        readme_content = response.text
        
        # Initialize sections dictionary
        sections = {
            "Points": {},
            "Detail": {},
            "Primitives": {},
            "VEX Shader": {},
            "Volume": {}
        }
        
        lines = readme_content.splitlines()
        current_ref_code = None
        current_section = None
        current_title = None
        current_mode = None
        code_block = []
        in_code_block = False
        
        processed_entries = 0
        
        for line in lines:
            # Don't strip whitespace from code lines
            if not in_code_block:
                line = line.strip()
            
            # Section detection
            if line.startswith('## '):
                current_section = line[3:].strip()
                continue
            
            # Reference code detection
            if '*Reference Code*' in line:
                ref_match = re.search(r'\*Reference Code\*:\s*(\d+)', line)
                if ref_match:
                    current_ref_code = ref_match.group(1)
                continue
            
            # Title detection
            if '**' in line and not 'Input' in line and not 'Output' in line and not 'Mode:' in line and not '*Reference Code*' in line and not '[!' in line:
                title_match = re.search(r'\*\*([^*]+)\*\*', line)
                if title_match:
                    current_title = title_match.group(1).strip()
                continue
            
            # Mode detection
            if '**Mode:**' in line:
                mode_match = re.search(r'\*\*Mode:\*\*\s*(.*?)\.?$', line)
                if mode_match:
                    current_mode = mode_match.group(1).strip()
                    if current_mode.endswith('.'):
                        current_mode = current_mode[:-1]
                continue
            
            # Code block detection
            if line.startswith('```'):
                if not in_code_block:
                    in_code_block = True
                    code_block = []
                else:
                    in_code_block = False
                    if current_title and current_mode and current_ref_code:
                        code_text = '\n'.join(code_block)
                        if current_mode in sections and code_text.strip():
                            sections[current_mode][current_title] = {
                                "reference_code": current_ref_code,
                                "section": current_section,
                                "code": code_text
                            }
                            processed_entries += 1
                continue
            
            if in_code_block:
                code_block.append(line)
        
        # Save parsed data to JSON file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, 'readme_sections.json')
        
        try:
            json_str = json.dumps(sections, indent=4, ensure_ascii=False)
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json_file.write(json_str)
            return sections
        except Exception as e:
            return None
            
    except requests.exceptions.RequestException as e:
        return None

# Import required modules
from PySide2 import QtWidgets, QtCore, QtUiTools, QtGui
import os
import json
import hou
from vex_formatting import VEXSyntaxHighlighter
import socket
import webbrowser
from request_git import get_snippets_for_library


# Define snippet categories
SNIPPET_TYPE = ['Point', 'Primitives', 'Detail', 'Vertex', 'Numbers', 'Volumes', 'DOPS']

# Define publish methods
PUBLISH = ['Personal', 'Snippet Library']

# Define node types
NODE_TYPES = ["gaswrangle", "attribwrangle", "popwrangle", "geometrywrangle"]

# UI class for saving snippets
class saveSnippet(QtWidgets.QWidget):
    def __init__(self, parm=None, type=None, content=None, parent=None):
        if parent is None:
            try:
                import hou
                parent = hou.ui.mainQtWindow()
            except:
                pass
       
        super(saveSnippet, self).__init__(parent=parent)

        # Initialize window properties
        self.setWindowTitle("Snippet Publisher v0.0.6")
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.Window)
        self.resize(500, 200)

        self.parm = parm
        self.type = type
        self.content = content

        self.init_ui()

    # Initialize UI components and signals
    def init_ui(self):
        ui_file = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ui/save.ui'))
        f = QtCore.QFile(ui_file)
        f.open(QtCore.QFile.ReadOnly)

        loader = QtUiTools.QUiLoader()
        self.uiSave = loader.load(f)
        f.close()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.uiSave)

        self.uiSave.type_combo.addItems(SNIPPET_TYPE)
        
        self.uiSave.save.clicked.connect(self.save_snippet)
        self.uiSave.snippet_name.editingFinished.connect(self.changePolicy)

    # Handle escape key press
    def keyPressEvent(self, event):   
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
            self.deleteLater()
    
    # Clear focus from input fields
    def changePolicy(self):
        self.uiSave.snippet_name.clearFocus()
        self.uiSave.snippet_description.clearFocus() 
                
    # Get save path and create vex_snippet.json if needed
    def get_savepath(self):
        data = {}
        code_name = self.uiSave.type_combo.currentText()
        self.vex_path = hou.text.expandString("$HOUDINI_USER_PREF_DIR") + "/VEXSnippets/"
        
        file_path = os.path.abspath(os.path.join(self.vex_path,
                                    code_name,
                                    'vex_snippet.json'))
        
        if not os.path.isdir(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
            json_object = json.dumps(data, indent=4)

            with open(file_path, "w") as outfile:
                outfile.write(json_object)
                outfile.close()
        
        return file_path

    # Save snippet code to file
    def save_snippet(self):
        snippet_title = self.uiSave.snippet_name.text()
        if snippet_title == "":
            snippet_title = "snippet_code"

        if self.type == "New Code":
            vex_code = self.content
        else:
            vex_code = self.parm.evalAsString()

        snippet_file = self.get_savepath()

        if self.uiSave.snippet_description.toPlainText() == "":
            description_code = ""
        else:
            plain = self.uiSave.snippet_description.toPlainText().replace('"', '')
            description_code = '"""' + plain + '""";' + "\n\n"

        vex = description_code + vex_code
        
        with open(snippet_file, 'r') as f:
            data = json.load(f)
            data[snippet_title] = vex

        with open(snippet_file, "w") as outfile:
            json.dump(data, outfile, indent=4)
        
        self.close()
        self.deleteLater()

# UI class for loading snippets
class loadSnippet(QtWidgets.QWidget):
    def __init__(self, parm=None, parent=None):
        if parent is None:
            parent = hou.qt.mainWindow()
        
        super(loadSnippet, self).__init__(parent)
        
        self.ui = None
        
        # Initialize text formats for syntax highlighting
        formats = VEXSyntaxHighlighter().get_vex_formats()
        self.keyword_format = formats['keyword']
        self.function_format = formats['function']
        self.string_format = formats['string']
        self.attribute_format = formats['attribute']
        self.comment_format = formats['comment']

        # Set window properties
        self.setWindowTitle("Snippet Loader v0.0.6")
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.Window)
        self.resize(1000, 500)

        self.vex_path = os.path.dirname(os.path.abspath(__file__))
        self.parm = parm
        self.current_code = ''
        self.prev_sel_list = ''
        
        self.create_ui()
        self.get_types()
        self.installEventFilter(self)
        
        QtCore.QTimer.singleShot(0, self.check_connection_status)

    # Check internet connection and display warning if needed
    def check_connection_status(self):
        if not self.check_internet_connection():
            hou.ui.displayMessage(
                "No internet connection available. Some Snippet Library features may be limited.",
                severity=hou.severityType.Warning
            )

    # Create and setup the UI components
    def create_ui(self):
        ui_file = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ui/load.ui'))
        f = QtCore.QFile(ui_file)
        f.open(QtCore.QFile.ReadOnly)
 
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(f)
        f.close()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.ui)
        
        # Configure text editor appearance
        self.ui.code.setStyleSheet("""
            QTextEdit {
                background-color: rgb(15, 15, 15);
                color: rgb(255, 255, 255);
                font-family: "Source Code Pro", "DejaVu Sans Mono", "Consolas", monospace;
                font-size: 9pt;
                font-weight: bold;
                line-height: 1.2;
            }
        """)
        
        # Configure horizontal scrolling
        self.ui.code.setWordWrapMode(QtGui.QTextOption.NoWrap)
        self.ui.code.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.ui.code.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(1)
        self.ui.code.setSizePolicy(size_policy)
        
        self.setup_connections()
        self.syntax_highlighter = VEXSyntaxHighlighter(self.ui.code.document())
        self.ui.loadfrom.addItems(PUBLISH)

    # Setup all signal connections
    def setup_connections(self):
        # Connect UI signals to their handlers
        self.ui.loadfrom.currentTextChanged.connect(self.contextFiles)
        self.ui.loadfrom.currentTextChanged.connect(self.get_types)
        self.ui.loadfrom.currentTextChanged.connect(self.update_workgroup_buttons_state)
        self.ui.loadfrom.currentTextChanged.connect(self.get_snippet_names)
        self.ui.node_list.currentTextChanged.connect(self.get_snippet_names)
        self.ui.refresh.clicked.connect(self.get_types)
        self.ui.refresh.clicked.connect(self.get_snippet_names)
        self.ui.refresh.clicked.connect(self.toggle_wifi)

        self.ui.search_value.textEdited.connect(self.get_snippet_names)
        self.ui.search_value.editingFinished.connect(self.changePolicy)
        self.ui.snippet_list.itemClicked.connect(self.get_snippet_code)
        self.ui.append_btn.clicked.connect(self.append_code)
        self.ui.replace_btn.clicked.connect(self.replace_code)
        self.ui.delete_btn.clicked.connect(self.delete_code)
        self.ui.edit_title.clicked.connect(self.editTitle)
        self.ui.commit_changes.clicked.connect(self.editCode)
        self.ui.github_btn.clicked.connect(self.open_github)
        self.ui.wifi_btn.clicked.connect(self.handle_wifi_toggle)
        self.ui.new_code_btn.clicked.connect(self.open_save_snippet)
        self.ui.github_btn.pressed.connect(self.github_btn_pressed)
        self.ui.github_btn.released.connect(self.github_btn_released)
        
        # Set initial button states
        self.ui.append_btn.setEnabled(False)
        self.ui.replace_btn.setEnabled(False)

        # Setup GitHub button
        self.setup_github_button()
        
        # Setup WiFi button
        self.setup_wifi_button()
        
        # Set initial WiFi icon
        self.toggle_wifi(show_message=False)

    # Setup GitHub button appearance and behavior
    def setup_github_button(self):
        github_default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'github-logo-default.png')
        github_sel_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'github-logo-sel.png')
        
        if os.path.exists(github_default_path) and os.path.exists(github_sel_path):
            self.github_default_icon = QtGui.QIcon(github_default_path)
            self.github_sel_icon = QtGui.QIcon(github_sel_path)
            
            self.ui.github_btn.setIcon(self.github_default_icon)
            self.ui.github_btn.setIconSize(QtCore.QSize(20, 20))
            self.ui.github_btn.setMinimumSize(QtCore.QSize(25, 25))
            self.ui.github_btn.setMaximumSize(QtCore.QSize(25, 25))
            self.ui.github_btn.setText("")
            
            self.ui.github_btn.setFlat(True)
            self.ui.github_btn.setStyleSheet("border: none; background: none;")


    # Setup WiFi button appearance
    def setup_wifi_button(self):
        wifi_off_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'wifi-off.png')
        wifi_on_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'wifi-on.png')
        
        if os.path.exists(wifi_off_path) and os.path.exists(wifi_on_path):
            self.wifi_off_icon = QtGui.QIcon(wifi_off_path)
            self.wifi_on_icon = QtGui.QIcon(wifi_on_path)
            
            self.ui.wifi_btn.setIcon(self.wifi_off_icon)
            self.ui.wifi_btn.setIconSize(QtCore.QSize(20, 20))
            self.ui.wifi_btn.setMinimumSize(QtCore.QSize(25, 25))
            self.ui.wifi_btn.setMaximumSize(QtCore.QSize(25, 25))
            self.ui.wifi_btn.setText("")
            
            self.ui.wifi_btn.setFlat(True)
            self.ui.wifi_btn.setStyleSheet("border: none; background: none;")

    # Toggle WiFi icon and show connection status
    def toggle_wifi(self, show_message=False):
        connection = self.check_internet_connection()
        self.ui.wifi_btn.setIcon(self.wifi_on_icon if connection else self.wifi_off_icon)
        
        if show_message:
            message = "Internet connection is available." if connection else "No internet connection available."
            hou.ui.displayMessage(message)

    # Handle WiFi button click
    def handle_wifi_toggle(self):
        self.toggle_wifi(show_message=True)

    # Handle escape key press
    def keyPressEvent(self, event):   
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
            self.deleteLater()
        
    # Clear focus from input fields
    def changePolicy(self):
        self.ui.search_value.clearFocus()
        self.ui.code.clearFocus()   

    # Test internet connection
    def check_internet_connection(self):
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False

    # Get types of snippets
    def get_types(self):
        current_selection = self.ui.node_list.currentText()
        
        self.ui.node_list.clear()
        
        if self.ui.loadfrom.currentText() == "Snippet Library":
            try:
                if not self.check_internet_connection():
                    hou.ui.displayMessage(
                        "No internet connection available. Some Snippet Library features may be limited.",
                        severity=hou.severityType.Warning
                    )

                else:
                    readme_path = os.path.join(self.vex_path, 'readme_sections.json')
                    if not os.path.exists(readme_path):
                        try:
                            with open(readme_path, 'w') as f:
                                json.dump({}, f, indent=4)
                            
                            from request_git import fetch_github_readme as fetch_readme
                            fetch_readme()
                        except Exception as e:
                            print(f"Error creating initial readme file: {e}")
                    else:
                        try:
                            from request_git import fetch_github_readme as fetch_readme
                            fetch_readme()
                        except ImportError as e:
                            print(f"Error importing git module: {e}")
                        except Exception as e:
                            print(f"Error updating from git: {e}")
                
                readme_path = os.path.join(self.vex_path, 'readme_sections.json')
                with open(readme_path, 'r') as f:
                    data = json.load(f)
                
                categories = list(data.keys())
                categories.sort()
                
                self.ui.node_list.addItems(categories)

                index = self.ui.node_list.findText(current_selection, QtCore.Qt.MatchFixedString)

                if index >=0:
                    self.ui.node_list.setCurrentIndex(index)
                
            except Exception as e:
                print(f"Error loading categories: {e}")
        else:
            try:
                self.nodes = os.listdir(self.vex_path)
                self.ui.node_list.addItems(self.nodes)
                index = self.ui.node_list.findText(current_selection, QtCore.Qt.MatchFixedString)

                if index >=0:
                    self.ui.node_list.setCurrentIndex(index)
            except:
                pass

    # Add elements to the snippet list name with ID numbers
    def get_snippet_names(self):
       
        try:
            current_selection = self.ui.snippet_list.selectedItems()
            self.prev_sel_list = current_selection[0].text()
        except:
            pass
            
        try:
            
            self.ui.snippet_list.clear()
            self.ui.code.clear()

            self.ui.append_btn.setEnabled(False)
            self.ui.replace_btn.setEnabled(False)
            self.ui.commit_changes.setEnabled(False)

            search_text = self.ui.search_value.text().lower()
            search_terms = search_text.split()

            if self.ui.loadfrom.currentText() == "Snippet Library":
                selected_category = self.ui.node_list.currentText()
                self.snippets_cache = {}
                if not selected_category:
                    return
                
                if not hasattr(self, 'snippets_cache'):
                    self.snippets_cache[selected_category] = get_snippets_for_library(selected_category)
                    
                if selected_category not in self.snippets_cache:
                    self.snippets_cache[selected_category] = get_snippets_for_library(selected_category)
                
                snippets = self.snippets_cache[selected_category]

                formatted_titles = []
                for title, snippet_data in snippets.items():
                    ref_code = snippet_data.get("reference_code", "")
                    formatted_title = f"{title} ({ref_code})"

                    if all(term in formatted_title.lower() for term in search_terms):
                        formatted_titles.append(formatted_title)

                formatted_titles.sort()

                self.ui.snippet_list.addItems(formatted_titles)
                items = self.ui.snippet_list.findItems(self.prev_sel_list, QtCore.Qt.MatchExactly)
                
                if len(items) > 0:
                    items[0].setSelected(True)
                    self.get_snippet_code()

            else:
                snippet_data = self.get_snippet_data()
                keys = snippet_data.keys()

                if search_terms:
                    filtered_keys = [key for key in keys if all(term in key.lower() for term in search_terms)]
                else:
                    filtered_keys = list(keys)

                filtered_keys.sort()
                self.ui.snippet_list.addItems(filtered_keys)
                items = self.ui.snippet_list.findItems(self.prev_sel_list, QtCore.Qt.MatchExactly)
                
                if len(items) > 0:
                    items[0].setSelected(True)
                    self.get_snippet_code()

        except Exception as e:
            print(f"Error in get_snippet_names: {e}")

    # Set vex_path based on user publish selection
    def contextFiles(self):
        if self.ui.loadfrom.currentText() == "Personal":
            self.vex_path = hou.text.expandString("$HOUDINI_USER_PREF_DIR") + "/VEXSnippets/"
        else:
            self.vex_path = os.path.dirname(os.path.abspath(__file__))
        

    # View snippet code in the text code widget
    def get_snippet_code(self):
        self.ui.code.clear()

        try:
            if self.ui.loadfrom.currentText() == "Snippet Library":
                selected_category = self.ui.node_list.currentText()
                formatted_name = self.ui.snippet_list.selectedItems()[0].text()
                snippet_name = formatted_name.split(" (")[0]
                snippets = get_snippets_for_library(selected_category)
                
                if snippet_name in snippets:
                    self.current_code = snippets[snippet_name]["code"]
                    self.ui.code.setPlainText(self.current_code)
                    
                    self.ui.append_btn.setEnabled(True)
                    self.ui.replace_btn.setEnabled(True)
                    self.ui.commit_changes.setEnabled(False)
                    self.ui.delete_btn.setEnabled(False)
                    self.ui.new_code_btn.setEnabled(False)
            else:
                snippet_data = self.get_snippet_data()
                current_selection = self.ui.snippet_list.selectedItems()[0].text()
                self.current_code = snippet_data[current_selection]
                self.ui.code.setPlainText(self.current_code)
                
                self.ui.append_btn.setEnabled(True)
                self.ui.replace_btn.setEnabled(True)
                self.ui.commit_changes.setEnabled(True)
                self.ui.delete_btn.setEnabled(True)
                self.ui.new_code_btn.setEnabled(True)
                
        except Exception as e:
            print(f"Error displaying code: {e}")

    # Get the snippet content based on user selection
    def get_snippet_data(self):
        data = {}
        
        if self.ui.loadfrom.currentText() == "Snippet Library":
            try:
                readme_path = os.path.join(self.vex_path, 'readme_sections.json')
                with open(readme_path, 'r') as f:
                    data = json.load(f)
                
                selected_node = self.ui.node_list.currentText()
                return data.get(selected_node, {})
            except:
                return {}
        else:
            try:
                selected_node = self.ui.node_list.currentText()
            except:
                selected_node = ""

            data_file = os.path.abspath(os.path.join(self.vex_path, selected_node, 'vex_snippet.json'))
            
            try:
                with open(data_file, 'r') as f:
                    data = json.load(f)
                return data
            except:
                return {}

    # Append code to existing snippet
    def append_code(self):
        try:
            selected_nodes = hou.selectedNodes()

            for node in selected_nodes:
                
                self.parm = node.parm("snippet")
                existing_code = self.parm.evalAsString()
                if existing_code == "":
                        new_code = self.current_code
                        self.parm.set(new_code)
                else:
                    new_code = "\n".join([existing_code, self.current_code])
                    self.parm.set(new_code)
        except:
            selected_nodes = hou.selectedNodes()

            WRANGLER_NODES = []
            for sel_node in selected_nodes:
                if sel_node.type().name() in NODE_TYPES:
                    WRANGLER_NODES.append(sel_node)
            try:
                for node in WRANGLER_NODES:
                    self.parm = node.parm('snippet')
                    existing_code = self.parm.evalAsString()

                    if existing_code == "":
                        new_code = self.current_code
                        self.parm.set(new_code)
                    else:
                        new_code = "\n".join([existing_code, self.current_code])
                        self.parm.set(new_code)
            except:
                hou.ui.displayMessage("Select a Wrangler Node to proceed.", severity=hou.severityType.Warning)
        
    # Replace existing code with new snippet
    def replace_code(self):
        try:
            selected_nodes = hou.selectedNodes()
            
            for node in selected_nodes:
                
                self.parm = node.parm("snippet")
                new_code = self.current_code
                self.parm.set(new_code)
        except:
            selected_nodes = hou.selectedNodes()

            WRANGLER_NODES = []
            for sel_node in selected_nodes:
                if sel_node.type().name() in NODE_TYPES:
                    WRANGLER_NODES.append(sel_node)
            try:
                 for node in WRANGLER_NODES:
                    self.parm = node.parm('snippet')
                    new_code = self.current_code
                    self.parm.set(new_code)
            except:
                hou.ui.displayMessage("Select a Wrangler Node to proceed.", severity=hou.severityType.Warning, suppress=hou.confirmType.OverwriteFile)
                
    # Edit snippet title
    def editTitle(self):        
        try:
            current_snippet_selection = self.ui.snippet_list.currentItem().text()
            selected_node = self.ui.node_list.currentText()
            
            new_title = hou.ui.readInput("Add a new name for the selected code:")
            if new_title[1] == "":
                raise 
            new_title = new_title[1]

            snippet_data = self.get_snippet_data()
            snippet_data[new_title] = snippet_data[current_snippet_selection]
            del snippet_data[current_snippet_selection]
            
            if self.ui.loadfrom.currentText() == "Personal":
                snippet_files = [os.path.abspath(os.path.join(self.vex_path, selected_node, 'vex_snippet.json'))]
            else:
                work_c = self.vex_path + "/" + selected_node + "/vex_snippet.json"
                snippet_files = [os.path.abspath(os.path.join(self.vex_path, selected_node, 'vex_snippet.json')), work_c]

            for snippet_file in snippet_files:
                with open(snippet_file, "w") as outfile:
                    json.dump(snippet_data, outfile, indent=4)
                
        except:
            pass

    # Edit snippet code
    def editCode(self):        
        try:
            current_snippet_selection = self.ui.snippet_list.currentItem().text()
            selected_node = self.ui.node_list.currentText()
            
            confirm = hou.ui.displayConfirmation("Are you sure that you want to commit changes in the code?")
            if confirm != 1:
                raise 
            
            new_vex = self.ui.code.toPlainText()

            snippet_data = self.get_snippet_data()
            snippet_data[current_snippet_selection] = new_vex
            
            if self.ui.loadfrom.currentText() == "Personal":
                snippet_files = [os.path.abspath(os.path.join(self.vex_path, selected_node, 'vex_snippet.json'))]
            else:
                work_c = self.vex_path + "/" + selected_node + "/vex_snippet.json"
                snippet_files = [os.path.abspath(os.path.join(self.vex_path, selected_node, 'vex_snippet.json')), work_c]

            for snippet_file in snippet_files:
                with open(snippet_file, "w") as outfile:
                    json.dump(snippet_data, outfile, indent=4)
                
        except:
            pass       

    # Delete snippet code
    def delete_code(self):
        try:
            current_snippet_selection = self.ui.snippet_list.currentItem().text()
            selected_node = self.ui.node_list.currentText()
            
            snippet_data = self.get_snippet_data()
            snippet_data.pop(current_snippet_selection)
            
            if self.ui.loadfrom.currentText() == "Personal":
                snippet_files = [os.path.abspath(os.path.join(self.vex_path, selected_node, 'vex_snippet.json'))]
            else:
                work_c = self.vex_path + "/" + selected_node + "/vex_snippet.json"
                snippet_files = [os.path.abspath(os.path.join(self.vex_path, selected_node, 'vex_snippet.json')), work_c]

            mssg = "Are you sure that you want to remove the displayed code from the library?"
            answer = hou.ui.displayConfirmation(mssg, severity=hou.severityType.Error, suppress=hou.confirmType.OverwriteFile)

            for snippet_file in snippet_files:
                if answer:
                    with open(snippet_file, "w") as outfile:
                        json.dump(snippet_data, outfile, indent=4)
                else:
                    pass
        except:
            pass   

    # Update button states based on mode
    def update_workgroup_buttons_state(self):
        is_personal = self.ui.loadfrom.currentText() != "Snippet Library"
        self.ui.commit_changes.setEnabled(is_personal)
        self.ui.delete_btn.setEnabled(is_personal)
        self.ui.edit_title.setEnabled(is_personal)
        self.ui.new_code_btn.setEnabled(is_personal)

    # Open GitHub README page
    def open_github(self):
        github_url = "https://github.com/marcmesafervfx/MMF_Hou_VEXSnippets/blob/main/README.md"
        webbrowser.open(github_url)

    # Handle GitHub button press
    def github_btn_pressed(self):
        self.ui.github_btn.setIcon(self.github_sel_icon)
    
    # Handle GitHub button release
    def github_btn_released(self):
        self.ui.github_btn.setIcon(self.github_default_icon)

    # Open save snippet UI
    def open_save_snippet(self):
        try:
            self.save_snippet_ui = saveSnippet(type='New Code', content=self.ui.code.toPlainText(), parent=self)
            self.save_snippet_ui.show()
        except Exception as e:
            hou.ui.displayMessage(f"Failed to open Save Snippet UI: {e}", severity=hou.severityType.Error)

import PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QPlainTextEdit
from PyQt6.QtGui import QIcon, QFontDatabase


class MainApp:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle("PikI")
        self.window.setGeometry(100, 100, 500, 720)
        self.window.setStyleSheet("background-color: #FFFFFF;")
        self.color_themes("green", "window")
           
    
    def color_themes(self, theme, layout):
        lite = {}
        dark = {}
        green = {"window": "background-color: #F3F3F4;",
                 "top_label": """background-color: #FFFFFF;
                                 border-radius: 10px;
                                 padding: 5px;""",
                 "top_next_label": """background-color: #CEFF1A;
                                      color: #000000; 
                                      font-size: 30px; 
                                      font-family: BalooDa2-Regular; 
                                      font-weight: bold;""",
                 "center_lower_label": """background-color: #F3F3F4;
                                          border-radius: 30px;
                                          padding: 10px;""",
                 "center_top_label": """background-color: #FFFFFF;
                                        border-radius: 40px;
                                        padding: 10px;""",
                 "text_input": """background-color: #FFFFFF;
                                  color: #000000;
                                  border-radius: 15px;
                                  padding: 10px;
                                  font-size: 15px;
                                  font-family: BalooDa2-Regular;""",
                 "generate_button": """background-color: #FFFFFF;
                                       color: #000000;
                                       border-radius: 15px;
                                       padding: 10px;
                                       font-size: 15px;
                                       font-family: BalooDa2-Regular;
                                       font-weight: bold;""",
                  "lower_label": """background-color: #CEFF1A;
                                    border-radius: 10px;
                                    padding: 5px;"""}
        
        themes = {"lite": lite,
                  "dark": dark,
                  "green": green}
        
        return themes[theme][layout]

        
    def top_label(self):
        self.top_label = QLabel(self.window)
        self.top_label.setStyleSheet(self.color_themes("green", "top_label"))
        self.top_label.setFixedWidth(190)
        self.top_label.setFixedHeight(30)
        self.top_label.move(155, -10)
        self.top_label.raise_()
        
        
    def top_next_label(self):
        self.top_next_label = QLabel(self.window)
        self.top_next_label.setText("PikI")
        self.top_next_label.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
        id_font = QFontDatabase.addApplicationFont("BalooDa2-Regular.ttf")
        families = QFontDatabase.applicationFontFamilies(id_font)
        self.top_next_label.setStyleSheet(self.color_themes("green", "top_next_label"))
        self.top_next_label.setFixedWidth(500)
        self.top_next_label.setFixedHeight(95)
        self.top_next_label.move(0, 0)
        self.top_next_label.lower()
        
        
    def center_lower_label(self):
        self.center_lower_label = QLabel(self.window)
        self.center_lower_label.setStyleSheet(self.color_themes("green", "center_lower_label"))
        self.center_lower_label.setFixedWidth(500)
        self.center_lower_label.setFixedHeight(500)
        self.center_lower_label.move(0, 70)
        
        
    def center_top_label(self):
        self.center_top_label = QLabel(self.window)
        self.center_top_label.setStyleSheet(self.color_themes("green", "center_top_label"))
        self.center_top_label.setFixedWidth(450)
        self.center_top_label.setFixedHeight(450)
        self.center_top_label.move(25, 95)
        self.center_top_label.raise_()
     
        
    def text_input(self):
        self.text_input = QPlainTextEdit(self.window)
        self.text_input.setStyleSheet(self.color_themes("green", "text_input"))
        self.text_input.setFixedWidth(450)
        self.text_input.setFixedHeight(50)
        self.text_input.move(25, 575)
        
        
    def generate_button(self):
        self.generate_button = QPushButton(self.window)
        self.generate_button.setText("Generate")
        self.generate_button.setStyleSheet(self.color_themes("green", "generate_button"))
        self.generate_button.setFixedWidth(450)
        self.generate_button.setFixedHeight(50)
        self.generate_button.move(25, 655)
        self.generate_button.raise_()
        
        
    def lower_label(self):
        self.lower_label = QLabel(self.window)
        self.lower_label.setStyleSheet(self.color_themes("green", "lower_label"))
        self.lower_label.setFixedWidth(500)
        self.lower_label.setFixedHeight(140)
        self.lower_label.move(0, 640)
        self.lower_label.lower()
        
        
    def run(self):
        self.top_label()
        self.top_next_label()
        self.center_lower_label()
        self.center_top_label()
        self.text_input()
        self.generate_button()
        self.lower_label()
        self.window.show()
        self.app.exec()
        
        
if __name__ == "__main__":
    app = MainApp()
    app.run()
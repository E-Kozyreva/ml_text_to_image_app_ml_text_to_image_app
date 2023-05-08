import PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QPlainTextEdit
from PyQt6.QtGui import QIcon, QFontDatabase


app = QApplication([])
window = QWidget()
window.setWindowTitle("PikI")
window.setGeometry(100, 100, 500, 720)
window.setStyleSheet("background-color: #F3F3F4;")   


top_label = QLabel(window)
top_label.setStyleSheet("""background-color: #FFFFFF;
                            border-radius: 10px;
                            padding: 5px;""")
top_label.setFixedWidth(190)
top_label.setFixedHeight(30)
top_label.move(155, -10)
top_label.raise_()

top_next_label = QLabel(window)
top_next_label.setText("PikI")
top_next_label.setAlignment(PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter)
id_font = QFontDatabase.addApplicationFont("BalooDa2-Regular.ttf")
families = QFontDatabase.applicationFontFamilies(id_font)
top_next_label.setStyleSheet("""background-color: #CEFF1A;
                                color: #000000; 
                                font-size: 30px; 
                                font-family: BalooDa2-Regular; 
                                font-weight: bold;""")
top_next_label.setFixedWidth(500)
top_next_label.setFixedHeight(95)
top_next_label.move(0, 0)
top_next_label.lower()


center_lower_label = QLabel(window)
center_lower_label.setStyleSheet("""background-color: #F3F3F4;
                                    border-radius: 30px;
                                    padding: 10px;
                                    """)
center_lower_label.setFixedWidth(500)
center_lower_label.setFixedHeight(500)
center_lower_label.move(0, 70)


center_top_label = QLabel(window)
center_top_label.setStyleSheet("""background-color: #FFFFFF;
                                  border-radius: 40px;
                                  padding: 10px;
                                  """)
center_top_label.setFixedWidth(450)
center_top_label.setFixedHeight(450)
center_top_label.move(25, 95)
center_top_label.raise_()


text_input = QPlainTextEdit(window)
text_input.setPlainText("Enter the text to generate the image...")
text_input.setStyleSheet("""background-color: #FFFFFF;
                            color: #000000;
                            border-radius: 15px;
                            padding: 10px;
                            font-size: 15px;
                            font-family: BalooDa2-Regular;
                            """)
text_input.setFixedWidth(450)
text_input.setFixedHeight(50)
text_input.move(25, 575)


generate_button = QPushButton(window)
generate_button.setText("Generate")
generate_button.setStyleSheet("""background-color: #FFFFFF;
                                 color: #000000;
                                 border-radius: 15px;
                                 padding: 10px;
                                 font-size: 15px;
                                 font-family: BalooDa2-Regular;
                                 font-weight: bold;""")
generate_button.setFixedWidth(450)
generate_button.setFixedHeight(50)
generate_button.move(25, 655)
generate_button.raise_()


lower_label = QLabel(window)
lower_label.setStyleSheet("""background-color: #CEFF1A;
                             border-radius: 10px;
                             padding: 5px;""")
lower_label.setFixedWidth(500)
lower_label.setFixedHeight(140)
lower_label.move(0, 640)
lower_label.lower()


window.show()
app.exec()

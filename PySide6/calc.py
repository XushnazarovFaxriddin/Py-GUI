from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator App")
        self.setGeometry(100, 100, 300, 400)
        self.setWindowIcon(QIcon("src/buxdu-logo.png"))
        self.create_layout()
    def create_layout(self):
        self.layout = QVBoxLayout()
        lineEditor = QLineEdit()
        lineEditor.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # set font size
        font = lineEditor.font()
        font.setPointSize(20)
        lineEditor.setFont(font)
        self.display = lineEditor
        self.layout.addWidget(self.display)
        self.create_buttons()
        self.setLayout(self.layout)
    def create_buttons(self):
        buttons = [
            [".", "(", ")", "^"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"]
        ]
        for row in buttons:
            h_layout = QHBoxLayout()
            for label in row:
                button = QPushButton(label)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.clicked.connect(self.button_click)
                h_layout.addWidget(button)
            self.layout.addLayout(h_layout)
    def validate(self, text):
        try:
            eval(text)
            return True
        except:
            return False
    def button_click(self):
        button = self.sender()
        label = button.text()
        if label == "C":
            self.display.clear()
        elif label == "=":
            if not self.validate(self.display.text()):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Invalid input")
                msg.setWindowTitle("Error")
                msg.exec()
                self.display.setText("0")
                return
            result = str(eval(self.display.text()))
            self.display.setText(result)
        else:
            current_text = self.display.text()
            new_text = current_text + label
            self.display.setText(new_text)
        
app = QApplication()
window = CalculatorApp()
window.show()
sys.exit(app.exec())
        
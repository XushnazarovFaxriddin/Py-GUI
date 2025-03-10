import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple App")
        self.setGeometry(100, 100, 400, 200)
        
        # Add a QLabel widget
        self.label = QLabel("Hello, PySide6!", self)
        self.label.move(150, 90)

app = QApplication(sys.argv)
window = SimpleApp()
window.show()
sys.exit(app.exec_())
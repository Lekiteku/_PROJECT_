from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

class IpLineEditApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create a QLineEdit for entering an IP address
        self.ip_line_edit = QLineEdit(self)
        
        # Create a regular expression for IP addresses
        ip_regex = QRegExp(
            r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])\."
            r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])\."
            r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])\."
            r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9])$"
        )
        
        # Create a validator for the QLineEdit using the IP address regex
        ip_validator = QRegExpValidator(ip_regex, self.ip_line_edit)
        self.ip_line_edit.setValidator(ip_validator)

        # Set up the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.ip_line_edit)

        # Set up the main window
        self.setGeometry(100, 100, 300, 100)
        self.setWindowTitle('IP Address Line Edit Example')
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = IpLineEditApp()
    app.exec_()

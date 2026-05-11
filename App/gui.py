from PyQt5.QtWidgets import *
import sys

def start_gui():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("InputOS")
    window.resize(500, 300)

    layout = QVBoxLayout()

    label = QLabel("Número IP do 3DS")
    ip_input = QLineEdit()

    button = QPushButton("Conectar")

    layout.addWidget(label)
    layout.addWidget(ip_input)
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())

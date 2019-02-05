#/usr/bin/python3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette

app = QApplication([])
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.black)
app.setPalette(palette)

window = QMainWindow()

front_panel = QWidget()
window.setCentralWidget(front_panel)
window.show()

front_layout = QVBoxLayout()
front_panel.setLayout(front_layout)

title_label = QLabel("Welcome to the Python Transfer Protocol (PTP) v0.1")
connect_label = QLabel("Insert an IP Address to connect to:")
connect_input = QLineEdit()
connect_button = QPushButton("Connect")
listen_label = QLabel("Alternatively, listen to incoming connections:")
listen_input = QLineEdit()
listen_button = QPushButton("Listen")

front_layout.addWidget(title_label)
front_layout.addSpacing(15)
front_layout.addWidget(connect_label)
front_layout.addWidget(connect_input)
front_layout.addWidget(connect_button)
front_layout.addSpacing(30)
front_layout.addWidget(listen_label)
front_layout.addWidget(listen_input)
front_layout.addWidget(listen_button)

# ptp_panel = QWidget()
# window.setCentralWidget(ptp_panel)
# window.show()

# ptp_subpanel = QWidget()
# ptp_layout = QVBoxLayout(ptp_subpanel)
# ptp_panel.setLayout(ptp_layout)
# ptp_panel_layout = QHBoxLayout()
# ptp_subpanel.setLayout(ptp_panel_layout)

# ptp_prototype = QLabel("Hello")
# ptp_prototype2 = QLabel("World")

# ptp_panel_layout.addWidget(ptp_prototype)
# ptp_panel_layout.addWidget(ptp_prototype2)

app.exec_()
# This is the application developed using PyQt5
# It allows for a graphical visualisation of the file transfer protocol 

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette

from network import Network

import os

# Naming convention for convenience:
# m --> main and f --> front
# l --> listen and c --> connect
# s --> send and r --> receive
# h --> horizontal and v --> vertical

# Create a container that allows making widgets more conveniently
def make_container_widget(widgets, vertical = True):
    """Takes a list of widgets and creates a vertical or horizontal layout with the widgets in it."""

    new_widget = QWidget()

    if vertical:
        new_layout = QVBoxLayout()
    else:
        new_layout = QHBoxLayout()
    
    for widget in widgets:
        new_layout.addWidget(widget)
    
    new_widget.setLayout(new_layout)

    return new_widget

# The main application class that is used in main.py
class Application():
    def __init__(self):
        # Creation of the main application and style
        app = QApplication(["SPTP"])
        app.setStyle('Fusion')
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.black)
        app.setPalette(palette)

        # Creation of the main window
        window = QMainWindow()
        
        # Creation of widget panels
        self.create_connection_panel()
        self.create_main_panel

        # Display the front panel
        window.setCentralWidget(self.f_panel)

        # Show the window
        window.show()

        # Attributes for later references
        self.app = app # Used in execute()
        self.window = window # Used in create_m_panel()

    # Create panel that is used to initiate a connection
    def create_connection_panel(self):
        fc_button = QRadioButton("Connect to IP Address")
        fl_button = QRadioButton("Listen for Connection")

        # Creation of a vertical connection widget
        c_label = QLabel("Input an IP Address and Port to connect:")
        c_label_IP = QLabel("IP:")
        c_label_port = QLabel("Port:")

        c_input_host = QLineEdit()
        c_input_host.setText("127.0.0.1")
        c_input_port = QLineEdit()
        c_input_port.setText("8888")

        c_button = QPushButton("Connect")      
        c_button.clicked.connect(self.c_button_clicked)

        c_subpanel = make_container_widget([c_label_IP, c_input_host, c_label_port, c_input_port], vertical = False)
        c_panel = make_container_widget([c_label, c_subpanel, c_button])
        
        # Creation of a vertical listening widget
        l_label = QLabel("Listen to incoming connections:")
        l_label_port = QLabel("Port:")
        l_input = QLineEdit()
        l_input.setText("4444")
        l_button = QPushButton("Listen")
        l_button.clicked.connect(self.l_button_clicked)

        l_subpanel = make_container_widget([l_label_port, l_input],vertical = False)
        l_panel = make_container_widget([l_label, l_subpanel, l_button])

        t_label = QLabel("Simple Python Transfer Protocol")

        # Creation of an entire front panel, with radio buttons that toggle between connection and listening
        f_panel = make_container_widget([t_label, fc_button, fl_button, l_panel, c_panel])

        l_panel.hide()
        c_panel.hide()

        # Functions that determine which widget is visible at one time
        def show_c_panel():
            l_panel.hide()
            c_panel.show()
            self.window.adjustSize()

        def show_l_panel():
            c_panel.hide()
            l_panel.show()
            self.window.adjustSize()

        fc_button.clicked.connect(show_c_panel)
        fl_button.clicked.connect(show_l_panel)

        # Attribute for later references
        self.f_panel = f_panel # Used in __init__()
        self.c_input_host = c_input_host # Used in c_button_clicked()
        self.c_input_port = c_input_port # Used in c_button_clicked()
        self.l_input = l_input # Used in l_button_clicked()

    # Create a main panel that serves as the primary application interface
    def create_main_panel(self):

        # Create two displays for the local and remote file systems
        m_local_fs_display = QTextEdit()
        m_local_fs_display.setReadOnly(True)
        m_remote_fs_display = QTextEdit()
        m_remote_fs_display.setReadOnly(True)

        files = os.listdir("/root/sptp")

        for file in files:
            m_local_fs_display.append(file)

        # Combine the displays into a container widget
        mh_panel = make_container_widget([m_local_fs_display, m_remote_fs_display], vertical = False)

        mh_history = QTextEdit()
        mh_history.setReadOnly(True)
        mh_history.setFixedHeight(100)

        # Prototyping the command line interface
        msr_button = QPushButton()
        msr_input = QLineEdit()
        
        # Transfer command line
        mh_input = make_container_widget([msr_button, msr_input], vertical = False)

        # Create entire panel that will be the window layout
        m_panel = make_container_widget([mh_panel, mh_history, mh_input])

        self.window.setCentralWidget(m_panel)
        self.window.setFixedSize(800,800)
        self.window.setWindowTitle("Simple Python Transfer Protocol")

    def create_listen_panel(self):
        pass

    def c_button_clicked(self):

        self.connection = Network.Connection(self.c_input_host.text(), self.c_input_port.text())

        print("Connecting Successful")

    def l_button_clicked(self):

        self.listener = Network.Listener(self.l_input.text())

        print("Listening Successful")
        self.accepting = True

    # Running the program
    def execute(self):
        self.app.exec()

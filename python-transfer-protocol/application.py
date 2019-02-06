#/usr/bin/python3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette

# Naming convention for convenience:
# m --> main and f --> front
# l --> listen and c --> connect

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

class Application():
    def __init__(self):
        # Creation of the main application and style
        app = QApplication([])
        app.setStyle('Fusion')
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.black)
        app.setPalette(palette)

        # Creation of the main window
        window = QMainWindow()
        
        # Creation of widget panels
        self.create_connection_panel()
        self.create_m_panel

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
        c_label = QLabel("Input an IP Address to connect:")
        c_label_IP = QLabel("IP:")
        c_input = QLineEdit()
        c_input.setText("127.0.0.1")

        c_button = QPushButton("Connect")      
        c_button.clicked.connect(self.create_m_panel)

        c_subpanel = make_container_widget([c_label_IP, c_input], vertical = False)
        c_panel = make_container_widget([c_label, c_subpanel, c_button])
        
        # Creation of a vertical listening widget
        l_label = QLabel("Listen to incoming connections:")
        l_label_port = QLabel("Port:")
        l_input = QLineEdit()
        l_input.setText("4444")
        l_button = QPushButton("Listen")

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
            c_panel.adjustSize()

        def show_l_panel():
            c_panel.hide()
            l_panel.show()
            l_panel.adjustSize()

        fc_button.clicked.connect(show_c_panel)
        fl_button.clicked.connect(show_l_panel)

        # Attribute for later references
        self.f_panel = f_panel # Used in __init__()

    # Create a main panel that serves as the primary application interface
    def create_m_panel(self):
        # Create two displays for the local and remote file systems
        m_local_fs_display = QTextEdit()
        m_local_fs_display.setReadOnly(True)
        m_remote_fs_display = QTextEdit()
        m_remote_fs_display.setReadOnly(True)

        # Combine the displays into a container widget
        mh_panel = make_container_widget([m_local_fs_display, m_remote_fs_display], vertical = False)
        
        # PROTOTYPING
        m_prototype1 = QLineEdit()
        m_prototype2 = QLineEdit()

        # VERTICAL PROTOTYPE
        mv_panel = make_container_widget([m_prototype1, m_prototype2])

        # Create entire panel that will be the window layout
        m_panel = make_container_widget([mh_panel, mv_panel])

        self.window.setCentralWidget(m_panel)

    def execute(self):
        self.app.exec()
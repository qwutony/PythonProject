# This is the application developed using PyQt5
# It allows for a graphical visualisation of the file transfer protocol 

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QMovie

from network import Network

import os

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
        """Initialisation and creation of the main application"""
        """# Naming convention for convenience:
            # m --> main and f --> front
            # l --> listen and c --> connect
            # s --> send and r --> receive
            # h --> horizontal and v --> vertical"""
        
        app = QApplication(["SPTP"])
        app.setStyle('Fusion')
        palette = QPalette()
        palette.setColor(QPalette.ButtonText, Qt.black)
        app.setPalette(palette)

        # Creation of the main window
        window = QMainWindow()
        
        # Creation of widget panels
        self.create_connection_panel()
        self.create_main_panel_connect
        self.create_main_panel_listen

        # Display the front panel
        window.setCentralWidget(self.f_panel)

        # Show the window
        window.show()

        # Attributes for later references
        self.app = app # Used in execute()
        self.window = window # Used in create_m_panel()

        self.timer = QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.tick)

        self.accepting = False
        self.receiving = False
        self.connection = None

        self.client = False
        self.server = False

    def create_connection_panel(self):
        """Create panel that is used to initiate a connection"""
        fc_button = QRadioButton("Connect to IP Address")
        fl_button = QRadioButton("Listen for Connection")

        """Creation of a vertical connection widget"""
        c_label = QLabel("Input an IP Address and Port to connect:")
        c_label_IP = QLabel("IP:")
        c_label_port = QLabel("Port:")

        c_input_host = QLineEdit()
        c_input_host.setText("127.0.0.1")
        c_input_port = QLineEdit()
        c_input_port.setText("8888")

        c_button = QPushButton("Connect")      
        c_button.clicked.connect(self.create_main_panel_connect)

        c_subpanel = make_container_widget([c_label_IP, c_input_host, c_label_port, c_input_port], vertical = False)
        c_panel = make_container_widget([c_label, c_subpanel, c_button])
        
        """Creation of a vertical listening widget"""
        l_label = QLabel("Listen to incoming connections:")
        l_label_port = QLabel("Port:")
        l_input = QLineEdit()
        l_input.setText("8888")
        l_button = QPushButton("Listen")
        l_button.clicked.connect(self.create_main_panel_listen)

        l_subpanel = make_container_widget([l_label_port, l_input],vertical = False)
        l_panel = make_container_widget([l_label, l_subpanel, l_button])

        t_label = QLabel("Simple Python Transfer Protocol")

        """Creation of an entire front panel, with radio buttons that toggle between connection and listening"""
        f_panel = make_container_widget([t_label, fc_button, fl_button, l_panel, c_panel])

        l_panel.hide()
        c_panel.hide()

        def show_c_panel():
            """Functions that determine which widget is visible at one time"""
            l_panel.hide()
            c_panel.show()
            self.window.adjustSize()

        def show_l_panel():
            """Functions that determine which widget is visible at one time"""
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

    def create_main_panel_connect(self):
        """Create a main panel that serves as the primary application interface"""

        self.connection = Network.Connection(self.c_input_host.text(), self.c_input_port.text())

        # Create two displays for the local and remote file systems
        cm_local_fs_display = QTextEdit()
        cm_local_fs_display.setReadOnly(True)
        cm_remote_fs_display = QTextEdit()
        cm_remote_fs_display.setReadOnly(True)

        files = os.listdir("/root/sptp_client")
        """Directory in which files are displayed"""

        connect_files = []

        for file in files:
            cm_local_fs_display.append(file)
            connect_files.append(file)

        mh_panel = make_container_widget([cm_local_fs_display, cm_remote_fs_display], vertical = False)
        """Combine the displays into a container widget"""

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
        self.window.setWindowTitle("Local: Simple Python Transfer Protocol")

        self.connect_files = connect_files

        self.cm_remote_fs_display = cm_remote_fs_display

    def create_main_panel_listen(self):
        """Creating the listening version of the interface"""
        self.listener = Network.Listener(self.l_input.text())

        self.accepting = True

        # Create two displays for the local and remote file systems
        m_local_fs_display = QTextEdit()
        m_local_fs_display.setReadOnly(True)
        m_remote_fs_listen = QTextEdit()
        m_remote_fs_listen.setReadOnly(True)

        files = os.listdir("/root/sptp_server")

        listen_files = []

        for file in files:
            m_local_fs_display.append(file)
            listen_files.append(file)

        # Combine the displays into a container widget
        mh_panel = make_container_widget([m_local_fs_display, m_remote_fs_listen], vertical = False)

        mh_history = QTextEdit()
        mh_history.setReadOnly(True)
        mh_history.setFixedHeight(100)

        # Prototyping the command line interface
        msr_button = QPushButton()
        msr_input = QLineEdit()
        
        # Transfer command line
        mh_input = make_container_widget([msr_button, msr_input], vertical = False)

        wait_label = QLabel("Waiting for a connection...")
        load = QLabel()
        movie = QMovie("loading.gif")
        load.setMovie(movie)
        movie.start()
            
        wait_panel = make_container_widget([wait_label, load])

        # Create entire panel that will be the window layout
        m_panel = make_container_widget([mh_panel, mh_history, mh_input])

        all_panel = make_container_widget([wait_panel, m_panel])

        m_panel.hide()

        self.window.setCentralWidget(all_panel)
        self.window.setWindowTitle("Server: Simple Python Transfer Protocol")

        self.m_remote_fs_listen = m_remote_fs_listen

        self.listen_files = listen_files
        self.wait_panel = wait_panel
        self.m_panel = m_panel

    def tick(self):
        """The application tick which constantly determines the current stage of the application"""
        if self.accepting:
            self.connection = self.listener.try_get_connection()
            self.server = True
            if self.connection is not None:
                self.accepting = False
                self.receiving = True
                self.wait_panel.hide()
                self.m_panel.show()
                self.window.setFixedSize(800,800)

        elif self.receiving:
                if self.server:
                    they_sent = self.connection.try_receive()
                    if they_sent is not None:
                        file_list = str(they_sent, 'utf-8')
                        self.m_remote_fs_listen.append(file_list)
                        for i in range(len(self.listen_files)):
                            self.connection.send(str.encode(self.listen_files[i] + "\n"))
                elif self.client:
                    they_sent = self.connection.try_receive()
                    if they_sent is not None:
                        file_list = str(they_sent, 'utf-8')
                        self.cm_remote_fs_display.append(file_list)
                else:
                    print("Error: Please check your connection and try again")

        elif self.connection is not None:
            self.connection.try_connect()
            self.client = True
            if self.connection.connected:
                self.receiving = True
                for i in range(len(self.connect_files)):
                        self.connection.send(str.encode(self.connect_files[i] + "\n"))

    # Running the program
    def execute(self):
        """Running the program, referenced in main"""
        self.app.exec()

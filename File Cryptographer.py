import os
import webbrowser
import random
import string
import sys
from itertools import cycle
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QDialog, QHBoxLayout, QFrame, QTabWidget, QLabel, QPushButton, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QWidget


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowIcon(QIcon(r"Files/icon.ico"))
        self.setFixedSize(300, 100)
        self.setWindowTitle("About us")

        discription = QLabel(self)
        discription.setGeometry(75, 10, 150, 30)
        discription.setAlignment(Qt.AlignmentFlag.AlignCenter)
        discription.setText("This program made by Sina.f")

        horizontalLayoutWidget = QWidget(self)
        horizontalLayoutWidget.setGeometry(15, 50, 270, 40)
        horizontalLayout = QHBoxLayout(horizontalLayoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(12)

        btn_github = QPushButton(horizontalLayoutWidget)
        btn_github.setText("GitHub")
        btn_github.clicked.connect(lambda: webbrowser.open(
            'https://github.com/sina-programer'))

        btn_instagram = QPushButton(horizontalLayoutWidget)
        btn_instagram.setText("Instagram")
        btn_instagram.clicked.connect(lambda: webbrowser.open(
            'https://www.instagram.com/sina.programer'))

        btn_telegram = QPushButton(horizontalLayoutWidget)
        btn_telegram.setText("Telegram")
        btn_telegram.clicked.connect(
            lambda: webbrowser.open('https://t.me/sina_programer'))

        horizontalLayout.addWidget(btn_github)
        horizontalLayout.addWidget(btn_instagram)
        horizontalLayout.addWidget(btn_telegram)


class Cryptographer:
    def cryptography(self, fileName, newName, key: bytes):
        with open(fileName, 'rb') as file:
            data = file.read()

        cryptographed = self.xor(data, key)

        with open(newName, 'wb') as file:
            file.write(cryptographed)

    @staticmethod
    def generate_key(key_name):
        strings = string.ascii_letters + string.digits + \
            string.hexdigits + string.ascii_uppercase + string.punctuation
        key = ''.join(random.sample(strings, 50)).encode()

        with open(key_name, 'wb') as keyFile:
            keyFile.write(key)

    @staticmethod
    def load_key(key_name):
        with open(key_name, 'rb') as keyFile:
            key = keyFile.read()

        return key

    @staticmethod
    def xor(data, key):
        return bytes(a ^ b for a, b in zip(data, cycle(key)))


class Widget(QMainWindow):
    def __init__(self):
        super(Widget, self).__init__()
        self.cryptographer = Cryptographer()
        self.aboutDialog = AboutDialog()
        self.key = None

        self.setupUi()

    def setupUi(self):
        window_icon = QIcon(QPixmap(r"Files\icon.ico"))

        self.setGeometry(430, 270, 580, 190)
        self.setFixedSize(580, 190)
        self.setWindowIcon(window_icon)
        self.setWindowTitle("File Cryptographer")

        key_frame = QFrame(self)
        key_frame.setGeometry(440, 41, 121, 120)

        load_key_btn_key_frame = QPushButton(key_frame)
        load_key_btn_key_frame.setGeometry(25, 40, 80, 30)
        load_key_btn_key_frame.setText("Load KEY")
        load_key_btn_key_frame.clicked.connect(self.load_key)

        generate_key_btn_key_frame = QPushButton(key_frame)
        generate_key_btn_key_frame.setGeometry(25, 80, 80, 30)
        generate_key_btn_key_frame.setText("Generate KEY")
        generate_key_btn_key_frame.clicked.connect(self.generate_key)

        self.selected_key_lbl_key_frame = QLabel(key_frame)
        self.selected_key_lbl_key_frame.setGeometry(25, 10, 100, 20)
        self.selected_key_lbl_key_frame.setText("KEY: ")

        lineEdit_font = QFont()
        lineEdit_font.setPointSize(10)
        lineEdit_font.setWeight(50)
        lineEdit_font.setKerning(True)

        tabWidget = QTabWidget(self)
        tabWidget.setGeometry(20, 35, 400, 130)
        tabWidget.setMovable(True)

        encoderTab_icon = QIcon(QPixmap(r"Files\encrypt.ico"))
        encoderTab = QWidget()

        open_file_btn_encoderTab = QPushButton(encoderTab)
        open_file_btn_encoderTab.setGeometry(290, 20, 81, 31)
        open_file_btn_encoderTab.setText("Open file")
        open_file_btn_encoderTab.clicked.connect(self.open_encode_file)

        encode_btn_encoderTab = QPushButton(encoderTab)
        encode_btn_encoderTab.setGeometry(290, 60, 81, 31)
        encode_btn_encoderTab.setText("Encrypt")
        encode_btn_encoderTab.clicked.connect(self.encrypt)

        self.file_path_line_encoder_tab = QLineEdit(encoderTab)
        self.file_path_line_encoder_tab.setGeometry(10, 20, 261, 31)
        self.file_path_line_encoder_tab.setFont(lineEdit_font)
        self.file_path_line_encoder_tab.setFocusPolicy(
            Qt.FocusPolicy.ClickFocus)
        self.file_path_line_encoder_tab.setReadOnly(True)
        self.file_path_line_encoder_tab.setPlaceholderText("file path")

        decoderTab_icon = QIcon(QPixmap(r"Files\decrypt.ico"))
        decoderTab = QWidget()

        open_file_btn_decoderTab = QPushButton(decoderTab)
        open_file_btn_decoderTab.setGeometry(290, 20, 81, 31)
        open_file_btn_decoderTab.setText("Open file")
        open_file_btn_decoderTab.clicked.connect(self.open_decode_file)

        decode_btn_decoderTab = QPushButton(decoderTab)
        decode_btn_decoderTab.setGeometry(290, 60, 81, 31)
        decode_btn_decoderTab.setText("Decrypt")
        decode_btn_decoderTab.clicked.connect(self.decrypt)

        self.file_path_line_decoder_tab = QLineEdit(decoderTab)
        self.file_path_line_decoder_tab.setGeometry(10, 20, 261, 31)
        self.file_path_line_decoder_tab.setFont(lineEdit_font)
        self.file_path_line_decoder_tab.setFocusPolicy(
            Qt.FocusPolicy.ClickFocus)
        self.file_path_line_decoder_tab.setReadOnly(True)
        self.file_path_line_decoder_tab.setPlaceholderText("file path")

        tabWidget.addTab(encoderTab, encoderTab_icon, '')
        tabWidget.setTabText(tabWidget.indexOf(encoderTab), "Encrypt  ")
        tabWidget.setTabToolTip(tabWidget.indexOf(
            encoderTab), "You can encrypt\nyour files here")

        tabWidget.addTab(decoderTab, decoderTab_icon, '')
        tabWidget.setTabText(tabWidget.indexOf(decoderTab), "Decrypt   ")
        tabWidget.setTabToolTip(tabWidget.indexOf(
            decoderTab), "You can decrypt\nyour files here")

        self.init_menu()

    def encrypt(self):
        if self.key:
            file_path = self.file_path_line_encoder_tab.text()

            if file_path:
                save_path, _ = QFileDialog.getSaveFileName(
                    self, 'Save Encrypt File', '', "Encrypt Files (*.encrypt)")

                if save_path:
                    self.cryptographer.cryptography(
                        file_path, save_path, self.key)

            else:
                QMessageBox.critical(
                    self, 'ERROR', '\nPlease open a file for encrypt!\t\n')

        else:
            QMessageBox.critical(
                self, 'ERROR', '\nPlease first load a KEY!\t\n')

    def decrypt(self):
        if self.key:
            file_path = self.file_path_line_decoder_tab.text()

            if file_path:
                save_path, _ = QFileDialog.getSaveFileName()

                if save_path:
                    self.cryptographer.cryptography(
                        file_path, save_path, self.key)

            else:
                QMessageBox.critical(
                    self, 'ERROR', '\nPlease open a file for decrypt!\t\n')

        else:
            QMessageBox.critical(
                self, 'ERROR', '\nPlease first load a KEY!\t\n')

    def load_key(self):
        key_path, _ = QFileDialog.getOpenFileName(
            self, 'Open Key File', '', "Key Files (*.key)")

        if key_path:
            key_name = os.path.basename(key_path)
            self.selected_key_lbl_key_frame.setText(f'KEY:  {key_name}')
            self.key = self.cryptographer.load_key(key_path)

    def generate_key(self):
        key_path, _ = QFileDialog.getSaveFileName(
            self, 'Save Key File', '', "Key Files (*.key)")

        if key_path:
            self.cryptographer.generate_key(key_path)

    def open_encode_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if file_path:
            self.file_path_line_encoder_tab.setText(file_path)

    def open_decode_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Open File', '', "Encrypt Files (*.encrypt)")
        if file_path:
            self.file_path_line_decoder_tab.setText(file_path)

    def init_menu(self):
        helpAction = QAction("Help", self)
        helpAction.triggered.connect(
            lambda: QMessageBox.information(self, 'Help', HELP_MESSAGE))

        aboutAction = QAction("About us", self)
        aboutAction.triggered.connect(lambda: self.aboutDialog.exec())

        menu = self.menuBar()
        menu.addAction(helpAction)
        menu.addAction(aboutAction)


HELP_MESSAGE = '''
1) Load a key (if you don't have any key, generate a key then load it).
2) Open file for encrypt or decrypt.
3) Press encrypt/decrypt button and choose save path.
4) Your file is ready now!
'''


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

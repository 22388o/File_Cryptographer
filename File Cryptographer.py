from PyQt5 import QtCore, QtGui, QtWidgets
from itertools import cycle
import webbrowser
import random
import string
import sys 
import os

class AboutDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.setupUi()
    
    def setupUi(self):        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setFixedSize(300, 100)
        self.setWindowTitle("About us")

        discription = QtWidgets.QLabel(self)
        discription.setGeometry(75, 10, 150, 30)
        discription.setAlignment(QtCore.Qt.AlignCenter)
        discription.setText("This program made by Sina.f")
        
        horizontalLayoutWidget = QtWidgets.QWidget(self)
        horizontalLayoutWidget.setGeometry(15, 50, 270, 40)
        horizontalLayout = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(12)
        
        btn_github = QtWidgets.QPushButton(horizontalLayoutWidget)
        btn_github.setText("GitHub")
        btn_github.clicked.connect(lambda: webbrowser.open('https://github.com/sina-programer'))
        
        btn_instagram = QtWidgets.QPushButton(horizontalLayoutWidget)
        btn_instagram.setText("Instagram")
        btn_instagram.clicked.connect(lambda: webbrowser.open('https://www.instagram.com/sina.programer'))
        
        btn_telegram = QtWidgets.QPushButton(horizontalLayoutWidget)
        btn_telegram.setText("Telegram")
        btn_telegram.clicked.connect(lambda: webbrowser.open('https://t.me/sina_programer'))
        
        horizontalLayout.addWidget(btn_github)
        horizontalLayout.addWidget(btn_instagram)
        horizontalLayout.addWidget(btn_telegram)


class Cryptographer:
    def cryptography(self, fileName, newName, key:bytes):
        with open(fileName, 'rb') as file:
            data = file.read()
        
        cryptographed = self.xor(data, key)  
    
        with open(newName, 'wb') as file:
            file.write(cryptographed)
            
    @staticmethod
    def generate_key(keyName):
        strings = string.ascii_letters + string.digits + string.hexdigits + string.ascii_uppercase + string.punctuation
        key = ''.join(random.sample(strings, 50)).encode()
        
        with open(keyName, 'wb') as keyFile:
            keyFile.write(key)
            
    @staticmethod
    def load_key(keyName):
        with open(keyName, 'rb') as keyFile:
            key = keyFile.read()
            
        return key 

    @staticmethod
    def xor(data, key):
        return bytes(a ^ b for a, b in zip(data, cycle(key)))
    

class Widget(QtWidgets.QMainWindow):
    def __init__(self):
        super(Widget, self).__init__()
        self.cryptographer = Cryptographer()
        self.aboutDialog = AboutDialog()
        self.key = None
        
        self.setupUi()
        self.show()

    def setupUi(self):
        window_icon = QtGui.QIcon()
        window_icon.addPixmap(QtGui.QPixmap(r"Files\icon.ico"))

        self.setGeometry(430, 270, 580, 190)
        self.setFixedSize(580, 190)
        self.setWindowIcon(window_icon)
        self.setWindowTitle("File Cryptographer")


        keyFrame = QtWidgets.QFrame(self)
        keyFrame.setGeometry(440, 41, 121, 120)
        load_key_btn_keyFrame = QtWidgets.QPushButton(keyFrame)
        load_key_btn_keyFrame.setGeometry(25, 40, 80, 30)
        load_key_btn_keyFrame.setText("Load KEY")
        load_key_btn_keyFrame.clicked.connect(self.load_key)
        generate_key_btn_keyFrame = QtWidgets.QPushButton(keyFrame)
        generate_key_btn_keyFrame.setGeometry(25, 80, 80, 30)
        generate_key_btn_keyFrame.setText("Generate KEY")
        generate_key_btn_keyFrame.clicked.connect(self.generate_key)
        self.selected_key_lbl_keyFrame = QtWidgets.QLabel(keyFrame)
        self.selected_key_lbl_keyFrame.setGeometry(25, 10, 100, 20)
        self.selected_key_lbl_keyFrame.setText("KEY: ")


        lineEdit_font = QtGui.QFont()
        lineEdit_font.setPointSize(10)
        lineEdit_font.setWeight(50)
        lineEdit_font.setKerning(True)
                
        tabWidget = QtWidgets.QTabWidget(self)
        tabWidget.setGeometry(20, 35, 400, 130)
        tabWidget.setMovable(True)
        
        encoderTab_icon = QtGui.QIcon()
        encoderTab_icon.addPixmap(QtGui.QPixmap(r"Files\encrypt.ico"))
        encoderTab = QtWidgets.QWidget()
        
        open_file_btn_encoderTab = QtWidgets.QPushButton(encoderTab)
        open_file_btn_encoderTab.setGeometry(290, 20, 81, 31)
        open_file_btn_encoderTab.setText("Open file")
        open_file_btn_encoderTab.clicked.connect(self.open_encode_file)
        encode_btn_encoderTab = QtWidgets.QPushButton(encoderTab)
        encode_btn_encoderTab.setGeometry(290, 60, 81, 31)
        encode_btn_encoderTab.setText("Encrypt")
        encode_btn_encoderTab.clicked.connect(self.encrypt)
        self.file_path_lineE_encoderTab = QtWidgets.QLineEdit(encoderTab)
        self.file_path_lineE_encoderTab.setGeometry(10, 20, 261, 31)
        self.file_path_lineE_encoderTab.setFont(lineEdit_font)
        self.file_path_lineE_encoderTab.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.file_path_lineE_encoderTab.setReadOnly(True)
        self.file_path_lineE_encoderTab.setPlaceholderText("file path")
        
        
        decoderTab_icon = QtGui.QIcon()
        decoderTab_icon.addPixmap(QtGui.QPixmap(r"Files\decrypt.ico"))
        decoderTab = QtWidgets.QWidget()

        open_file_btn_decoderTab = QtWidgets.QPushButton(decoderTab)
        open_file_btn_decoderTab.setGeometry(290, 20, 81, 31)
        open_file_btn_decoderTab.setText("Open file")
        open_file_btn_decoderTab.clicked.connect(self.open_decode_file)
        decode_btn_decoderTab = QtWidgets.QPushButton(decoderTab)
        decode_btn_decoderTab.setGeometry(290, 60, 81, 31)
        decode_btn_decoderTab.setText("Decrypt")
        decode_btn_decoderTab.clicked.connect(self.decrypt)
        self.file_path_lineE_decoderTab = QtWidgets.QLineEdit(decoderTab)
        self.file_path_lineE_decoderTab.setGeometry(10, 20, 261, 31)
        self.file_path_lineE_decoderTab.setFont(lineEdit_font)
        self.file_path_lineE_decoderTab.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.file_path_lineE_decoderTab.setReadOnly(True)
        self.file_path_lineE_decoderTab.setPlaceholderText("file path")
        
        
        tabWidget.addTab(encoderTab, encoderTab_icon, '')
        tabWidget.setTabText(tabWidget.indexOf(encoderTab), "Encrypt  ")
        tabWidget.setTabToolTip(tabWidget.indexOf(encoderTab), "<html><head/><body><p>You can encrypt your files here</p></body></html>")
        
        tabWidget.addTab(decoderTab, decoderTab_icon, '')
        tabWidget.setTabText(tabWidget.indexOf(decoderTab), "Decrypt   ")
        tabWidget.setTabToolTip(tabWidget.indexOf(decoderTab), "<html><head/><body><p>You can decrypt your files here</p></body></html>")
        
        self.init_menu()

    def encrypt(self):
        if self.key:
            file_path = self.file_path_lineE_encoderTab.text()
            
            if file_path:            
                save_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Encrypt File', '', "Encrypt Files (*.encrypt)")
    
                if save_path:         
                    self.cryptographer.cryptography(file_path, save_path, self.key)
                        
            else:
                QtWidgets.QMessageBox.critical(self, 'ERROR', '\nPlease open a file for encrypt!\t\n')
                    
        else:
            QtWidgets.QMessageBox.critical(self, 'ERROR', '\nPlease first load a KEY!\t\n')
                         
    def decrypt(self):
        if self.key:
            file_path = self.file_path_lineE_decoderTab.text()
            
            if file_path:            
                save_path, _ = QtWidgets.QFileDialog.getSaveFileName()
    
                if save_path:
                    self.cryptographer.cryptography(file_path, save_path, self.key)
                        
            else:
                QtWidgets.QMessageBox.critical(self, 'ERROR', '\nPlease open a file for decrypt!\t\n')
                    
        else:
            QtWidgets.QMessageBox.critical(self, 'ERROR', '\nPlease first load a KEY!\t\n')
    
    def load_key(self):
        key_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Key File', '', "Key Files (*.key)")
        
        if key_path:
            key_name = os.path.basename(key_path)
            self.selected_key_lbl_keyFrame.setText(f'KEY:  {key_name}')
            
            self.key = self.cryptographer.load_key(key_path)

    def generate_key(self):
        key_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Key File', '', "Key Files (*.key)")
        
        if key_path:
            self.cryptographer.generate_key(key_path)
               
    def open_encode_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if file_path:
            self.file_path_lineE_encoderTab.setText(file_path)
               
    def open_decode_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '', "Encrypt Files (*.encrypt)")
        if file_path:
            self.file_path_lineE_decoderTab.setText(file_path)
            
    def init_menu(self):
        helpAction = QtWidgets.QAction('Help', self)
        helpAction.triggered.connect(lambda: QtWidgets.QMessageBox.information(self, 'Help', help_msg))
        
        aboutAction = QtWidgets.QAction('About us', self)
        aboutAction.triggered.connect(lambda: self.aboutDialog.exec_())
        
        menu = self.menuBar()
        menu.addAction(helpAction)
        menu.addAction(aboutAction)


help_msg = '''\n1_ Load a key (if you don't have any key, generate a key then load it)
2_ Open file for encrypt or decrypt
3_ Press encrypt/decrypt button and choose save path
4_ Your file is ready now!\t\n'''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()

    sys.exit(app.exec_())

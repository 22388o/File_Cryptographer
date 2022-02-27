from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QDialog
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt, QRect


class Ui_Dialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("About us")
        self.resize(300, 99)
        self.setWindowIcon(QIcon(QPixmap("../icon.ico")))
        self.discription = QLabel(self)
        self.discription.setText("This program made by Sina.f")
        self.discription.setGeometry(QRect(75, 10, 150, 30))
        self.discription.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QRect(20, 50, 267, 41))

        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(12)

        self.btn_github = QPushButton(self.horizontalLayoutWidget)
        self.btn_github.setText("GitHub")
        self.horizontalLayout.addWidget(self.btn_github)
        self.btn_instagram = QPushButton(self.horizontalLayoutWidget)
        self.btn_instagram.setText("Instagram")
        self.horizontalLayout.addWidget(self.btn_instagram)
        self.btn_telegram = QPushButton(self.horizontalLayoutWidget)
        self.btn_telegram.setText("Telegram")
        self.horizontalLayout.addWidget(self.btn_telegram)


if __name__ == "__main__":
    import sys
    app = QApplication([])
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

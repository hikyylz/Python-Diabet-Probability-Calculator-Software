import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,700,700)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Spacer Örneği")

        # Label'lar oluştur
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")

        # Spacer eklemek için QVBoxLayout oluştur
        layout = QVBoxLayout()

        # Label'ları layout'a ekle
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # Spacer ekle
        layout.addStretch(1)

        # Buton eklemek için örnek bir QPushButton oluştur
        button = QPushButton("Örnek Buton")

        # Butonu layout'a ekle
        layout.addWidget(button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

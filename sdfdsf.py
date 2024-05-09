import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Widget Görünürlük Örneği")

        # Başlangıçta gösterilecek widget'lar
        self.label1 = QLabel("Label 1")
        self.label2 = QLabel("Label 2")
        self.button = QPushButton("layout hide open button")
        self.button.clicked.connect(self.toggleLabelVisibility)

        # Layout oluştur
        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.label1)
        self.layout1.addWidget(self.label2)

        self.layout2 = QVBoxLayout()
        self.layout2.addWidget(self.button)

        self.layout3 = QVBoxLayout()
        self.layout3.addLayout(self.layout1)
        self.layout3.addLayout(self.layout2)

        # Layout'u içeren bir widget oluştur
        self.widget_with_layout = QWidget()
        self.widget_with_layout.setLayout(self.layout3)

        # Layout'u içeren widget'i ve butonu ana layout'a ekle
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.widget_with_layout)
        main_layout.addWidget(self.button)

        self.setLayout(main_layout)

    def toggleLabelVisibility(self):
        # Layout'un görünürlüğünü değiştir
        self.widget_with_layout.setVisible(not self.widget_with_layout.isVisible())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

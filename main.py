import sys, os
 
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit, QMessageBox, QTableView, QFileDialog, QLabel
from PySide2.QtCore import QFile, QObject
from PySide2.QtGui import QPixmap

 
class Form(QObject):
 
    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
 
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
 
        self.line = self.window.findChild(QLineEdit, 'lineEdit')
        self.table = self.window.findChild(QTableView, 'tableView')
        self.label_1 = self.window.findChild(QLabel, 'label')
        btn = self.window.findChild(QPushButton, 'pushButton')
        btn.clicked.connect(self.ok_handler)
        self.window.show()
 
    def ok_handler(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getOpenFileName(None, 'Choose Image', '/home', 'Image Files (*.jpg *.png)', options=options)
        print(file_name[0])
        self.label_1.setPixmap(QPixmap(file_name[0]))
        # self.label_1.setMask(pixmap.mask())
        # print(file_name[0])
        # msgBox = QMessageBox()
        # msgBox.setWindowTitle('Mensaje!')
        # print(self.calc.calculo(self.line.text()))
        # msgBox.setText(self.calc.calculo(self.line.text()))
        # msgBox.exec_()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form('main.ui')
    sys.exit(app.exec_())


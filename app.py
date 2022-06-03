import sys
from PyQt5.QtWidgets import QApplication 

from gui import MyApp;



def main():
    return;

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main();
    ex = MyApp()
    sys.exit(app.exec_())


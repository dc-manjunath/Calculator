import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6.QtGui import QIcon
from UI.ui_calculator import Ui_MainWindow
from functools import partial
import sys
ERROR_MSG = "ERROR"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Calculator")

        self.display = self.ui.lineEdit

    def setDisplayText(self, text):
        """
        Set display text
        :param text:
        :return:
        """
        self.display.setText(text)
        self.display.setFocus()

    def setInit(self):
        self.display.setText("0")
        self.display.setFocus()

    def displayText(self):
        """
        Get display text
        :return: text
        """
        return self.display.text()

    def clearDisplay(self):
        """
        Clear display text
        :return:
        """
        self.display.clear()

class PyCalCtrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()

    def _calculateResult(self):
        """
        Calculate result and display
        :return:
        """
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """
        Build expression
        :param sub_exp:
        :return:
        """
        # Clear if displaying an error message
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        if self._view.displayText() == "0":
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        """
        Connect signals and slots
        :return:
        """
        # Iterate through all controls on the page to find specific types
        btn_list = self._view.findChildren(QPushButton)

        for btn in btn_list:
            if btn.text() not in {"=", "C"}:
                btn.clicked.connect(partial(self._buildExpression, btn.text()))
            elif btn.text() == "C":
                btn.clicked.connect(self._view.setInit)
            elif btn.text() == "=":
                btn.clicked.connect(self._calculateResult)

        self._view.display.returnPressed.connect(self._calculateResult)

def evaluateExpression(expression):
    try:
        # eval() evaluates the string as a Python expression
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowIcon("Calculator_icon.webp") # type: ignore
    window.show()

    PyCalCtrl(model=evaluateExpression, view=window)

    sys.exit(app.exec())

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Stylesheet')

        gridLayout = QGridLayout()

        gridLayout.addWidget(QLabel('background-color'), 0, 0)
        gridLayout.addWidget(QLabel('color'), 1, 0)
        gridLayout.addWidget(QLabel('border-color'), 2, 0)
        gridLayout.addWidget(QLabel('selection-color'), 3, 0)
        gridLayout.addWidget(QLabel('border-style'), 4, 0)
        gridLayout.addWidget(QLabel('border-width(px)'), 5, 0)
        gridLayout.addWidget(QLabel('border-radius(px)'), 6, 0)

        # user input widgets
        self.widgetBackgroundColor = QComboBox()
        self.widgetColor = QComboBox()
        self.widgetBorderColor = QComboBox()
        self.widgetSelectionColor = QComboBox()
        self.widgetBorderStyle = QComboBox()
        self.widgetBorderWidth = QSpinBox()
        self.widgetBorderRadius = QSpinBox()

        self.widgetBackgroundColor.setEditable(True)
        self.widgetColor.setEditable(True)
        self.widgetBorderColor.setEditable(True)
        self.widgetSelectionColor.setEditable(True)

        self.btnBackgroundColor = QPushButton('Color')
        self.btnColor = QPushButton('Color')
        self.btnBorderColor = QPushButton('Color')
        self.btnSelectionColor = QPushButton('Color')

        gridLayout.addWidget(self.widgetBackgroundColor, 0, 1)
        gridLayout.addWidget(self.btnBackgroundColor, 0, 2)
        gridLayout.addWidget(self.widgetColor, 1, 1)
        gridLayout.addWidget(self.btnColor, 1, 2)
        gridLayout.addWidget(self.widgetBorderColor, 2, 1)
        gridLayout.addWidget(self.btnBorderColor, 2, 2)
        gridLayout.addWidget(self.widgetSelectionColor, 3, 1)
        gridLayout.addWidget(self.btnSelectionColor, 3, 2)
        gridLayout.addWidget(self.widgetBorderStyle, 4, 1)
        gridLayout.addWidget(self.widgetBorderWidth, 5, 1)
        gridLayout.addWidget(self.widgetBorderRadius, 6, 1)

        styleGroup = QGroupBox()
        styleGroup.setTitle('Widget Style Sheet')
        styleGroup.setLayout(gridLayout)

        styleLayout = QHBoxLayout()
        styleLayout.addWidget(styleGroup)

        self.cmdButton = QPushButton('적용')
        self.targetItems = QComboBox()
        # target widgets
        self.theLabel = QLabel('레이블(Label)')
        self.thePushButton = QPushButton('버튼(Button)')
        self.theLineEdit = QLineEdit()
        self.theLineEdit.setPlaceholderText('입력 Hint')
        __TARGET_WIDGETS = ['Label', 'LineEdit', 'PushButton']
        self.targetItems.addItems(__TARGET_WIDGETS)

        cmdLayout = QHBoxLayout()
        cmdLayout.addWidget(QLabel('적용 대상 Widget'))
        cmdLayout.addWidget(self.targetItems)
        cmdLayout.addWidget(self.cmdButton)

        targetLayout = QGridLayout()
        self.logLabel = QTextEdit()
        self.logPushButton = QTextEdit()
        self.logLineEdit = QTextEdit()
        targetLayout.addWidget(self.theLabel, 0, 0)
        targetLayout.addWidget(self.logLabel, 1, 0)
        targetLayout.addWidget(self.theLineEdit, 0, 1)
        targetLayout.addWidget(self.logLineEdit, 1, 1)
        targetLayout.addWidget(self.thePushButton, 0, 2)
        targetLayout.addWidget(self.logPushButton, 1, 2)

        resultGroup = QGroupBox()
        resultGroup.setTitle('적용 결과')
        resultGroup.setLayout(targetLayout)
        resultLayout = QVBoxLayout()
        resultLayout.addWidget(resultGroup)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(styleLayout)
        mainLayout.addLayout(cmdLayout)
        mainLayout.addLayout(resultLayout)
        self.setLayout(mainLayout)

        self.initData()
        self.setSignals()

    def initData(self):
        # __COLORS = ['white', 'black', 'gray', 'green', 'red', 'yellow', \
        #             '#FA8072', '#87CEFA', '#1E90FF', \
        #             'rgb(255, 0, 0)', 'rgba(255, 0, 0, 75%)']
        __COLORS = QColor.colorNames()      # Predefined colors
        __BORDER_STYLES = ['none', 'dashed', 'dot-dash', 'dot-dot-dash', 'dotted', 'double', 'groove', \
                           'inset', 'outset', 'ridge', 'solid']
        __COLORS.sort()
        __BORDER_STYLES.sort()
        # fill the items
        self.widgetBackgroundColor.addItems(__COLORS)
        self.widgetColor.addItems(__COLORS)
        self.widgetBorderColor.addItems(__COLORS)
        self.widgetSelectionColor.addItems(__COLORS)
        self.widgetBorderStyle.addItems(__BORDER_STYLES)
        # set default value to widgets
        self.widgetBackgroundColor.setCurrentText('white')
        self.widgetColor.setCurrentText('black')
        self.widgetBorderColor.setCurrentText('black')
        self.widgetSelectionColor.setCurrentText('yellow')
        self.widgetBorderStyle.setCurrentText('none')
        self.widgetBorderWidth.setValue(1)
        self.widgetBorderRadius.setValue(1)
        # set default value to variables
        self.inputBackgroundColor = self.widgetBackgroundColor.currentText()
        self.inputColor = self.widgetColor.currentText()
        self.inputBorderColor = self.widgetBorderColor.currentText()
        self.inputSelectionColor = self.widgetSelectionColor.currentText()
        self.inputBorderStyle = self.widgetBorderStyle.currentText()
        self.inputBorderWidth = self.widgetBorderWidth.value()
        self.inputBorderRadius = self.widgetBorderRadius.value()

    def setSignals(self):
        self.cmdButton.clicked.connect(self.__setStyleSheet)
        self.widgetColor.currentIndexChanged.connect(self._changedColor)
        self.widgetBackgroundColor.currentIndexChanged.connect(self._changedBackgroundColor)
        self.widgetBorderColor.currentIndexChanged.connect(self._changedBorderColor)
        self.widgetSelectionColor.currentIndexChanged.connect(self._changedSelectionColor)
        self.widgetBorderStyle.currentIndexChanged.connect(self._changedBorderStyle)
        self.widgetBorderWidth.valueChanged.connect(self.__changedBorderWidth)
        self.widgetBorderRadius.valueChanged.connect(self.__changedBorderRadius)
        self.btnBackgroundColor.clicked.connect(self.showBackgroundColorDialog)
        self.btnColor.clicked.connect(self.showColorDialog)
        self.btnBorderColor.clicked.connect(self.showBorderColorDialog)
        self.btnSelectionColor.clicked.connect(self.showSelectionColorDialog)

    def showBackgroundColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.widgetBackgroundColor.insertItem(0, color.name())
            self.widgetBackgroundColor.setCurrentText(color.name())

    def showColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.widgetColor.insertItem(0, color.name())
            self.widgetColor.setCurrentText(color.name())

    def showBorderColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.widgetBorderColor.insertItem(0, color.name())
            self.widgetBorderColor.setCurrentText(color.name())

    def showSelectionColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.widgetSelectionColor.insertItem(0, color.name())
            self.widgetSelectionColor.setCurrentText(color.name())

    def _changedColor(self):
        self.inputColor = self.widgetColor.currentText()

    def _changedBackgroundColor(self):
        self.inputBackgroundColor = self.widgetBackgroundColor.currentText()

    def _changedBorderColor(self):
        self.inputBorderColor = self.widgetBorderColor.currentText()

    def _changedSelectionColor(self):
        self.inputSelectionColor = self.widgetSelectionColor.currentText()

    def _changedBorderStyle(self):
        self.inputBorderStyle = self.widgetBorderStyle.currentText()

    def __changedBorderWidth(self):
        self.inputBorderWidth = self.widgetBorderWidth.value()

    def __changedBorderRadius(self):
        self.inputBorderRadius = self.widgetBorderRadius.value()

    def __setStyleSheet(self):
        if self.targetItems.currentText() == 'Label':
            self.theLabel.setStyleSheet(f'background-color: {self.inputBackgroundColor};'
                                        f'color: {self.inputColor};'
                                        f'border-color: {self.inputBorderColor};'
                                        f'border-style: {self.inputBorderStyle};'
                                        f'border-width: {self.inputBorderWidth}px;'
                                        f'border-radius: {self.inputBorderRadius}px;')
            self.logLabel.clear()
            self.logLabel.setText(f'background-color: {self.inputBackgroundColor};\n'
                                        f'color: {self.inputColor};\n'
                                        f'border-color: {self.inputBorderColor};\n'
                                        f'border-style: {self.inputBorderStyle};\n'
                                        f'border-width: {self.inputBorderWidth}px;\n'
                                        f'border-radius: {self.inputBorderRadius}px;\n')
        if self.targetItems.currentText() == 'PushButton':
            self.thePushButton.setStyleSheet(f'background-color: {self.inputBackgroundColor};'
                                        f'color: {self.inputColor};'
                                        f'border-color: {self.inputBorderColor};'
                                        f'border-style: {self.inputBorderStyle};'
                                        f'border-width: {self.inputBorderWidth}px;'
                                        f'border-radius: {self.inputBorderRadius}px;')
            self.logPushButton.clear()
            self.logPushButton.setText(f'background-color: {self.inputBackgroundColor};\n'
                                        f'color: {self.inputColor};\n'
                                        f'border-color: {self.inputBorderColor};\n'
                                        f'border-style: {self.inputBorderStyle};\n'
                                        f'border-width: {self.inputBorderWidth}px;\n'
                                        f'border-radius: {self.inputBorderRadius}px;\n')
        if self.targetItems.currentText() == 'LineEdit':
            self.theLineEdit.setStyleSheet(f'background-color: {self.inputBackgroundColor};'
                                        f'color: {self.inputColor};'
                                        f'border-color: {self.inputBorderColor};'
                                        f'selection-color: {self.inputSelectionColor};'   
                                        f'border-style: {self.inputBorderStyle};'
                                        f'border-width: {self.inputBorderWidth}px;'
                                        f'border-radius: {self.inputBorderRadius}px;')
            self.logLineEdit.clear()
            self.logLineEdit.setText(f'background-color: {self.inputBackgroundColor};\n'
                                        f'color: {self.inputColor};\n'
                                        f'border-color: {self.inputBorderColor};\n'
                                        f'selection-color: {self.inputSelectionColor};\n'   
                                        f'border-style: {self.inputBorderStyle};\n'
                                        f'border-width: {self.inputBorderWidth}px;\n'
                                        f'border-radius: {self.inputBorderRadius}px;\n')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
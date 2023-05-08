import sys, keyboard, webbrowser, resources

from PyQt5.QtWidgets import (QMainWindow,
                             QApplication,
                             QPushButton,
                             QCheckBox,
                             QSpinBox,
                             QLabel,
                             QFileDialog,
                             QWidget)
from PyQt5.QtCore import (QPropertyAnimation,
                          QPoint,
                          QParallelAnimationGroup)
from PyQt5.QtGui import QIcon, QPixmap

from random import choices

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(":/icons/icon.png"), QIcon.Selected, QIcon.On)
        self.setWindowIcon(self.icon)
        self.setWindowTitle("Scrambler Password Generator")
        self.setStyleSheet("background-color: #202020")

        self.Style = """
            QPushButton {
                color: silver;
                font-size: 15px;
                border: 1px solid silver;
                border-radius: 10px;
            }
            QPushButton::hover {
                border: 1px solid white;
                color: white;
            }
            QPushButton::presseded {
                border: 1px solid silver;
                color: silver;
            }
            QPushButton#GitHubButton {
                color: #fff;
                background-color: #080B0F;
                font-size: 16px;
                font: bold;
                border-radius: 5px;
                border: none;
            }

            QPushButton#GitHubButton:hover {
                background-color: #12151A;
                font-size: 17px;
            }

            QPushButton#GitHubButton:presseded {
                background-color: #080B0F
            }
            QPushButton#TelegramButton {
                color: #fff;
                background-color: #208FFF;
                font-size: 18px;
                border-radius: 5px;
                border: none;
            }

            QPushButton#TelegramButton:hover {
                background-color: #46A0FC;
                font-size: 19px;
            }

            QPushButton#TelegramButton:presseded {
                background-color: #208FFF
            }
            QPushButton#CloseButton {
                color: #fff;
                font-size: 20px;
                border-radius: 10;
                border: none;
                background-color: #333232
            }
            QPushButton#CloseButton:hover {
                background-color: #191818
            }
            QCheckBox {
                    font-size: 30px;
                    color: silver;
                    spacing: 55px;
                    background-color: none;
            }
            QCheckBox::hover {
                    font-size: 30px;
                    color: white;
            }
            QSpinBox {
                color: white;
                font-size: 20px;
                border: none;
                background-color: #202020;
                border-radius: 2px;
            }
            QSpinBox::hover{
                background-color: #39393B;
            }
            QLabel {
                color: white;
                font-size: 20px;
                background-color: none;
            }
            QWidget#panel {
                background-color: #333232
            }

        """

        self.reset_setting = QPushButton('Сбросить', self)
        self.reset_setting.setStyleSheet(self.Style)
        self.reset_setting.adjustSize()
        self.reset_setting.setGeometry(75, 500, 250, 50)
        self.reset_setting.clicked.connect(self.reset)
        self.reset_setting.setToolTip('pressed: Ctrl+R')
        self.reset_setting.setShortcut('Ctrl+R')

        self.generate_password = QPushButton('Генерировать', self)
        self.generate_password.setStyleSheet(self.Style)
        self.generate_password.adjustSize()
        self.generate_password.setGeometry(75, 425, 250, 50)
        self.generate_password.clicked.connect(self.password_generator)
        self.generate_password.setToolTip('pressed: Ctrl+S')
        self.generate_password.setShortcut('Ctrl+S')

        self.open_menu = QPushButton('Меню', self)
        self.open_menu.setStyleSheet(self.Style)
        self.open_menu.adjustSize()
        self.open_menu.setGeometry(75, 575, 250, 50)
        self.open_menu.clicked.connect(self.PanelOpen)

        self.label_spinbox_count_password = QLabel('Количество паролей', self)
        self.label_spinbox_count_password.setStyleSheet(self.Style)
        self.label_spinbox_count_password.setGeometry(120, 30, 200, 30)

        self.count_password = QSpinBox(self)
        self.count_password.setStyleSheet(self.Style)
        self.count_password.setGeometry(50, 30, 50, 30)
        self.count_password.setMinimum(1)

        self.label_spinbox_len_password = QLabel('Длина пароля', self)
        self.label_spinbox_len_password.setStyleSheet(self.Style)
        self.label_spinbox_len_password.setGeometry(120, 100, 200, 30)

        self.len_password = QSpinBox(self)
        self.len_password.setStyleSheet(self.Style)
        self.len_password.setGeometry(50, 100, 50, 30)
        self.len_password.setMinimum(1)

        self.checkbox_options_numbers = QCheckBox('Цифры', self)
        self.checkbox_options_numbers.setStyleSheet(self.Style)
        self.checkbox_options_numbers.setGeometry(50, 150, 200, 50)
        self.checkbox_options_numbers.setToolTip("1234567890")

        self.checkbox_options_letters = QCheckBox('Буквы', self)
        self.checkbox_options_letters.setStyleSheet(self.Style)
        self.checkbox_options_letters.setGeometry(50, 200, 200, 50)
        self.checkbox_options_letters.setToolTip("qwertyuiopasdfghjklzxcvbnm")

        self.checkbox_options_symbols = QCheckBox('Символы', self)
        self.checkbox_options_symbols.setStyleSheet(self.Style)
        self.checkbox_options_symbols.setGeometry(50, 250, 200, 50)
        self.checkbox_options_symbols.setToolTip("~!@#$%^&*()_+}{|\\/?>-<")


        self.panel_menu = QWidget(self)
        self.panel_menu.setObjectName('panel')
        self.panel_menu.setStyleSheet(self.Style)
        self.panel_menu.setGeometry(-300, 0, 250, 650)

        self.TelegramButton = QPushButton("Telegram", self)
        self.TelegramButton.setObjectName("TelegramButton")
        self.TelegramButton.setStyleSheet(self.Style)
        self.TelegramButton.setGeometry(-300, 100, 200, 30)
        self.TelegramButton.clicked.connect(self.openTelegramWebBrowser)

        self.GitHubButton = QPushButton("GitHub", self)
        self.GitHubButton.setObjectName("GitHubButton")
        self.GitHubButton.setStyleSheet(self.Style)
        self.GitHubButton.setGeometry(-300, 150, 200, 30)
        self.GitHubButton.clicked.connect(self.openGitHubWebBrowser)

        self.checkbox_options_language = QCheckBox('RU', self)
        self.checkbox_options_language.setObjectName('language')
        self.checkbox_options_language.setStyleSheet(self.Style)
        self.checkbox_options_language.setGeometry(-300, 200, 300, 50)
        self.checkbox_options_language.setChecked(True)
        self.checkbox_options_language.stateChanged.connect(self.language_interface)
        self.checkbox_options_language.setToolTip("Language Interface")

        self.information_interface = QLabel("""
            HOTKEY

Pressed - I (hide)

Pressed - Esc (close)

Pressed - Ctrl+S (save)

Pressed - Ctrl+R (reset)
        """, self)
        self.information_interface.setStyleSheet(self.Style)
        self.information_interface.setGeometry(-300, 300, 220, 250)

        self.CloseButton = QPushButton("✕", self)
        self.CloseButton.setObjectName("CloseButton")
        self.CloseButton.setStyleSheet(self.Style)
        self.CloseButton.setGeometry(-300, 20, 30, 30)
        self.CloseButton.clicked.connect(self.PanelClose)

        self.anim_group = QParallelAnimationGroup()
        self.AnimationPanel = QPropertyAnimation(self.panel_menu, b"pos")
        self.AnimationTelegramButton = QPropertyAnimation(self.TelegramButton, b"pos")
        self.AnimationGitHubButton = QPropertyAnimation(self.GitHubButton, b"pos")
        self.AnimationCheckBoxLanguage = QPropertyAnimation(self.checkbox_options_language, b"pos")
        self.AnimationInformationHotkey = QPropertyAnimation(self.information_interface, b"pos")
        self.AnimationCloseButton = QPropertyAnimation(self.CloseButton, b"pos")

        keyboard.add_hotkey('i', lambda: self.checl_hide_program())
        keyboard.add_hotkey('esc', lambda: sys.exit(QApplication.exit()))

    def checl_hide_program(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()

    def language_interface(self):
        if self.checkbox_options_language.isChecked():
            self.reset_setting.setText("Сбросить")
            self.generate_password.setText("Генерировать")
            self.open_menu.setText("Меню")
            self.label_spinbox_count_password.setText("Количество паролей")
            self.label_spinbox_len_password.setText("Длина пароля")
            self.checkbox_options_numbers.setText("Цифры")
            self.checkbox_options_letters.setText("Буквы")
            self.checkbox_options_symbols.setText("Символы")
        else:
            self.reset_setting.setText("Reset")
            self.generate_password.setText("Generator")
            self.open_menu.setText("Menu")
            self.label_spinbox_count_password.setText("Number of password")
            self.label_spinbox_len_password.setText("Length password")
            self.checkbox_options_numbers.setText("Numbers")
            self.checkbox_options_letters.setText("Letters")
            self.checkbox_options_symbols.setText("Symbols")


    def PanelOpen(self):
        self.AnimationPanel.setEndValue(QPoint(0, 0))  # Geometry Animation PanelOpen
        self.AnimationPanel.setDuration(200)

        self.AnimationTelegramButton.setEndValue(QPoint(25, 100))
        self.AnimationTelegramButton.setDuration(200)

        self.AnimationGitHubButton.setEndValue(QPoint(25, 150))
        self.AnimationGitHubButton.setDuration(200)

        self.AnimationCheckBoxLanguage.setEndValue(QPoint(25, 200))
        self.AnimationCheckBoxLanguage.setDuration(200)

        self.AnimationInformationHotkey.setEndValue(QPoint(25, 300))
        self.AnimationInformationHotkey.setDuration(200)

        self.AnimationCloseButton.setEndValue(QPoint(205, 20))
        self.AnimationCloseButton.setDuration(180)

        self.reset_setting.setEnabled(False)
        self.generate_password.setEnabled(False)
        self.open_menu.setEnabled(False)
        self.count_password.setEnabled(False)
        self.checkbox_options_numbers.setEnabled(False)
        self.checkbox_options_letters.setEnabled(False)
        self.checkbox_options_symbols.setEnabled(False)

        self.start_animation()

    def PanelClose(self):
        self.AnimationPanel.setEndValue(QPoint(-300, 0))  # Geometry Animation PanelOpen
        self.AnimationPanel.setDuration(200)

        self.AnimationTelegramButton.setEndValue(QPoint(-300, 100))
        self.AnimationTelegramButton.setDuration(200)

        self.AnimationGitHubButton.setEndValue(QPoint(-300, 150))
        self.AnimationGitHubButton.setDuration(200)

        self.AnimationCheckBoxLanguage.setEndValue(QPoint(-300, 200))
        self.AnimationCheckBoxLanguage.setDuration(180)

        self.AnimationInformationHotkey.setEndValue(QPoint(-300, 300))
        self.AnimationInformationHotkey.setDuration(200)

        self.AnimationCloseButton.setEndValue(QPoint(-300, 30))
        self.AnimationCloseButton.setDuration(180)

        self.reset_setting.setEnabled(True)
        self.generate_password.setEnabled(True)
        self.open_menu.setEnabled(True)
        self.count_password.setEnabled(True)
        self.checkbox_options_numbers.setEnabled(True)
        self.checkbox_options_letters.setEnabled(True)
        self.checkbox_options_symbols.setEnabled(True)

        self.start_animation()

    def start_animation(self):
        self.anim_group.addAnimation(self.AnimationPanel)
        self.anim_group.addAnimation(self.AnimationTelegramButton)
        self.anim_group.addAnimation(self.AnimationGitHubButton)
        self.anim_group.addAnimation(self.AnimationCheckBoxLanguage)
        self.anim_group.addAnimation(self.AnimationInformationHotkey)
        self.anim_group.addAnimation(self.AnimationCloseButton)
        self.anim_group.start()

    def openTelegramWebBrowser(self):
        webbrowser.open('https://t.me/ProgramsCreator/')

    def openGitHubWebBrowser(self):
        webbrowser.open('https://github.com/Shedrjoinzz')


    def reset(self):
        self.count_password.setValue(0)
        self.len_password.setValue(0)
        self.checkbox_options_numbers.setChecked(False)
        self.checkbox_options_letters.setChecked(False)
        self.checkbox_options_symbols.setChecked(False)

    def password_generator(self):
        DIGIT = '1234567890'
        ALPHA_LOWER = 'qwertyuiopasdfghjklzxcvbnm'
        ALPHA_UPPER = ALPHA_LOWER.upper()
        SYMBOL = '~!@#$%^&*()_+}{"|\\/?><-'
        line = ''

        password_list = []

        if self.checkbox_options_numbers.isChecked():
            line += DIGIT

        if self.checkbox_options_letters.isChecked():
            line += ALPHA_LOWER + ALPHA_UPPER


        if self.checkbox_options_symbols.isChecked():
            line += SYMBOL

        if self.checkbox_options_numbers.isChecked() == False and self.checkbox_options_letters.isChecked() == False and self.checkbox_options_symbols.isChecked() == False:
            line += DIGIT
            line += ALPHA_LOWER + ALPHA_UPPER
            line += SYMBOL

        for i in range(self.count_password.value()):
            password_list.append(''.join(choices(line, k=self.len_password.value())))

        filename = QFileDialog.getSaveFileName(self, 'Сохранить', '/password.txt')
        count_line = 1

        try:
            with open(filename[0], 'w') as file_passowrds:
                for i in password_list:
                    file_passowrds.write(f"{count_line})    {i}" )
                    file_passowrds.write('\n')
                    count_line+=1
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(400, 650)
    window.show()
    sys.exit(app.exec_())

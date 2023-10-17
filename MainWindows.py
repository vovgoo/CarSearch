from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
import cv2
import imutils
from PySide6 import QtGui
from main import main
from scripts.send_email import main_streep
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMessageBox)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/newPrefix/\u0411\u0435\u0437 \u0438\u043c\u0435\u043d\u0438-2.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: #262f34;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setStyleSheet(u"background-color: #20282b;\n"
"color:  #20282b;\n"
"")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        self.label_9.setMaximumSize(QSize(120, 120))
        self.label_9.setStyleSheet(u"background-color: #20282b;\n"
"color: white;\n"
"padding: 20px;\n"
"\n"
"")
        self.label_9.setPixmap(QPixmap(u":/newPrefix/\u0411\u0435\u0437 \u0438\u043c\u0435\u043d\u0438-1.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setMargin(0)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Icon.Information)
        self.msgBox.setWindowIcon(QPixmap(u":/newPrefix/\u0411\u0435\u0437 \u0438\u043c\u0435\u043d\u0438-2.png"))
        self.msgBox.setWindowTitle("Ошибка")
        self.msgBox.setText("Автомобиль не распознан. Попробуйте распознать автомообиль и повторите попытку.")

        self.msgBox1 = QMessageBox()
        self.msgBox1.setIcon(QMessageBox.Icon.Information)
        self.msgBox1.setWindowIcon(QPixmap(u":/newPrefix/\u0411\u0435\u0437 \u0438\u043c\u0435\u043d\u0438-2.png"))
        self.msgBox1.setWindowTitle("Ошибка")
        self.msgBox1.setText("Ошибка загрузки фотографии, убедитесь что фотография нужного разрешения и в формате PNG.")

        self.msgBox2 = QMessageBox()
        self.msgBox2.setIcon(QMessageBox.Icon.Information)
        self.msgBox2.setWindowIcon(QPixmap(u":/newPrefix/\u0411\u0435\u0437 \u0438\u043c\u0435\u043d\u0438-2.png"))
        self.msgBox2.setWindowTitle("Ошибка")
        self.msgBox2.setText("Не удалось распознать фотографию. Убедитесь что есть подключение к интернету, либо отправьте снимок более хорошего разрешения.")

        self.msgBox3 = QMessageBox()
        self.msgBox3.setIcon(QMessageBox.Icon.Information)
        self.msgBox3.setWindowIcon(QPixmap(u":/newPrefix/\u0411\u0435\u0437 \u0438\u043c\u0435\u043d\u0438-2.png"))
        self.msgBox3.setWindowTitle("Ошибка")
        self.msgBox3.setText(
            "Что бы начать процесс распознавания, загрузите фотографию для поиска.")

        self.msgBox4 = QMessageBox()
        self.msgBox4.setIcon(QMessageBox.Icon.Information)
        self.msgBox4.setWindowIcon(QPixmap(u":/newPrefix/\u0411\u0435\u0437 \u0438\u043c\u0435\u043d\u0438-2.png"))
        self.msgBox4.setWindowTitle("Ошибка")
        self.msgBox4.setText(
            "Ошибка сохранения. Возможно этот файл уже где то открыт или используется.")

        self.msgBox5 = QMessageBox()
        self.msgBox5.setIcon(QMessageBox.Icon.Information)
        self.msgBox5.setWindowIcon(QPixmap(u":/newPrefix/\u0411\u0435\u0437 \u0438\u043c\u0435\u043d\u0438-2.png"))
        self.msgBox5.setWindowTitle("Успешно")
        self.msgBox5.setText(
            "Файл успешно сохранен.")


        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Nexa Text Demo"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: #20282b;\n"
"color: white;\n"
"")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setMargin(0)

        self.horizontalLayout_5.addWidget(self.label)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"background-color: #20282b;\n"
"color: white;\n"
"padding-right: auto;\n"
"")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)
        self.label_2.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Nexa Text Demo"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(10)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: white;\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setMargin(10)

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Nexa Text Demo"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color: white;\n"
"border-color: #F34A4A;\n"
"background-color: #20282b;\n"
"margin: 10px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setMargin(0)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border-style: solid;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: #F34A4A;\n"
"background-color: #20282b;")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(142, 50, 251, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"border-style: outset;\n"
"border-width: 0px;\n"
"color: white;\n"
"\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(87, 120, 361, 31))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"border-style: outset;\n"
"border-width: 0px;\n"
"color: white;\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(142, 210, 251, 31))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"border-style: outset;\n"
"border-width: 0px;\n"
"color: white;\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(87, 280, 361, 31))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"border-style: outset;\n"
"border-width: 0px;\n"
"color: white;\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.widget)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, -1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.loadImage)
        font3 = QFont()
        font3.setFamilies([u"Nexa Text Demo"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(False)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: #F34A4A;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"padding: 6px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: #C41E32;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font4 = QFont()
        font4.setFamilies([u"Nexa Text Demo"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-color: #F34A4A;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"padding: 6px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: #C41E32;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font4)
        self.pushButton_3.clicked.connect(self.send_email)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-color: #F34A4A;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"padding: 6px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: #C41E32;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.clicked.connect(self.save_file)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background-color: #F34A4A;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"padding: 6px;\n"
"color: white;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"   background-color: #C41E32;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        self.filename = None
        self.save_filename = None
        self.tmp = None


    def loadImage(self):
        try:
            self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
            self.image = cv2.imread(self.filename)
            self.SetPhoto(self.image)
        except:
            self.label_3.setText("Не удалось загрузить фотографию.")

    def SetPhoto(self, image):
        try:
            self.tmp = image
            image = imutils.resize(image, width=400)
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
            self.label_3.setPixmap(QtGui.QPixmap.fromImage(image))
            self.label_6.setText("Отсутствует")
            self.label_8.setText("Отсутствует")
        except:
            self.label_3.setText("Не удалось загрузить фотографию.")
            self.msgBox1.exec()


    def search(self):
        if self.label_3.text() == "Загрузите изображение" or self.label_3.text() == "Не удалось загрузить фотографию.":
            self.msgBox3.exec()
        else:
            self.temp = main(self.filename)
            if self.temp != None:
                self.label_6.setText(self.temp[0])
                self.label_8.setText(self.temp[1])
            else:
                self.label_6.setText("Не распознан")
                self.label_8.setText("Не распознан")
                self.msgBox2.exec()

    def send_email(self):
        if self.label_6.text() == "Не распознан" and self.label_8.text() == "Не распознан":
            self.msgBox.exec()
        elif self.label_6.text() == "Отсутствует" and self.label_8.text() == "Отсутствует":
            self.msgBox.exec()
        else:
            text = f"Номер авто: {self.label_6.text()}\nНазвание авто:{self.label_8.text()}\n\nИнформацию которую удалось найти про этот атвомобиль в Google:\n{self.temp[2]}\n{self.temp[3]}\n{self.temp[4]}\n{self.temp[5]}\n{self.temp[6]}\n"
            main_streep(text)

    def save_file(self):
        if self.label_6.text() == "Не распознан" and self.label_8.text() == "Не распознан":
            self.msgBox.exec()
        elif self.label_6.text() == "Отсутствует" and self.label_8.text() == "Отсутствует":
            self.msgBox.exec()
        else:
            try:
                self.save_filename = QFileDialog.getSaveFileName(filter="txt files (*.txt)")[0]
                with open(self.save_filename, "w", encoding="utf-8") as f:
                    text = f"Номер авто: {self.label_6.text()}\nНазвание авто:{self.label_8.text()}\n\nИнформацию которую удалось найти про этот атвомобиль в Google:\n{self.temp[2]}\n{self.temp[3]}\n{self.temp[4]}\n{self.temp[5]}\n{self.temp[6]}\n"
                    f.write(text)
                self.msgBox5.exec()
            except:
                self.msgBox4.exec()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CarInfo | \u0420\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0435\u0439", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"CarInfo", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0438\u0435 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u0435\u0439", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Загрузите изображение", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0430\u0432\u0442\u043e\u043c\u043e\u0431\u0438\u043b\u044f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi


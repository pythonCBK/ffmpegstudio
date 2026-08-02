import sys
import random

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QThread

from converter import Worker


# -----------------------------
# Переменные
# -----------------------------

FilesList = []

splashes = [
    "ERROR! Just kidding lol",
    "Psst! A python here somewhere..",
    "Here be dragons.",
    "100% code. Zero polyester!",
    "Beep boop",
    "Hi :3",
    "Hello world!",
    "cbk was here <3",
    "You there?",
    "Great argument.. but! Blah blah blah bu bu bu :3"]



                                # ----------------------------- #
                                #      Оконо "О программе"      #
                                # ----------------------------- # 


from ui_about import Ui_AboutWindow
class AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)




                                # ----------------------------- #
                                #           Осн. окно           #
                                # ----------------------------- # 


from ui_main import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # -----------------------------
        # При запуске программы.
        # ----------------------------- 

        # Смена сплэша
        self.ui.txtStatus.setText(random.choice(splashes))

        # Установка ограниченний на ввод                                                    #???
        self.ui.entryW.setValidator(QIntValidator(1, 16384))
        self.ui.entryH.setValidator(QIntValidator(1, 16384))

        self.ui.entryBitrate.setValidator(QIntValidator(1, 1000000))
        self.ui.entryFPS.setValidator(QIntValidator(1, 1000000))
    


        # -----------------------------
        # Привязка команд       
        # -----------------------------

        # Чекбоксы
        # ----------------
        self.ui.KeepOriginal.stateChanged.connect(self.KeepOriginalStatus)              # KeepOriginal
        self.ui.CropTheVideo.stateChanged.connect(self.CropTheVideoStatus)              # CropTheVideo

        # Выпадающее меню
        # ---------------- 
        self.ui.BoxResolutions.currentTextChanged.connect(self.resolution_changed)      # BoxResolutions
        self.ui.BoxFPS.currentTextChanged.connect(self.fps_changed)                     # BoxFPS
        self.ui.BoxBitrate.currentTextChanged.connect(self.Bitrate_changed)             # BoxBitrate
        self.ui.BoxSound.currentTextChanged.connect(self.Sound_changed)                 # BoxSound

        # Кнопки
        # ---------------- 
        self.ui.btnAddFiles.clicked.connect(self.addfiles)                              # btnAddFiles
        self.ui.btnClearList.clicked.connect(self.clearlist)                            # btnClearList
        self.ui.btnBrowse.clicked.connect(self.outPath)                                 # btnBrowse
        self.ui.btnConvert.clicked.connect(self.convert)                                # btnConvert
        self.ui.btnAbout.clicked.connect(self.open_about)                               # btnAbout



    # <<     --------------------------     >> #
    # <<              Команды               >> #
    # <<     --------------------------     >> #

    # Обновление статус-бара
    def set_status(self, text, color='#ffffff'):
            self.ui.txtStatus.setStyleSheet(f"color: {color};")
            self.ui.txtStatus.setText(text)

                # ---------------- #
                #     Чекбоксы     #
                # ---------------- #

    # KeepOriginal
    def KeepOriginalStatus(self, state):

        group_properties = [
            self.ui.BoxResolutions,
            self.ui.entryW,
            self.ui.entryH,
            self.ui.BoxFPS,
            self.ui.entryFPS,
            self.ui.BoxBitrate,
            self.ui.entryBitrate]

        enabled = not self.ui.KeepOriginal.isChecked()
        for obj in group_properties:
            obj.setEnabled(enabled)


    # CropTheVideo
    def CropTheVideoStatus(self, state):

        group_crop = [
            self.ui.timeStart,
            self.ui.timeEnd]

        enabled = self.ui.CropTheVideo.isChecked()
        for obj in group_crop:
            obj.setEnabled(enabled)   




                # ----------------- #
                #  Выпадающее меню  #
                # ----------------- # 

    #  Разрешение
    # ------------
    def readonlyRES(self):
        self.ui.entryW.setReadOnly(True)
        self.ui.entryH.setReadOnly(True)
    
    def resolution_changed(self, text):                                 #Opt

        if text == '4K':
            self.ui.entryW.setText('4096')
            self.ui.entryH.setText('2160')
            self.readonlyRES()

        elif text == 'UHD':
            self.ui.entryW.setText('3840')
            self.ui.entryH.setText('2160')
            self.readonlyRES()

        elif text == 'Quad HD':
            self.ui.entryW.setText('2560')
            self.ui.entryH.setText('1440')
            self.readonlyRES()

        elif text == '2K':
            self.ui.entryW.setText('2048')
            self.ui.entryH.setText('1080')
            self.readonlyRES()

        elif text == 'Full HD':
            self.ui.entryW.setText('1920')
            self.ui.entryH.setText('1080')
            self.readonlyRES()

        elif text == 'HD':
            self.ui.entryW.setText('1280')
            self.ui.entryH.setText('720')
            self.readonlyRES()

        elif text == 'SVGA':
            self.ui.entryW.setText('800')
            self.ui.entryH.setText('600')
            self.readonlyRES()

        elif text == 'VGA':
            self.ui.entryW.setText('640')
            self.ui.entryH.setText('480')
            self.readonlyRES()

        else:
            self.ui.entryW.setText('')
            self.ui.entryH.setText('')
            
            self.ui.entryW.setReadOnly(False)
            self.ui.entryH.setReadOnly(False)


    #     FPS
    # ------------
    def readonlyFPS(self):
        self.ui.entryFPS.setReadOnly(True)
    
    def fps_changed(self, text):                                        #Opt!

        if text == 'Custom':
            self.ui.entryFPS.setText('')
            self.ui.entryFPS.setReadOnly(False)

        else:
            self.ui.entryFPS.setText(text)
            self.readonlyFPS()


    #   Битрейт
    # ------------
    def readonlyBIT(self):
        self.ui.entryBitrate.setReadOnly(True)
    
    def Bitrate_changed(self, text):

        if text == 'Custom':
            self.ui.entryBitrate.setText('')
            self.ui.entryBitrate.setReadOnly(False)

        else:
            self.ui.entryBitrate.setText(text.replace(" kbps", ""))
            self.readonlyBIT()


    #    Звук
    # ------------
    def readonlySOUND(self):
        self.ui.entrySound.setReadOnly(True)
    
    def Sound_changed(self, text):

        if text == 'Custom':
            self.ui.entrySound.setText('')
            self.ui.entrySound.setReadOnly(False)

        else:
            self.ui.entrySound.setText(text.replace(" kbps", ""))
            self.readonlySOUND()




                # ----------------- #
                #       Кнопки      #
                # ----------------- # 

    #  Выбор файлов
    # ----------------
    def addfiles(self):
        files, _ = QFileDialog.getOpenFileNames(
        self,
        "Выберите файл",
        "",
        "Video files (*.mp4 *.mkv *.avi *.mov *.webm)")

        if files:

            # Добавить выбранные файлы в интерфейсе.
            self.ui.listFiles.clear() # Очистить от старых.
            self.ui.listFiles.addItems(files) # Добавить новые.

            # Добавить файлы в глоб. список.
            global FilesList
            FilesList.clear()
            for file in files:
                FilesList.append(file)

            # Обновить счётчик выбранных файлов.
            count = 0
            for n in files:
                count += 1

            self.ui.FileCount.setText(f'{count} files')
        

    #  Очистить список
    # -----------------
    def clearlist(self):
        self.ui.listFiles.clear()
        self.ui.FileCount.setText('0 files')


        global FilesList
        FilesList.clear()


    #  Выбор папки сохранения
    # ------------------------
    def outPath(self):
        path = QFileDialog.getExistingDirectory(self, "Выберите папку сохранения")

        self.ui.entryPath.setText(path)


    #  Окно "О программе"
    # --------------------
    def open_about(self):
            self.about_window = AboutWindow()
            self.about_window.show()


    #  Вызов конвертации
    # --------------------
    def convert(self):

        self.set_status('In process...', "#FFFFFF")

                        #   Переменные   #
                        # -------------- #

        # Время начала и конца обрезки.
        cropSTART = self.ui.timeStart.time().toString("HH:mm:ss")
        cropEND = self.ui.timeEnd.time().toString("HH:mm:ss")

        # Разрешение видео.
        width = self.ui.entryW.text().strip()
        height = self.ui.entryH.text().strip()

        # FPS видео.
        fps = self.ui.entryFPS.text().strip()

        # Битрейт видео.
        bitrate = self.ui.entryBitrate.text().strip()

        # Качество звука.
        sound = self.ui.entrySound.text().strip()

        # Новое разрешение файла.
        selected_format = self.ui.BoxFormats.currentText().lower()

        # Новое название выходного файла.
        outputname = self.ui.entryName.text().strip()

        # Путь сохранения выходных файлов
        outputpath = self.ui.entryPath.text().strip()


        # Обрезать ли видео
        if self.ui.CropTheVideo.isChecked():
            docrop = True
        else:
            docrop = False

        # Сохранять ли настройки
        if not self.ui.KeepOriginal.isChecked():
            keeporiginal = True
        else:
            keeporiginal = False

        data = [FilesList,
                cropSTART, cropEND,
                width, height,
                fps,
                bitrate,
                sound,
                selected_format,
                outputname,
                outputpath,
                docrop,
                keeporiginal
                ]


                    #  Создание и вызов потока  #
                    # ------------------------- #
        
        # Создаём поток
        self.thread = QThread()

        # Создаем объект Worker, который будет выполнять работу.
        self.worker = Worker(data) # <--- Передаём данные

        # Перемещаем Worker в другой поток отдельный от потока UI. Теперь Worker принадлежит другому потоку.
        self.worker.moveToThread(self.thread)

        # При запуске потока автоматически начинается выполнение Worker.run().
        self.thread.started.connect(self.worker.run)

        # После окончания работы вызвать:
        self.worker.finished.connect(self.show_result) # При завершении.
        self.worker.error.connect(self.show_error) # При ошибке.

        # Когда работа закончена завершить поток.
        self.worker.finished.connect(self.thread.quit)
        self.worker.error.connect(self.thread.quit)

        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.worker.deleteLater)

        # Запускаем поток. После запуска автоматически сработает сигнал started.
        self.thread.start()


    # Обновление статуса после выполнения задачи.
    def show_result(self, text, color):
        self.set_status(text, color)

    # Обновление статуса при ошибке.
    def show_error(self, text, color):
        self.set_status(text, color)





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
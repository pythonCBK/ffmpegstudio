import sys
import random
import subprocess
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIntValidator
import resources_rc



#   -=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####
#   Переменные   =-=-=-=-=-=-=-=-=-=-=-= #####
#   -=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####

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





# Окно "о программе"
from ui_about import Ui_AboutWindow
class AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)




# Основное окно
from ui_main import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #   -=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####
        #   При запуске   =-=-=-=-=-=-=-=-=-=-=-= #####
        #   -=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####

        # Смена сплэша
        self.ui.txtStatus.setText(random.choice(splashes))

        # Установка ограниченний на ввод
        self.ui.entryW.setValidator(QIntValidator(1, 16384))
        self.ui.entryH.setValidator(QIntValidator(1, 16384))

        self.ui.entryBitrate.setValidator(QIntValidator(1, 1000000))
        self.ui.entryFPS.setValidator(QIntValidator(1, 1000000))
    


        #   -=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####
        #   Инициализация кнопок    =-=-=-=-=-=-=-=-=-=-=-= #####
        #   -=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####


        # KeepOriginal - Checkbox
        self.ui.KeepOriginal.stateChanged.connect(self.KeepOriginalStatus)

        # CropTheVideo - Checkbox
        self.ui.CropTheVideo.stateChanged.connect(self.CropTheVideoStatus)


        # BoxResolutions - ComboBox
        self.ui.BoxResolutions.currentTextChanged.connect(self.resolution_changed)

        # BoxFPS - ComboBox
        self.ui.BoxFPS.currentTextChanged.connect(self.fps_changed)

        # BoxBitrate - ComboBox
        self.ui.BoxBitrate.currentTextChanged.connect(self.Bitrate_changed)

        # BoxSound - ComboBox
        self.ui.BoxSound.currentTextChanged.connect(self.Sound_changed)


        # btnAddFiles - Button
        self.ui.btnAddFiles.clicked.connect(self.addfiles)

        # btnClearList - Button
        self.ui.btnClearList.clicked.connect(self.clearlist)

        # btnBrowse - Button
        self.ui.btnBrowse.clicked.connect(self.outPath)

        # btnConvert - Button
        self.ui.btnConvert.clicked.connect(self.convert)

        # btnAbout - Button
        self.ui.btnAbout.clicked.connect(self.open_about)













    ##### =-=-=-=-=-=-=-=-=-=-=-=  -=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####
   ##### =-=-=-=-=-=-=-=-=-=-=-=    Чекбоксы    =-=-=-=-=-=-=-=-=-=-=-= #####
    ##### =-=-=-=-=-=-=-=-=-=-=-=  -=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####

    # KeepOriginal - Checkbox
    def KeepOriginalStatus(self, state):

        group_properties = [
            self.ui.BoxResolutions,
            self.ui.entryW,
            self.ui.entryH,
            self.ui.BoxFPS,
            self.ui.entryFPS,
            self.ui.BoxBitrate,
            self.ui.entryBitrate
        ]

        enabled = not self.ui.KeepOriginal.isChecked()

        for obj in group_properties:
            obj.setEnabled(enabled)


    # CropTheVideo - Checkbox
    def CropTheVideoStatus(self, state):

        group_crop = [
            self.ui.timeStart,
            self.ui.timeEnd
        ]

        enabled = self.ui.CropTheVideo.isChecked()

        for obj in group_crop:
            obj.setEnabled(enabled)   











    

    ##### =-=-=-=-=-=-=-=-=-=-=-=  -=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####
   ##### =-=-=-=-=-=-=-=-=-=-=-=   Комбобоксы   =-=-=-=-=-=-=-=-=-=-=-= #####
    ##### =-=-=-=-=-=-=-=-=-=-=-=  -=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####

    # BoxResolutions - ComboBox

    def readonlyRES(self):
        self.ui.entryW.setReadOnly(True)
        self.ui.entryH.setReadOnly(True)
    
    def resolution_changed(self, text):

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


    # BoxFPS - ComboBox
    def readonlyFPS(self):
        self.ui.entryFPS.setReadOnly(True)
    
    def fps_changed(self, text):

        if text == '120':
            self.ui.entryFPS.setText('120')
            self.readonlyFPS()

        elif text == '60':
            self.ui.entryFPS.setText('60')
            self.readonlyFPS()

        elif text == '30':
            self.ui.entryFPS.setText('30')
            self.readonlyFPS()

        else:
            self.ui.entryFPS.setText('')
            
            self.ui.entryFPS.setReadOnly(False)


    # BoxBitrate - ComboBox
    def readonlyBIT(self):
        self.ui.entryBitrate.setReadOnly(True)
    
    def Bitrate_changed(self, text):

        if text == 'Custom':
            self.ui.entryBitrate.setText('')
            self.ui.entryBitrate.setReadOnly(False)

        else:
            self.ui.entryBitrate.setText(text.replace(" kbps", ""))
            self.readonlyBIT()


    # BoxSound - ComboBox
    def readonlySOUND(self):
        self.ui.entrySound.setReadOnly(True)
    
    def Sound_changed(self, text):

        if text == 'Custom':
            self.ui.entrySound.setText('')
            self.ui.entrySound.setReadOnly(False)

        else:
            self.ui.entrySound.setText(text.replace(" kbps", ""))
            self.readonlySOUND()

















    ##### =-=-=-=-=-=-=-=-=-=-=-=  =-=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####
   ##### =-=-=-=-=-=-=-=-=-=-=-=     Кнопки      =-=-=-=-=-=-=-=-=-=-=-= #####
    ##### =-=-=-=-=-=-=-=-=-=-=-=  =-=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####


        # btnAddFiles - Button
    def addfiles(self):
        files, _ = QFileDialog.getOpenFileNames(
        self,
        "Выберите файл",
        "",
        "Video files (*.mp4 *.mkv *.avi *.mov *.webm)")

        if files:

            # add to ui
            self.ui.listFiles.clear() # <--- очистить от старых
            self.ui.listFiles.addItems(files)

            # add to list
            global FilesList
            FilesList.clear()

            for file in files:
                FilesList.append(file)

            # update text
            count = 0
            for n in files:
                count += 1

            self.ui.FileCount.setText(f'{count} files')
        

        # btnClearList - Button
    def clearlist(self):
        self.ui.listFiles.clear()
        self.ui.FileCount.setText('0 files')


        global FilesList
        FilesList.clear()


        # btnBrowse - Button
    def outPath(self):
        path = QFileDialog.getExistingDirectory(self, "Выберите папку сохранения")

        self.ui.entryPath.setText(path)



        # btnAbout - Button
    def open_about(self):
            self.about_window = AboutWindow()
            self.about_window.show()






    def set_status(self, text, color='#ffffff'):
            self.ui.txtStatus.setStyleSheet(f"color: {color};")
            self.ui.txtStatus.setText(text)













    ##### =-=-=-=-=-=-=-=-=-=-=-=  =-=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####
   ##### =-=-=-=-=-=-=-=-=-=-=-=   Конвертация   =-=-=-=-=-=-=-=-=-=-=-= #####
    ##### =-=-=-=-=-=-=-=-=-=-=-=  =-=-=-=-=-=  =-=-=-=-=-=-=-=-=-=-=-= #####

    def convert(self):

        ##### ============ Переменные ============ #####        

        # Время старта и конца обрезки.
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





        ##### ============ Процесс конвертации файлов ============ #####


        # Проверка наличия FFmpeg и его работы.
        try:
            ffmpegcheck = subprocess.run(["ffmpeg", "-version"],
                            capture_output=True, text=True,
                            creationflags=subprocess.CREATE_NO_WINDOW)
            
        except FileNotFoundError:
            self.set_status('Looks like there is no FFmpeg on your device. Download it from the official website.', '#f63333')
            return

        if ffmpegcheck.returncode != 0:
            self.set_status('FFmpeg was found but returned an error. Try to reinstall it from the official website.', '#f63333')
            return


        # Проверка выбраны ли файлы.
        if not FilesList:
            self.set_status('No files Selected!', '#f6b233')
            return



        ### === Проверка пути соранения === ###

        # Проверка указан ли путь
        if outputpath == "":
            self.set_status('The file saving path is not specified!', '#f6b233')
            return

        # Проверка существует ли путь
        if not os.path.exists(outputpath):
            self.set_status('The file saving path does not exist!', '#f63333')
            return


        
                
        
        # Если выбраны
        for file in FilesList: # <-- Для каждого файла выполнить:

            # Созадть новое имя файла и расширение.
            original_name = os.path.splitext(os.path.basename(file))[0]
            extension = os.path.splitext(os.path.basename(file))[1]

            # Расширение.
            if selected_format == 'original format':
                newformat = extension
            else:
                newformat = "." + selected_format

            # Базовое имя выходного файла.
            if outputname:
                newname = outputname
                base_name = outputname
            else:
                base_name = f"FFS-{original_name}"
                newname = base_name

            # Проверка существования файла.
            counter = 1
            while True:
                output_file = os.path.join(outputpath, 
                                            f"{newname}{newformat}")
                if os.path.exists(output_file):
                    self.set_status('A file with that name already exists. Assigning a new name.', '#ffffff')
                    newname = f'{base_name} ({counter})'
                    counter += 1
                else:
                    break

            # Создание команды
            command = ["ffmpeg"]

            # Проверка выполнять ли обрезку по времени.
            if self.ui.CropTheVideo.isChecked():

                # Проверка что бы конечное время было больше начального.
                if cropEND > cropSTART:
                    command += ['-ss', cropSTART,
                                '-to', cropEND]
                else:
                    self.set_status('The end time must be later than the start time.', '#f6b233')
                    return




            
            # Добавить файл с которым работаем.
            command += ['-i', file]

            # Проверить если оригинальные настройки не сохраняются.
            if not self.ui.KeepOriginal.isChecked():


                ### === Проверка разрешения === ###
                # Проверяем указано ли разрешения.
                if width and height:

                    # Проверяем что оба значения положительные.
                    if int(width) > 0 and int(height) >0:
                      command += ['-vf',
                            f'scale={width}:{height}']
                    else:
                        self.set_status('The width and height must be positive integers greater than zero.', '#f6b233')
                        return

                elif width or height:
                    self.set_status('You must specify both the width and height.', '#f6b233')
                    return



                ### === Проверка FPS === ###
                # Проверяем указан ли FPS.
                if fps:

                    # Проверяем что FPS больше 0
                    if int(fps) > 0:
                        command += ['-r', fps]
                    else:
                        self.set_status('FPS must be a positive integer greater than zero.', '#f6b233')
                        return



                ### === Проверка битрейта === ###
                # Проверяем указан ли битрейт.
                if bitrate:

                    # Проверяем что битрейта больше 0
                    if int(bitrate) > 0:
                        command += ['-b:v',
                                    f'{bitrate}k']
                    else:
                        self.set_status('Bitrate must be greater than zero.', '#f6b233')
                        return


                ### === Проверка звука === ###
                # Проверяем указан ли битрейт звука.
                if sound:

                    # Проверяем что битрейта аудио больше 0
                    if int(sound) > 0:
                        command += ['-b:a',
                                    f'{sound}k']
                    else:
                        self.set_status('Audio bitrate must be greater than zero.', '#f6b233')
                        return







                    

            # Указать путь сохранения и названеия выходного файла.
            command += [output_file]
            print(command)
            
            convert = subprocess.run(command, creationflags=subprocess.CREATE_NO_WINDOW)
            result = convert.returncode

            if result == 0:
                self.set_status('Last task completed successfully.', '#00FF88')
            else:
                self.set_status('Task failed.', '#f63333')













if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
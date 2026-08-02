import time
import os
import subprocess
from PySide6.QtCore import QObject, Signal

class Worker(QObject):

    finished = Signal(str, str) # Ответ результата.
    error = Signal(str, str) # Ответ ошибки.

    # Получение переменных для работы FFmpeg.
    def __init__(self, data):

        super().__init__()
        self.data = data # Получение данных


    # Проверка наличия FFmpeg.
    def ffmpegcheck(self):
        try:
            ffmpegcheck = subprocess.run(["ffmpeg", "-version"],
                            capture_output=True, text=True,
                            creationflags=subprocess.CREATE_NO_WINDOW)
            
        except FileNotFoundError:
            self.error.emit('Looks like there is no FFmpeg on your device. Download it from the official website.', '#f63333')
            return False

        if ffmpegcheck.returncode != 0:
            self.error.emit('FFmpeg was found but returned an error. Try to reinstall it from the official website.', '#f63333')
            return False

        return True


    # Сборка комманды.
    def command_build(self, file):

        FilesList = self.data[0]
        cropSTART = self.data[1]
        cropEND = self.data[2]
        width = self.data[3]
        height = self.data[4]
        fps = self.data[5]
        bitrate = self.data[6]
        sound = self.data[7]
        selected_format = self.data[8]
        outputname = self.data[9]
        outputpath = self.data[10]

        docrop = self.data[11]
        keeporiginal = self.data[12]



        #  Проверка выбраны ли файлы
        # ---------------------------
        if not FilesList:
            self.error.emit('No files Selected!', '#f6b233')
            return None


        #  Проверка пути сохраненияю
        # ---------------------------

        # Проверка указан ли путь
        if outputpath == "":
            self.error.emit('The file saving path is not specified!', '#f6b233')
            return None

        # Проверка существует ли путь
        if not os.path.exists(outputpath):
            self.error.emit('The file saving path does not exist!', '#f6b233')
            return None


        #  Созадть новое имя файла и расширение
        # --------------------------------------
        original_name = os.path.splitext(os.path.basename(file))[0]
        extension = os.path.splitext(os.path.basename(file))[1]

        # Расширение
        if selected_format == 'original format':
            newformat = extension
        else:
            newformat = "." + selected_format

        # Базовое имя выходного файла
        if outputname:
            newname = outputname
            base_name = outputname
        else:
            base_name = f"FFS-{original_name}"
            newname = base_name


        #  Проверка существования файла с таким же названием
        # ---------------------------------------------------
        counter = 1
        while True:
            output_file = os.path.join(outputpath, 
                                        f"{newname}{newformat}")
            if os.path.exists(output_file):
                self.error.emit('A file with that name already exists. Assigning a new name.', '#ffffff')
                newname = f'{base_name} ({counter})'
                counter += 1
            else:
                break


        #  Создание команды
        # ------------------
        command = ["ffmpeg"]


        # Обрезка по времени
        # -------------------
        if docrop:
            # Проверка что бы конечное время было больше начального.
            if cropEND > cropSTART:
                command += ['-ss', cropSTART,
                            '-to', cropEND]
            else:
                self.error.emit('The end time must be later than the start time.', '#f6b233')
                return None


        #  Файл с которым работаем
        # -------------------------
        command += ['-i', file]


        #  Оригинальные настройки
        # ------------------------
        if not keeporiginal:

            #  Разрешение
            # ------------
            if width and height:

                # Проверяем что оба значения положительные.
                if int(width) > 0 and int(height) >0:
                    command += ['-vf',
                        f'scale={width}:{height}']
                else:
                    self.error.emit('The width and height must be positive integers greater than zero.', '#f6b233')
                    return None

            elif width or height:
                self.error.emit('You must specify both the width and height.', '#f6b233')
                return None



            #  FPS
            # -----
            if fps:

                # Проверяем что FPS больше 0
                if int(fps) > 0:
                    command += ['-r', fps]
                else:
                    self.error.emit('FPS must be a positive integer greater than zero.', '#f6b233')
                    return None



            #   Битрейт
            # ------------
            if bitrate:

                # Проверяем что битрейта больше 0
                if int(bitrate) > 0:
                    command += ['-b:v',
                                f'{bitrate}k']
                else:
                    self.error.emit('Bitrate must be greater than zero.', '#f6b233')
                    return None
                

            #   Звук
            # -------
            if sound:

                # Проверяем что битрейта аудио больше 0
                if int(sound) > 0:
                    command += ['-b:a',
                                f'{sound}k']
                else:
                    self.error.emit('Audio bitrate must be greater than zero.', '#f6b233')
                    return None


        #  Путь сохранения
        # ------------------
        command += [output_file]

        # Передача команды в run()
        # -------------------------
        return command


    # Запуск команды.
    def run(self):

        # Вызов проверки FFmpeg.
        if not self.ffmpegcheck():
            return

        FilesList = self.data[0]

        if not FilesList:
            self.error.emit('No files Selected!', '#f6b233')
            return

        for file in FilesList:

            command = self.command_build(file)

            if command is None:
                return

            convert = subprocess.run(command, creationflags=subprocess.CREATE_NO_WINDOW)

            if convert.returncode != 0:
                self.error.emit("Task failed.", "#f63333")
                return

        self.finished.emit("Last task completed successfully.", "#00FF88")

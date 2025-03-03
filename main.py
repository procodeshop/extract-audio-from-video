from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import threading
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QProgressBar
# from moviepy.video.io.ffmpeg_tools import ProgressBarLogger
from proglog import ProgressBarLogger
class MyBarLogger(ProgressBarLogger):
    def callback(self, **changes):
        # Every time the logger message is updated, this function is called with
        # the `changes` dictionary of the form `parameter: new value`.
        for (parameter, value) in changes.items():
            print(f'Parameter {parameter} is now {value}')

    def bars_callback(self, bar, attr, value, old_value=None):
        # Every time the logger progress is updated, this function is called
        if 'total' in self.bars[bar]:
            percentage = (value / self.bars[bar]['total']) * 100
            print(bar, attr, percentage)
            # Update the progress bar in the PyQt application
            if hasattr(self, 'progress_bar_widget'):
                self.progress_bar_widget.setValue(int(percentage))

class VideoToAudioConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Video to Audio Converter")
        self.setGeometry(100, 100, 500, 250)

        layout = QVBoxLayout()

        self.label_file = QLabel("Select Video File:")
        layout.addWidget(self.label_file)

        self.entry_file = QLineEdit(self)
        layout.addWidget(self.entry_file)

        self.button_file = QPushButton("Browse", self)
        self.button_file.clicked.connect(self.select_file)
        layout.addWidget(self.button_file)

        self.label_dest = QLabel("Select Destination Folder:")
        layout.addWidget(self.label_dest)

        self.entry_dest = QLineEdit(self)
        layout.addWidget(self.entry_dest)

        self.button_dest = QPushButton("Browse", self)
        self.button_dest.clicked.connect(self.select_destination)
        layout.addWidget(self.button_dest)

        self.button_convert = QPushButton("Convert", self)
        self.button_convert.setStyleSheet("background-color: green; color: white;")
        self.button_convert.clicked.connect(self.convert_video)
        layout.addWidget(self.button_convert)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.status_label = QLabel("", self)
        self.status_label.setStyleSheet("color: gray;")
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Video File", "",
                                                   "Video Files (*.mp4 *.avi *.mov *.mkv *.flv *.wmv *.webm)")
        if file_path:
            self.entry_file.setText(file_path)

    def select_destination(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Destination Folder")
        if folder_path:
            self.entry_dest.setText(folder_path)

    def convert_video(self):
        input_file = self.entry_file.text()
        output_folder = self.entry_dest.text()

        if not input_file or not output_folder:
            self.status_label.setText("Error: Please select both input file and destination folder.")
            self.status_label.setStyleSheet("color: red;")
            return

        def conversion_thread():
            try:
                self.progress_bar.setValue(0)
                self.status_label.setText("Converting... Please wait.")
                self.status_label.setStyleSheet("color: blue;")

                logger = MyBarLogger()
                logger.progress_bar_widget = self.progress_bar  # Bind the progress bar to the logger

                video = VideoFileClip(input_file)
                output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + ".mp3")
                video.audio.write_audiofile(output_file, logger=logger)

                self.progress_bar.setValue(100)
                self.status_label.setText("Conversion completed successfully!")
                self.status_label.setStyleSheet("color: green;")
            except Exception as e:
                self.status_label.setText(f"Error: {e}")
                self.status_label.setStyleSheet("color: red.")

        thread = threading.Thread(target=conversion_thread)
        thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoToAudioConverter()
    window.show()
    sys.exit(app.exec_())
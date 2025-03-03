This is a simple PyQt5-based GUI application that allows users to convert video files to audio (MP3) format. It uses the moviepy library to extract audio from video files and supports various video formats such as MP4, AVI, MOV, MKV, FLV, WMV, and WEBM.

# Features

🎥 Convert video files to audio (MP3)

🖥️ User-friendly graphical interface built with PyQt5

🎵 Supports multiple video file formats

📁 Allows users to select input video files and destination folders

📊 Displays conversion progress with a progress bar

✅ Provides status updates to notify users about the conversion process

# Installation

Make sure you have Python installed. Then, install the required dependencies by running:

pip install -r requirements.txt

Alternatively, install the dependencies manually:

pip install moviepy PyQt5

# Usage

Run the script using the following command:

python main.py

Steps to Convert a Video File:

Click on the Browse button to select a video file.

Click on the Browse button to choose a destination folder.

Click the Convert button to start the conversion process.

Wait for the conversion to complete. The progress bar will show the progress, and a message will indicate when it's done.

# Code Overview

MyBarLogger: A custom logger that updates the progress bar during conversion.

VideoToAudioConverter: The main PyQt5 window containing UI elements for file selection and conversion.

convert_video: Function that handles the video-to-audio conversion in a separate thread to keep the UI responsive.

Supported Formats

Input: .mp4, .avi, .mov, .mkv, .flv, .wmv, .webm

Output: .mp3

Contributing

Pull requests are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

# License

This project is open-source and available under the MIT License.

⭐ Don't forget to star this repository if you found it useful! ⭐

# YOUTUBE MP3 DOWNLOADER FOR PC

# Using "pip install pytube" or "pip3 install pytube" commands we can import the necessary YouTube library.
from pytube import YouTube
from sys import argv


# Using argv in order to access the link to the video from the command line (argv[0] has the name of this program).
link = argv[1]
# Creating a YouTube object named "yt", in which we store the link to the video we want to download.
yt = YouTube(link)

# Print the title, the numbers of views the video has as well as its length.
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: " + str(yt.length) + " sec")

# Get only the audio of the video (mp3 version).
yd = yt.streams.get_audio_only()

# Download the audio in whichever folder you want.
# (The audio gets downloaded only if it hasn't been previously downloaded)
yd.download("/Users/dimit/OneDrive/Υπολογιστής/python_audio")

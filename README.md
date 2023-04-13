you can download multiple youtube videos or music or both of them using yt_dlp and python 3.10
open in firefox tabs with the youtube links you wanna to download
this is a great tool to make txt file to use  https://addons.mozilla.org/en-US/firefox/addon/export-tabs-urls-and-titles/

Make sure that you have installed the yt-dlp module in your Python environment. You can install it using pip by running      " pip install yt-dlp" in your terminal or command prompt.

If you have already installed yt-dlp, check that you are using the correct Python environment where the module is installed. You can check the Python environment by running python --version and pip list in your terminal or command prompt.

If you have  an error like 

:Traceback` (most recent call last):   File "f.py", line 1, in <module>     import yt_dlp ModuleNotFoundError: No module named 'yt_dlp', try installing the module using in python " pip install yt-dlp. "


if u have windows have a folder with 

1 the links.txt using firefox module
2 ffmpeg.exe find it here
3 and this python_file.py 

if you have Linux just make sure you have installed ffmpeg 

on the same folder have
1 the links.txt
2 and this python_file.py 
### ### ### ### ### ### ### ### ### ### ### ### ### 
import yt_dlp #pip install yt-dlp

file_path = 'links.txt'

with open(file_path, 'r') as f:
    video_links = [line.strip() for line in f]

ydl_opts = {
    'format': 'bestvideo+bestaudio', #you can change here qualities 
    'outtmpl': '%(title)s.%(ext)s',
    'fragment_retries': 100000,
    'max_sleep_interval': 1,
    'retry_max_sleep': 2,
}


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_links)
###########################################
here is for the music 

import yt_dlp

file_path = 'links.txt'

with open(file_path, 'r') as f:
    video_links = [line.strip() for line in f]

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(autonumber)s_%(title)s.%(id)s.%(ext)s',
    'fragment_retries': 100000,
    'max_sleep_interval': 1,
    'retry_max_sleep': 2,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '64',

    }],
    'socket_timeout': 5,  # set a low socket timeout to use multiple threads
    'extractaudio': True,  # add this option to extract only audio 
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_links)

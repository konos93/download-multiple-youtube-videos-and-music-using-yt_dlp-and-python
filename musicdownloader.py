import yt_dlp

file_path = 'links.txt'

with open(file_path, 'r') as f:
    video_links = [line.strip() for line in f]

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(autonumber)s_%(title)s.%(ext)s',
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


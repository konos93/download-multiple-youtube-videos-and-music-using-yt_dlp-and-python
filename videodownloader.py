import yt_dlp

file_path = 'links.txt'

with open(file_path, 'r') as f:
    video_links = [line.strip() for line in f]

ydl_opts = {
    'format': 'bestvideo+bestaudio',
    'outtmpl': '%(title)s.%(ext)s',
    'fragment_retries': 100000,
    'max_sleep_interval': 1,
    'retry_max_sleep': 3,
}


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_links)
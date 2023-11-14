import yt_dlp
import os
import glob
import re
import concurrent.futures
import time 

start_time = time.time()

for _ in range(2): # i run it 2 times because sometimes it does not download ,last time i check was 2 url from 60 

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s_%(id)s.%(ext)s',
        'fragment_retries': 100000,
        'max_sleep_interval': 1,
        'retry_max_sleep': 1,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '64',
        }],
        'socket_timeout': 50,
        'extractaudio': True,
        'quiet': False,  # Set to False to enable verbose output
        'verbose': True,  # Set to True to enable verbose output
        'keepvideo': False,  # This option keep the downloaded files from being deleted ,type false if u wanna to delete
        'concurrent-fragments': 1  # Set the number of concurrent fragments you want to download,i did not see much different
    }
    '''

     #if u wanna download video use this staff here i use it to watch some lectures on smartphone 
     # and sometimes i need to check slides u can change the format for differnet quality
    ydl_opts = {
        'format': 'best[height<=480]/bestvideo[height<=480]+bestaudio',
        'outtmpl': '%(title)s_%(id)s.%(ext)s',
        'fragment_retries': 100000,
        'max_sleep_interval': 1,
        'retry_max_sleep': 1,
        'socket_timeout': 50,
        'extractaudio': True,
        'quiet': False,  # Set to False to enable verbose output
        'verbose': True,  # Set to True to enable verbose output
        'keepvideo': False,  # This option keep the downloaded files from being deleted ,type false if u wanna to delete
        'concurrent-fragments': 1  # Set the number of concurrent fragments you want to download,i did not see much different
    }
    '''

        
    with open('links.txt', 'r', encoding='utf-8') as input_file, open('helplinks.txt', 'w', encoding='utf-8') as output_file:
        links = input_file.read().splitlines()
        
        for i, link in enumerate(links, 1):
            link = link.strip()
            if link.startswith("https://www.youtube.com/watch?v="):
                formatted_link = f' {link[:43]} {i:04d}'
                output_file.write(formatted_link + '\n')


    directory = os.getcwd()

    file_list = os.listdir(directory)

    file_path = 'helplinks.txt'


    if not any (file.endswith(".mp4") or file.endswith(".mp3") for file in file_list):



        with open(file_path, 'r') as f:
            video_links = [line.strip() for line in f]


        def download_video(link):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

        # Set the maximum number of concurrent downloads (you can adjust this) .how many url u download in the same time?
        max_concurrent_downloads = 50

        with concurrent.futures.ThreadPoolExecutor(max_concurrent_downloads) as executor:
            executor.map(download_video, video_links)


    else:

        webm_files = glob.glob(os.path.join(directory, "*.webm")) + glob.glob(os.path.join(directory, "*.webm.part"))
        print("webm part or file deleted")

        # Iterate through the list of webm files and delete them
        for webm_file in webm_files:
            try:
                os.remove(webm_file)
                print(f"Deleted: {webm_file}")
            except OSError as e:
                print(f"Error deleting {webm_file}: {e}")
                
        current_directory = os.getcwd()
        output_file = 'file_list.txt'

        with open(output_file, 'w', encoding='utf-8') as f:
            for filename in os.listdir(current_directory):
                if os.path.isfile(filename):
                    f.write(filename + '\n')


        file_list_path = 'file_list.txt'  # Path to the file containing existing titles

        # Read the existing titles from file_list.txt
        with open(file_list_path, 'r', encoding='utf-8') as f_list:
            existing_titles = f_list.read()

        with open(file_path, 'r', encoding='utf-8') as f:
            video_links = [line.strip() for line in f]

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for link in video_links:
                info_dict = ydl.extract_info(link, download=False)  # Get video information without downloading
                video_title = info_dict.get('id', '')  # Get video id
                if video_title not in existing_titles:
                    ydl.download([link])  # Download the video if the id is not found within file_list.txt


       
    for _ in range(10): #lol because sometimes i got names like 0001_0001_0001_0001 nevergonagive up.mp3
        for filename in os.listdir(directory):
            if (filename.endswith(".mp4") or filename.endswith(".mp3")):
                # Use regular expressions to remove leading four-digit numbers
                new_filename = re.sub(r"^\d{4}_", "", filename)
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
         
    # Function to extract video ID from a YouTube URL
    def extract_video_id(url):
        match = re.search(r'v=([A-Za-z0-9_\-]+)', url)
        if match:
            return match.group(1)
        return None


            
    # Read links from the links.txt file
    with open(os.path.join(directory, "helplinks.txt"), "r", encoding='utf-8') as links_file:
        links = links_file.readlines()

    # Rename files based on the links
    for link in links:
        link = link.strip()
        video_id = extract_video_id(link)
        if video_id:
            for filename in os.listdir(directory):
                if (filename.endswith(".mp4") or filename.endswith(".mp3")) and video_id in filename:
                    new_filename = f"{link.split()[-1]}_{filename}"
                    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                 #   print(f"Renamed: {filename} to {new_filename}")   


    files_to_remove = ['file_list.txt', 'helplinks.txt']

    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)

              
end_time = time.time()  # Record the end time
elapsed_time = end_time - start_time
    
print(f"Total time taken: {elapsed_time:.2f} seconds")
    
print("Done")

#!/bin/bash

# If you're using GNOME (Ubuntu, Pop!_OS, Fedora, etc.):
# Open Settings.
# Go to Keyboard.
# Scroll to the bottom and click + to add a custom shortcut.
# Name: anything like YouTube Downloader
# Command: /home/kmk/downloadfromyoutube/ctrl_alt_s.sh
# Set the shortcut to Ctrl + Alt + H.
# wget https://github.com/yt-dlp/yt-dlp/releases/download/2025.06.09/yt-dlp_linux -O yt-dlp
# chmod +x yt-dlp
# which yt-dlp
# sudo mv ~/downloadfromyoutube/yt-dlp /usr/bin/yt-dlp
# tail -f /home/kmk/downloadfromyoutube/ctrl_alt_h.log to check if working


exec > /home/kmk/downloadfromyoutube/ctrl_alt_h.log 2>&1
export DISPLAY=:1  # Use correct DISPLAY number
cd /home/kmk/downloadfromyoutube #path to save

echo "DISPLAY=$DISPLAY"
echo "USER=$USER"

# Activate Firefox window
xdotool search --class "Firefox" windowactivate
sleep 1

# Copy current URL
xdotool key --clearmodifiers ctrl+l
sleep 0.3
xdotool key --clearmodifiers ctrl+c
sleep 0.3

URL=$(xclip -selection clipboard -o 2>/dev/null)

if [ -z "$URL" ]; then
    echo "Failed to get URL from clipboard."
    exit 1
fi

echo "Downloading from URL: $URL"

yt-dlp \
    --format bestaudio/best \
    --output '%(title)s_%(id)s.%(ext)s' \
    --fragment-retries 100000 \
    --min-sleep-interval 0.5 \
    --max-sleep-interval 1 \
    --retry-sleep 1 \
    --extract-audio \
    --audio-format mp3 \
    --audio-quality 64K \
    --socket-timeout 50 \
    --no-keep-video \
    --concurrent-fragments 1 \
    --cookies-from-browser firefox \
    "$URL"

echo "Downloading is Done $(date '+%Y-%m-%d %H:%M')"

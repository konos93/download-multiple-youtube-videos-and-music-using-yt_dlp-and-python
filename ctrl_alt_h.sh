#!/bin/bash

# If you're using GNOME (Ubuntu, Pop!_OS, Fedora, etc.):
# Open Settings.
# Go to Keyboard.
# Scroll to the bottom and click + to add a custom shortcut.
# Name: anything like YouTube Downloader
# Command: /home/kmk/downloadfromyoutube/ctrl_alt_s.sh
# Set the shortcut to Ctrl + Alt + H.
#  tail -f /home/kmk/downloadfromyoutube/ctrl_alt_h.log to check if working

exec > /home/kmk/downloadfromyoutube/ctrl_alt_h.log 2>&1
export DISPLAY=:1
cd /home/kmk/downloadfromyoutube

echo "DISPLAY=$DISPLAY"
echo "USER=$USER"

# Focus Firefox window
xdotool search --class "Firefox" windowactivate

# Give it a moment
sleep 1

# Send Ctrl+L then Ctrl+C to copy URL
xdotool key --clearmodifiers ctrl+l
sleep 0.2
xdotool key --clearmodifiers ctrl+c
sleep 0.2

# Read from clipboard
URL=$(xclip -selection clipboard -o 2>/dev/null)

if [ -z "$URL" ]; then
    echo "Failed to get URL from clipboard."
    exit 1
fi

# Export URL as env variable if needed
export URL

# ✅ Activate virtual environment
source /home/kmk/yt_env/bin/activate

# Run Python scripts
python3 /home/kmk/downloadfromyoutube/copytolink.py
sleep 2
python3 /home/kmk/downloadfromyoutube/musicdownloader.py

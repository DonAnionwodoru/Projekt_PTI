#!/bin/bash

echo The script is running
# 1. Force cron to load your normal terminal's environment and paths
source ~/.bashrc

# 2. Move directly into your project folder
cd /home/janek/Desktop/work/studia/knsi/CheckersBot/

# 3. If you use a virtual environment, remove the '#' on the next line to activate it:
source .venv/bin/activate

# 4. Run the Python script normally, just like you do in the terminal
cd /home/janek/PycharmProjects/pti_proj/FrameSaver
python3 screenshots.py

echo The script is finished
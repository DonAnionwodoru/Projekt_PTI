from ss_function import Screenshooter

# USTAWIENIA
SOURCE = 'https://youtu.be/1ieoJnt8grw'
dtime = 15 # Ile czasu miedzy screenami w minutach
max_frames = 100 # Ile screenow chcemy
FOLDER_NAME = 'ss' # nazwa istniejacego folderu w ktorym zapisujemy screeny
settings = {"STREAM_RESOLUTION": "720p"} # Tutaj mozna zmienic jakosc

Screenshooter(URL=SOURCE,settings=settings,FOLDER_NAME=FOLDER_NAME,dtime=dtime,max_frames=max_frames)

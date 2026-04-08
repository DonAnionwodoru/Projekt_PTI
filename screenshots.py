from ss_function import Screenshooter

# USTAWIENIA
Start_Time = [2,0] # godzina do ktorej program czeka zeby odpalic zapisywanie. Format : [Godzina, minuta]
                   # jezeli chcemy, zeby program dzialal od razu, usuwamy argument z funkcji
                   # program automatycznie wykryje jezeli godzina juz minela i zalozy ze chodzi o kolejny dzien
                   # np jezeli jest 23:50, wpiszemy [0,5], to program zaczeka 15 minut
SOURCE = 'https://www.youtube.com/watch?v=4p9DlyqEJYA'
dtime = 15 # Ile czasu miedzy screenami w minutach
max_frames = 100 # Ile screenow chcemy
FOLDER_NAME = 'ss' # nazwa istniejacego folderu w ktorym zapisujemy screeny
settings = {"STREAM_RESOLUTION": "480p"} # Tutaj mozna zmienic jakosc

Screenshooter(URL=SOURCE,
              settings=settings,
              FOLDER_NAME=FOLDER_NAME,
              dtime=dtime,
              max_frames=max_frames,
              start_time=Start_Time)

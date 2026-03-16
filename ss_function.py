import cv2
import time
from vidgear.gears import CamGear
import yt_dlp

def Screenshooter(URL, settings, dtime ,max_frames, FOLDER_NAME ,IsStream=True):
    STREAM_URL = None
    VIDEO_URL = None
    if IsStream:
        STREAM_URL = URL
    else:
        VIDEO_URL = URL
    #
    dstime = int(dtime*60)
    frame_counter = 0
    # petla dla streama:
    stream = None
    while IsStream and frame_counter < max_frames:
        stream = CamGear(source=STREAM_URL, logging=False, stream_mode=True, **settings).start()
        frame = stream.read()
        try:
            timestamp = int(time.time())
            filename = f"{FOLDER_NAME}/image_{timestamp}.jpg"
            if frame is not None:
                cv2.imwrite(filename, frame)
                print(f"saved {frame_counter+1}/{max_frames} -- {filename}")
                frame_counter += 1
            else:
                print(f"failed to save a file {frame_counter+1}/{max_frames} -- {filename}")
        except:
            print("Program stopped manually")
        finally:
            stream.stop()
        if frame_counter <= max_frames:
            time.sleep(dstime)
    if IsStream:
        stream.stop()

    # dla filmiku na yt:
    if not IsStream:
        ydl_opts = {'format': 'best[ext=mp4][height<=720]'}
        cap = cv2.VideoCapture(URL)
        if not cap.isOpened():
            print("failed to open video file")
        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps == 0:
            fps = 30
        frame_interval = int(fps*dstime)
        frame_counter = 0
        current_frame_position = 0
        # video loop
        while frame_counter < max_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame_position)
            ret, frame = cap.read()
            if not ret:
                print("Reached the end of the video.")
                break
            filename = f"{FOLDER_NAME}/image_{frame_counter:03d}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved {frame_counter + 1}/{max_frames} -- {filename}")
            frame_counter += 1
            current_frame_position += frame_interval
        cap.release()

    # zakonczenie dzialania funkcji
    print("Process stopped")
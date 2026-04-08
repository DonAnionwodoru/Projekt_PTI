import cv2
import time as Time
from datetime import datetime, time, timedelta
from vidgear.gears import CamGear
import yt_dlp

def Screenshooter(URL, settings, dtime ,max_frames, FOLDER_NAME, start_time=[-1,-1]):
    # czekamy do podanej godziny, jezeli jest po tej godzinie nie czekamy wgl
    if start_time[0] >= 0 and start_time[1] >= 0:
        now = datetime.now()
        target_time = time(start_time[0],start_time[1])
        target_dt = datetime.combine(now.date(), target_time)
        if now.time() > target_time:
            target_dt = target_dt.replace(day=target_dt.day + 1)
        waittime = (target_dt - now).total_seconds()
        print(f"current time: {now.time()} | target time: {target_dt.time()}")
        print(f"waiting {int(waittime/3600)}:{int((waittime%3600)/60)}:{int((waittime%3600)%60)}...")
        Time.sleep(waittime)

   #
    STREAM_URL = URL
    dstime = int(dtime*60)
    frame_counter = 0
    # petla dla streama:
    while frame_counter < max_frames:
        stream = CamGear(source=STREAM_URL, logging=False, stream_mode=True, **settings).start()
        frame = stream.read()
        try:
            timestamp = int(Time.time())
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
            Time.sleep(dstime)
    # zakonczenie dzialania funkcji
    print("Process stopped")
import time
from winsound import SND_FILENAME, PlaySound


def read_script(scene, start, end, interval=1, basedir=".."):
    for i in range(start, end + 1):
        f = f"{basedir}/assets/{scene}/{i}.wav"
        PlaySound(f, SND_FILENAME)
        time.sleep(interval)

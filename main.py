from threading import Thread
from cameras import *
from lam import *
from parking import *
from weather import *
import time


def main():
    threads = [cameras_start, lam_start, parking_start, weather_start]
    for thread in threads:
        thread = Thread(target=thread)
        thread.start()
        time.sleep(5)


if __name__ == '__main__':
    main()

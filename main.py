from threading import Thread
from cameras import *
from lam import *
from parking import *
from weather import *
import time


class Main:
    def __init__(self, started):
        self.start_list = started

    def start(self):
            self.start()
            time.sleep(1)


def main():
    threads = [cameras_start, lam_start, parking_start, weather_start]
    for thread in threads:
        t = Main(thread)
        t.start()


if __name__ == '__main__':
    main()

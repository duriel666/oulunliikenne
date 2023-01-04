import threading
from cameras import *
from lam import *
from parking import *
from weather import *
import time


class Main:
    def __init__(self, started):
        self.started = started
        self.t = threading.Thread(target=self.run(self.started))
        self.t.start()
        self.t.join()

    def run(self, started):
        self.started()
        


def main():
    threads = [cameras_start, lam_start, parking_start, weather_start]
    for thread in threads:
        Main(thread)


if __name__ == '__main__':
    main()

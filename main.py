from threading import Thread
from cameras import *
from lam import *
from parking import *
from weather import *
import time

if __name__ == '__main__':
    t1 = Thread(target=cameras_start)
    t2 = Thread(target=lam_start)
    t3 = Thread(target=parking_start)
    t4 = Thread(target=weather_start)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print('All threads finished')
    time.sleep(1)

import threading
from cameras import *
from lam import *
from parking import *
from weather import *
import time


if __name__ == "__main__":
    total_time_start: float = time.time()
    threads: list[Any] = [cameras_start, lam_start, parking_start, weather_start]

    thread_list: list[Any] = []
    for thread_name in threads:
        t: Any = threading.Thread(target=thread_name)
        t.daemon = True
        t.start()
        thread_list.append(t)

    try:
        while threading.active_count() > 0:
            time.sleep(0.1)
    except KeyboardInterrupt:
        total_runtime: float = time.time() - total_time_start
        print("--- Terminated by user ---")
        print("--- Total runtime: {:.2f} seconds ---".format(total_runtime))

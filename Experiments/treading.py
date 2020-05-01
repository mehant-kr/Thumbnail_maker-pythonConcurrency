# import concurrent.futures
# import time

# start = time.perf_counter()

# def do_something(sec):
#     print(f'Sleeping {sec} second...')
#     time.sleep(sec)
#     return f'Done Sleeping for {sec} ...'

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     secs = [5,4,3,2,1]
#     results = executor.map(do_something, secs)

#     for f in concurrent.futures.as_completed(result):
#         print(f.result())

# finish = time.perf_counter()
# print(f'Finished in {round(finish-start, 2)} second(s)...')

import time, threading

class myThread(threading.Thread):
    def __init__(self, sec):
        self.sec = sec

    def run(self);

from time import time, sleep
from contextlib import contextmanager


class cm_timer_1:

    def __enter__(self):
        self.start = time()
    def __exit__(self, type, value, traceback):
        self.end = time()
        print(f"Затраченное время: {self.end - self.start}")

@contextmanager
def cm_timer_2() -> None:
    begin = time()
    yield
    calcTime = time() - begin
    print(f"Затраченное время: {calcTime}")


# with cm_timer_1():
#     testList = [x for x in range(100_000)]
#
# with cm_timer_1():
#     sleep(1)
#
# with cm_timer_2():
#     testList = [x for x in range(100_000_000)]
#
# with cm_timer_2():
#     sleep(1.2)
from contextlib import contextmanager
from time import time, sleep

class cm_timer_1:
    def __init__(self):
        pass

    def __enter__(self):
        self.start_time = time()
        return self.start_time

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print('time: {}'.format(time() - self.start_time))


@contextmanager
def cm_timer_2():
    start_time = time()
    yield start_time
    print('time: {}'.format(time() - start_time))


if __name__ == '__main__':
    with cm_timer_1():
        sleep(5.5)

    with cm_timer_2():
        sleep(5.5)

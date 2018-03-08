from __future__ import print_function

import time


def today_time(t):
    format = '%H:%M:%S'
    value = time.localtime(int(t))
    today_time = time.strftime(format, value)
    return today_time


def log(*args, **kwargs):
    t = time.time()
    t_t = today_time(t)
    f = open('whister.log.txt', 'a')
    print(t_t, *args, **kwargs)
    print(t_t, *args, file=f, **kwargs)

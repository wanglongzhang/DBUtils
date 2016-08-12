#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Singleton 4 multi thread
"""
import threading

__all__ = ["local"]

class ThreadLocker:
    def __init__(self, lock):
        self.lock = lock

    def __enter__(self):
        self.lock.acquire()
        return self.lock

    def __exit__(self, type, msg, traceback):
        self.lock.release()

class Singleton(object):
    objs = {}
    obj_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
       if cls in cls.objs:
            return cls.objs[cls]['obj']
       else:

           with ThreadLocker(cls.obj_lock) as lock:
                if cls in cls.objs:
                    return cls.objs[cls]['obj']
                obj = object.__new__(cls)
                cls.objs[cls] = {'obj': obj, 'init': False}
                setattr(cls, '__init__', cls.decorate_init(cls.__init__))
                return cls.objs[cls]['obj']

    @classmethod
    def decorate_init(cls, func):
        def wrapper(*args, **kwargs):
            if not cls.objs[cls]['init']:
                func(*args, **kwargs)
                cls.objs[cls]['init'] = True
            return
        return wrapper

import time

class testA(Singleton):
    def __init__(self, a, b=1):
        super(testA, self).__init__()
        self.a = a
        self.b = b
        self.current_time = time.ctime()
        time.sleep(1)

class testB(testA):
    def __init__(self, c, d=3, e=6):
        super(testB, self).__init__(c, b=d)
        self.e = e
        self.now_time = time.ctime()
        time.sleep(.5)

if __name__ == "__main__":
    for i in range(3):
        test_obj = testB(i, d=i)
        print(test_obj)






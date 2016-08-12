#!/usr/bin/env python
# -*- coding:utf-8 -*-

from DBUtils.Singleton import Singleton
from DButils.PooledDB import PooledDB

class SinglePooledDB(Singleton, PooledDB):
    def __init__(self, 
                creator,
                mincached=0,
                maxcached=0,
                maxshared=0,
                maxconnections=0,
                blocking=False,
                maxusage=None,
                setsession=None,
                reset=True,
                failures=None,
                ping=1,
                *args, **kwargs):
                
        super(SinglePooledDB, self).__init__(
                                            creator,
                                            mincached=mincached,
                                            maxcached=maxcached,
                                            maxshared=maxshared,
                                            maxconnections=maxconnections,
                                            blocking=blocking,
                                            maxusage=maxusage,
                                            setsession=setsession,
                                            reset=reset,
                                            failures=failures, 
                                            ping=ping, 
                                            *args, **kwargs)



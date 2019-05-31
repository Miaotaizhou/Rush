#! usr/bin/python3
# *-* coding=UTF-8 *-*
__author__ = "Rush"

import time


class Clock(object):
    """数字时钟"""


    def __init__(self,hour=0,minute=0,second=0):
        """

        :param hour: 小时
        :param minute: 分钟
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """时钟行走"""
        self._second += 1
        if self._second == 60:
            self._second =0
            self._minute +=1
            if self._minute == 60:
                self._minute =0
                self._hour += 1
                if self._hour ==24:
                    self._hour =0

    def show(self):
        """显示时间"""
        return  '%02d:%02d:%02d'% (self._hour,self._minute,self._second)

def main():
    clock = Clock(12,0,0)
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()


#! usr/bin/python3
# *-* coding=UTF-8 *-*
__author__ = "Rush"

import math


'''
1.求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只
穷举法
'''
def chicken():
    for i in range(1,20):
        for j in range(1,33):
            k = 100-i-j
            if 5*i+3*j+k/3 == 100:
                print('公鸡：%d只,母鸡：%d只,小鸡：%d只' % (i,j,k))
'''
水仙花数：一个3位数，其中每个位上数字的3次幂之和等于它本身
如：1^3+5^3+3^=153
'''
def narcissistic():
    for num in range(100,1000):
        digits = num%10
        ten_digits = num//10%10
        hundred_digits = num//100
        if num == math.pow(digits,3)+math.pow(ten_digits,3)+math.pow(hundred_digits,3):
            print(num)

'''
完美数：除去该数本身且小于该数的约数之和等于该数本身
如：6的约数有1,2,3,6,除去6,其余数之和为6
'''
# 寻找1～10000的完美数
def perfect():
    for num in range(1,10000):
        sum = 0
        for factor in range(1,int(math.sqrt(num)) + 1):
            if num % factor == 0:
                sum += factor
                if factor >1 and num/factor != factor:
                    sum += num/factor
        if sum == num:
            print(num)

if __name__ == '__main__':
    chicken()
    print('-'*50)
    narcissistic()
    print('-' * 50)
    perfect()
    print('-' * 50)



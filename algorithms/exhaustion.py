#! usr/bin/python3
# *-* coding=UTF-8 *-*
__author__ = "Rush"

'''
A、B、C、D、E五人在某天夜里合伙捕鱼,最后疲惫不堪各自睡觉,
第二天A第一个醒来,他将鱼分为5份,扔掉多余的1条,拿走自己的一份,
B第二个醒来,也将鱼分为5份,扔掉多余的1条,拿走自己的一份,
然后C、D、E依次醒来也按同样的方式分鱼,问他们至少捕了多少条鱼
'''
# 先假设E至少1只
# 使用枚举法，循环查找符合分配规则的鱼数
# 每次分配是的总数需满足以下条件：总数减1是5的倍数


def sep_fish(n):
    fish = 1
    while True:
        total = fish
        enough = True
        for _ in range(n):
            if (total - 1) % n == 0:
                total = (total - 1) // n * (n-1)
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += n


if __name__ == '__main__':
    n = int(input('请输入分鱼的人数：'))
    sep_fish(n)
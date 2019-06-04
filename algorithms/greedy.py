#! usr/bin/python3
# *-* coding=UTF-8 *-*
__author__ = "Rush"


'''
假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。
很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。
价格(美元)={电脑：200， 收音机：20， 钟：175，  花瓶：50，  书：10，   油画：90}
重量(kg)={电脑：20，  收音机：4，  钟：10，   花瓶：2，   书：1，    油画：9}
最大重量20kg，物品数量6件
在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解
'''


class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    # 以价格重量的比值衡量物品拿走优先度
    @property
    def value(self):
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input('物品名称，价格，重量: ').split()
    return name_str, int(price_str), int(weight_str)


def main():
    """主函数"""
    max_weight, num_of_things = map(int, input('最大重量,物品总数:').split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'总价值: {total_price}美元')


if __name__ == '__main__':
    main()
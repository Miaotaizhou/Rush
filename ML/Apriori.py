#! usr/bin/python3
# *-* coding=UTF-8 *-*
__author__ = "Rush"


'''
使用Apriori算法发掘癌症与各中医证型的关联规则
'''

import time
import pandas as pd
from sklearn.cluster import KMeans


"""
1.聚类离散化数据   clus()
2.定义连接关联输出字符串   conbstr()                  
3.定义关联规则(Apriori算法)     rule()
4.执行关联规则并计时     main()
"""
def clus():

    file = "data.xls"
    clus_result = "res/clus_data_processed.xls"
    typelabel = {
        "肝气郁结证型系数": "A",
        "热毒蕴结证型系数": "B",
        "冲任失调证型系数": "C",
        "气血两虚证型系数": "D",
        "脾胃虚弱证型系数": "E",
        "肝肾阴虚证型系数": "F",
    }
    k = 4

    data = pd.read_excel(file)
    result = pd.DataFrame()

    for key, item in typelabel.items():
        print(u"正在进行“%s”的聚类..." % key)
        kmodel = KMeans(n_clusters=k, n_jobs=4)
        kmodel.fit(data[[key]].as_matrix())

        r1 = pd.DataFrame(kmodel.cluster_centers_, columns=[item])
        r2 = pd.Series(kmodel.labels_).value_counts()
        r2 = pd.DataFrame(r2, columns=[item + "n"])
        r = pd.concat([r1, r2], axis=1).sort_values(item)
        r.index = list(range(1, 5))
        # 用来计算相邻两列的均值，以此作为边界点
        r[item] = pd.Series.rolling(r[item], 2).mean()
        r.loc[1, item] = 0.0
        result = result.append(r.T)
    result = result.sort_index()
    result.to_excel(clus_result)


def conbstr(x,marker):
    x = list(map(lambda i: sorted(i.split(marker)), x))
    r = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i][:-1] == x[j][:-1] and x[i][-1] != x[j][-1]:
                r.append(x[i][:-1] + sorted([x[j][-1], x[i][-1]]))
    return r


def rule(data, support, confidence, marker='~~'):
    result = pd.DataFrame(index=["support", "confidence"])

    # 第一批支持度筛选
    support_series = 1.0 * data.sum() / len(data)

    column = list(support_series[support_series > support].index)
    k = 0

    while len(column) > 1:
        k = k + 1
        print(u"\n正在进行第%s次搜索..." % k)

        column = conbstr(column, marker)
        print(u"数目%s..." % len(column))
        index_lst = [marker.join(i) for i in column]

        # 新的支持度函数
        sf = lambda i: data[i].prod(axis=1, numeric_only=True)
        # 计算连接后的支持度，开始筛选
        d_2 = pd.DataFrame(list(map(sf, column)), index=index_lst).T
        support_series_2 = 1.0 * d_2[index_lst].sum() / len(data)
        column = list(support_series_2[support_series_2 > support].index)

        support_series = support_series.append(support_series_2)
        column2 = []
        # 遍历所有可能的情况
        for i in column:
            i = i.split(marker)
            for j in range(len(i)):
                column2.append(i[:j] + i[j + 1:] + i[j:j + 1])

        # 置信度序列
        cofidence_series = pd.Series(index=[marker.join(i) for i in column2])

        for i in column2:
            cofidence_series[marker.join(i)] = support_series[marker.join(
                sorted(i))] / support_series[marker.join(i[:-1])]
        # 置信度筛选
        for i in cofidence_series[cofidence_series > confidence].index:
            result[i] = 0.0
            result[i]["confidence"] = cofidence_series[i]
            result[i]["support"] = support_series[marker.join(sorted(i.split(marker)))]

    result = result.T.sort_values(["confidence", "support"], ascending=False)
    print(u"\nresult:")
    print(result)

    return result


def main():
    inputfile = "data/apriori.txt"
    data = pd.read_csv(inputfile, header=None, dtype=object)

    # 计时
    start = time.clock()
    print(u"\n转换原始数据至0-1矩阵...")
    # 0-1矩阵的转换
    ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])
    b = list(map(ct, data.as_matrix()))
    data = pd.DataFrame(b).fillna(0)
    end = time.clock()
    print(u"\n转换完毕，用时：%0.2f s" % (end - start))
    # 删除中间变量b，节省内存
    del b

    # 定义支持度，置信度，连接符号
    support = 0.06
    confidence = 0.75
    ms = "---"

    # 计时
    start = time.clock()
    print(u"\n开始搜索关联规则...")
    rule(data, support, confidence, ms)
    end = time.clock()
    print(u"\n搜索完成，用时%0.2f s" % (end - start))


if __name__ == "__main__":
    clus()
    print('-'*50)
    main()
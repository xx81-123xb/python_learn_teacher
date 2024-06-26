"""
统计hello.txt文件内各个单词出现的次数
"""

from sc_util import *


def main():
    sc = get_spark_context()
    rdd = sc.textFile("hello.txt")
    rdd = rdd.flatMap(lambda s: s.split(" ")).map(lambda x: (x, 1)) \
        .reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False, numPartitions=2)
    print(rdd.collect())


# def main():
#     file = open("hello.txt", "r", encoding="UTF-8")
#     datas = []
#     for line in file.readlines():
#         for word in line.strip().split(" "):
#             datas.append((word, 1))
#     sc = get_spark_context()
#     rdd = sc.parallelize(datas)
#
#     rdd = rdd.reduceByKey(lambda x, y: x + y)
#
#     print(rdd.collect())


if __name__ == '__main__':
    main()

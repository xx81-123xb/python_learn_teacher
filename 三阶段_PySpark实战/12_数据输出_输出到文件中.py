"""
saveAsTextFile算子
支持本地,hdfs

并行度:
方法1:
    SparkConf对象设置属性全局并行度为1:
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app").set("spark.default.parallelism", "1")
    sc = SparkContext(conf=conf)
方法2:
    创建rdd的时候设置(parallelize方法传入numSlices参数为1)
"""
from sc_util import *


def main():
    sc = get_spark_context(parallelism=1)
    rdd1 = sc.parallelize([1, 2, 3, 4, 5])
    rdd2 = sc.parallelize([("Hello", 3), ("Spark", 5), ("Hi", 7)])
    rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 13, 11]])

    path1 = "output1"
    path2 = "output2"
    path3 = "output3"

    rdd1.saveAsTextFile(path1)
    rdd2.saveAsTextFile(path2)
    rdd3.saveAsTextFile(path3)


if __name__ == '__main__':
    main()

"""
演示通过PySpark代码加载数据,即数据输入
"""

from pyspark import SparkConf, SparkContext


def get_spark_context() -> SparkContext:
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
    sc = SparkContext(conf=conf)
    return sc


def main():
    sc = get_spark_context()
    # # 通过parallelize方法将Python对象加载到Spark内,成为RDD对象
    # rdd1 = sc.parallelize([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    # rdd2 = sc.parallelize({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
    # rdd3 = sc.parallelize((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    # rdd4 = sc.parallelize("abcdefghijklmnopqrstuvwxyz")
    # rdd5 = sc.parallelize({"key1": "value1", })
    #
    # # 查看RDD的数据要用collect方法
    # print(rdd1.collect())
    # print(rdd2.collect())
    # print(rdd3.collect())
    # print(rdd4.collect())
    # print(rdd5.collect())

    rdd6 = sc.textFile("hello.txt")

    print(rdd6.collect())


if __name__ == '__main__':
    main()

"""
演示数据计算
"""

from pyspark import SparkConf, SparkContext
# 下面两句话是为了解决spark找不到python解释器的错误
import os

def get_spark_context() -> SparkContext:
    os.environ["PYSPARK_PYTHON"] = "C:/Python310/python.exe"
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
    sc = SparkContext(conf=conf)
    return sc


def main():
    sc = get_spark_context()
    # 通过parallelize方法将Python对象加载到Spark内,成为RDD对象
    rdd1 = sc.parallelize([("a", 1), ("a", 1), ("b", 1), ("b", 1), ("b", 1)])
    rdd1 = rdd1.reduceByKey(lambda x, y: x + y)

    print(rdd1.collect())

if __name__ == '__main__':
    main()

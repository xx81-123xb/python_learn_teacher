from pyspark import SparkConf, SparkContext
# 下面两句话是为了解决spark找不到python解释器的错误
import os


def get_spark_context(parallelism="1") -> SparkContext:
    os.environ["PYSPARK_PYTHON"] = "C:/Python310/python.exe"
    os.environ["HADOOP_HOME"] = "D:/soft2/hadoop-3.0.0/hadoop-3.0.0"
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app").set("spark.default.parallelism", parallelism)
    sc = SparkContext(conf=conf)
    return sc

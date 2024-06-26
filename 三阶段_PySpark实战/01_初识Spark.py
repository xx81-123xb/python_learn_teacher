"""
演示获取PySpark的执行环境入库对象:SparkContext
并通过SparkContext对象获取当前PySpark版本
"""
from pyspark import SparkConf, SparkContext


def main():
    sc = get_spark_context()
    print(sc.version)
    sc.stop()


def get_spark_context():
    conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
    sc = SparkContext(conf=conf)
    return sc


if __name__ == "__main__":
    main()

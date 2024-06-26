"""
collect算子:转化为python的list
"""

from sc_util import *


def main():
    sc = get_spark_context()

    rdd = sc.parallelize([1, 2, 3, 4, 5, 6])

    print(rdd.take(3))


if __name__ == '__main__':
    main()

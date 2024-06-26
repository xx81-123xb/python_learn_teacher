from sc_util import *


def main():
    sc = get_spark_context()

    rdd = sc.parallelize([1, 2, 3, 4, 5, 6]).filter(lambda x: x % 2 == 0)
    print(rdd.collect())


if __name__ == '__main__':
    main()

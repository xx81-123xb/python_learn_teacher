from sc_util import *


class SearchLog:
    # 00:00:00
    def __init__(self, time, id, keyword, num1, num2, source):
        self.time: str = time
        self.id: str = id
        self.keyword: str = keyword
        self.num1: int = int(num1)
        self.num2: int = int(num2)
        self.source: int = source

    def getTime(self) -> str:
        return self.time.split(":")[0]

    def getSearchCount(self) -> int:
        return self.num1 + self.num2

    def toDict(self) -> dict:
        return {"time": self.time, "id": self.id, "keyword": self.keyword, "num1": self.num1, "num2": self.num2,
                "source": self.source}


def parse_line_to_searchlog(line: str) -> SearchLog:
    data_list = line.split("\t")
    return SearchLog(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5])


def main():
    sc = get_spark_context(parallelism="1")
    source_rdd = sc.textFile("search_log.txt").map(lambda line: parse_line_to_searchlog(line))
    # 需求1:热搜时间段(小时精度)Top3
    result1 = source_rdd.map(lambda searchlog: (searchlog.getTime(), searchlog.getSearchCount())) \
        .reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False, numPartitions=1).take(3)
    print(result1)
    # 需求2:热门搜索词Top3
    result2 = source_rdd.map(lambda searchlog: (searchlog.keyword, 1)).reduceByKey(lambda x, y: x + y) \
        .sortBy(lambda x: x[1], ascending=False, numPartitions=1).take(3)
    print(result2)
    # 需求3:统计黑马程序员在哪个时间段被搜索的最多
    result3 = source_rdd.filter(lambda searchlog: searchlog.keyword == "黑马程序员") \
        .map(lambda searchlog: (searchlog.getTime(), searchlog.getSearchCount())) \
        .reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1], ascending=False, numPartitions=1).take(3)
    print(result3)
    # 需求4:将数据转换为JSON格式写出为文件
    source_rdd.map(lambda searchlog: searchlog.toDict()).saveAsTextFile("综合案例JSON结果")


if __name__ == '__main__':
    main()

import json

from sc_util import *


class Order:
    def __init__(self, id, timestamp, category, areaName, money):
        self.id = id
        self.timestamp = timestamp
        self.category = category
        self.areaName = areaName
        self.money = int(money)

    def __str__(self):
        return f"{self.id},{self.timestamp},{self.category},{self.areaName},{self.money}"


def parse_line_to_order(s: str) -> Order:
    data_dict = json.loads(s)
    return Order(data_dict["id"], data_dict["timestamp"], data_dict["category"], data_dict["areaName"],
                 data_dict["money"])


def main():
    sc = get_spark_context()
    order_rdd = sc.textFile("orders.txt").flatMap(lambda x: x.split("|")).map(lambda s: parse_line_to_order(s))
    rdd1 = order_rdd.map(lambda order: (order.areaName, order.money)).reduceByKey(lambda x, y: x + y).sortBy(
        lambda x: x[1], ascending=False, numPartitions=1
    )
    print("===各个城市销售额排名:===")
    print(rdd1.collect())
    print("===全部城市所售卖的商品种类:===")
    rdd2 = order_rdd.map(lambda order: order.category).distinct()
    print(rdd2.collect())
    print("===北京有哪些商品在售卖:===")
    rdd3 = order_rdd.filter(lambda order: order.areaName == "北京").map(lambda order: order.category).distinct()
    print(rdd3.collect())


if __name__ == '__main__':
    main()

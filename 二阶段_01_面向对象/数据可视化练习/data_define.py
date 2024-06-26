"""
数据类的定义
"""
from typing import Union


class Record:

    def __init__(self, date, order_id, money: Union[int, str], province):
        self.date: str = date  # 订单日期
        self.order_id: str = order_id  # 订单ID
        if money is str:
            self.money: int = int(money)  # 订单金额
        else:
            self.money: int = money
        self.province: str = province  # 订单~

    def __str__(self):
        return f"('{self.date}','{self.order_id}','{self.money}','{self.province}')"

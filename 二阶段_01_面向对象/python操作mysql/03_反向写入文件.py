"""
1.获取数据
2.写入文件
"""

from data_define import *
from pymysql import Connection
from pymysql.cursors import Cursor
from typing import Any
from typing import Union


def get_connection(host="localhost", port=3306, user="root", password="SHENLAN@2016", autocommit=False) -> Connection:
    return Connection(host=host, port=port, user=user, password=password, autocommit=autocommit)


def select_datas() -> tuple[tuple[Any]]:
    """
    从数据库中查询数据
    :return:
    """
    connection = get_connection()
    cursor = connection.cursor()
    connection.select_db("test")
    sql = """
    select * from tbl_selldata
    """
    cursor.execute(sql)
    return cursor.fetchall()


def main():
    write2file(select_datas())


def write2file(datas: tuple):
    file = open("data.txt", "w", encoding="UTF-8")
    for data in datas:
        line = ""
        for i in range(len(data)):
            if i != len(data) - 1:
                line += f"{data[i]},"
            else:
                line += str(data[i])
        file.write(f"{line}\n")
    file.close()


if __name__ == "__main__":
    main()

"""
1.创建连接
2.解析数据
3.创建表
4.插入数据
"""

from file_define import *
from data_define import *
from pymysql import Connection
from pymysql.cursors import Cursor


def get_connection(host, port, user, password, autocommit=False) -> Connection:
    return Connection(host=host, port=port, user=user, password=password, autocommit=autocommit)


def create_table(cursor: Cursor):
    create_table_sql = """
        create table if not exists tbl_selldata 
        (
        order_id varchar(100) PRIMARY KEY,
        date DATE,
        money int,
        province varchar(100)
        );
        """
    cursor.execute(create_table_sql)


def parse_data() -> list[Record]:
    # 解析数据
    csvFileReader = CSVFileReader("2011年1月销售数据.txt")
    jsonFileReader = JSONFileReader("2011年2月销售数据JSON.txt")
    csv_datas = csvFileReader.read_data()
    json_datas = jsonFileReader.read_data()
    datas: list[Record] = csv_datas + json_datas
    return datas


def main():
    connection = get_connection("localhost", 3306, "root", "SHENLAN@2016", autocommit=True)
    cursor = connection.cursor()
    connection.select_db("test")
    # 建表
    create_table(cursor)

    # 解析数据
    datas = parse_data()

    # 插入数据
    insert_data(cursor, datas)

    connection.close()


def insert_data(cursor: Cursor, datas: list[Record]):
    values = ""
    for i in range(len(datas)):
        if i != len(datas) - 1:
            values += f"{datas[i]},"
        else:
            values += str(datas[i])
    # 插入数据
    insert_sql = f"""
    insert into tbl_selldata (date,order_id,money,province) values {values};
    """
    cursor.execute(insert_sql)


def test():
    test = ""
    record = Record("123", "654", 123, "河南")
    test += record
    print(record)


if __name__ == "__main__":
    main()

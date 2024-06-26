from pymysql import Connection
from pymysql.cursors import Cursor


def main():
    conn = Connection(
        host="localhost",
        port=3306,
        user="root",
        password="SHENLAN@2016"
    )

    print(conn.get_server_info())

    # 非查询性质
    # 获取游标对象
    cursor = conn.cursor()
    # select数据库
    conn.select_db("test")
    do_select_table(cursor)

    conn.close()


def do_create_table(cursor: Cursor):
    # 执行sql
    cursor.execute("create table if not exists test_pymysql(id int);")

def do_select_table(cursor: Cursor):
    # 执行sql
    cursor.execute("select * from tbl_book")
    data = cursor.fetchall()
    for col in data:
        print(col)

if __name__ == "__main__":
    main()

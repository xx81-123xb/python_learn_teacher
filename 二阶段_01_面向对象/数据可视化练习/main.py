"""
1.设计一个类,数据封装
2.设计抽象类,定义文件读取的相关功能,并使用子类实现具体功能
3.计算每天销售额
5.通过PyEcharts进行图形绘制
"""
from file_define import CSVFileReader, JSONFileReader, FileReader
from data_define import Record
from pyecharts.charts import Bar  # 柱状图
from pyecharts.options import *  # 可选的选项
from pyecharts.globals import ThemeType  # 图标颜色


def main():
    csvFileReader = CSVFileReader("2011年1月销售数据.txt")
    jsonFileReader = JSONFileReader("2011年2月销售数据JSON.txt")
    csv_datas = csvFileReader.read_data()
    json_datas = jsonFileReader.read_data()
    datas: list[Record] = csv_datas + json_datas
    data_dict: dict[str, int] = {}
    for record in datas:
        # if data_dict.__contains__(record.date):
        if record.date in data_dict.keys():
            data_dict[record.date] += record.money
        else:
            data_dict[record.date] = record.money

    bar = Bar(init_opts=InitOpts(
        theme=ThemeType.LIGHT, width="1600px"
    ))
    # 添加x轴数据
    bar.add_xaxis(list(data_dict.keys()))
    # 添加y轴数据
    bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(
        is_show=False
    ))
    # 添加title
    bar.set_global_opts(
        title_opts=TitleOpts(title="每日销售额")
    )
    # 渲染
    bar.render("每日销售额柱状图.html")


if __name__ == "__main__":
    main()

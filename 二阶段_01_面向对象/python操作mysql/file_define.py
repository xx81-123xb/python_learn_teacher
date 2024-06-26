"""
和文件相关的类定义
"""
import json

from data_define import Record


class FileReader:

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        pass


class GenericFileReader(FileReader):
    def __init__(self, path):
        super().__init__(path)

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list = []
        for line in f.readlines():
            line = line.strip()
            record = self.parse_line2Record(line)
            if record is not None:
                record_list.append(record)

        f.close()
        return record_list

    def parse_line2Record(self, line: str) -> Record:
        pass


class CSVFileReader(GenericFileReader):

    def __init__(self, path):
        super().__init__(path)

    def parse_line2Record(self, line: str) -> Record:
        data_list = line.split(",")
        return Record(data_list[0], data_list[1], int(data_list[2]), data_list[0])


class JSONFileReader(GenericFileReader):
    def __init__(self, path):
        super().__init__(path)

    def parse_line2Record(self, line: str) -> Record:
        data_dict = json.loads(line)
        return Record(data_dict["date"], data_dict["order_id"], data_dict["money"], data_dict["province"])


def main():
    csvFileReader = CSVFileReader("2011年1月销售数据.txt")
    jsonFileReader = JSONFileReader("2011年2月销售数据JSON.txt")
    genericFileReader = GenericFileReader("2011年2月销售数据JSON.txt")
    csv_datas = csvFileReader.read_data()
    json_datas = jsonFileReader.read_data()
    datas: list[Record] = csv_datas + json_datas


if __name__ == '__main__':
    main()


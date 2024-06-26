# 单继承
class Phone:
    IMEI = None
    producer = "GUOHAO"

    def call_by_4g(self):
        print("4g通话")


class Phone2024(Phone):
    face_id = True

    def call_by_5g(self):
        print("2022最新5g通话")


# 单继承

# 多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外记录开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    """
    pass主要用于补全语法
    """
    pass


my_phone = MyPhone()

my_phone.write_card()

# 多继承时,如果父类中的属性名相同,则前面的优先,方法一样
print(my_phone.producer)

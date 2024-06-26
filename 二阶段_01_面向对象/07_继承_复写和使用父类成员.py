class Phone:
    IMEI = None
    producer = "GUOHAO"

    def call_by_4g(self):
        print("4g通话")


class MyPhone(Phone):
    producer = "MY GUOHAO"
    """
    pass主要用于补全语法
    """

    def call_by_4g(self):
        print("开启CPU单核模式,确保通话的时候省电")
        # 方式1
        # print(f"父类的厂商是:{Phone.producer}")
        # Phone.call_by_4g(self)
        # 方式2
        print(f"父类的厂商是:{super().producer}")
        super().call_by_4g()
        print("关闭CPU单核模式,确保性能")


my_phone = MyPhone()

my_phone.call_by_4g()

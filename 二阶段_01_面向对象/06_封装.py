"""
两个下划线开头的成员方法和成员变量是私有的,类似java中的private
"""


class Phone:
    def __init__(self):
        ...

    __current_voltage = 0.5

    def call_by_5g(self):
        if self.__current_voltage >= 5:
            print("5g通话模式")
        else:
            self.__keep_single_core()
            print("电量不足,无法使用5g通话,并已设置单核运行进行省电.")

    def __keep_single_core(self):
        print("让CPU以单核模式运行")


phone = Phone()
phone.call_by_5g()

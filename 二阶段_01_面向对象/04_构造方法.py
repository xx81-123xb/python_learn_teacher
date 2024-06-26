class Bird:

    # type = None #可以省略
    # name = None
    # age = None

    def __init__(self, type="", name="", age=18, weight=90, **kwargs):
        self.type = type
        self.name = name
        self.age = age
        self.weight = weight
        if not kwargs:
            print("使用位置关键字参数")
            self.name = kwargs["name"]
            self.type = kwargs["type"]
            self.age = kwargs["age"]
            return

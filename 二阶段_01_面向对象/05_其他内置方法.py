class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """
        类似java中的toString()
        :return:
        """
        return self.name

    def __lt__(self, other):
        """
        小于符号的比较
        :param other:
        :return:
        """
        return self.age < other.age

    def __le__(self, other):
        """
        小于等于符号的比较
        :param other:
        :return:
        """
        return self.age <= other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


p1 = People("李小龙", 31)
p2 = People("李小龙", 36)

print(p1 == p2)

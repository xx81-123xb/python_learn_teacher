num: int = 10

num_list: list[int] = [1, 2, 3, 4]
my_tuple: tuple[int, str, bool] = (1, "", True)

# 基础数据类型注解
var_1: int = 10
var_2: str = "itheima"
var_3: bool = True


# 类对象
class Student:
    pass


stu: Student = Student()

# 基础容器
my_list: list = [1, 2, 3]
my_tuple: tuple = ()
my_dict: dict = {}

# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, bool] = (1, False)
my_dict: dict[str, int] = {}

# 类型注解的限制:只是备注,不会影响代码的运行
num: str = 1
print(num)

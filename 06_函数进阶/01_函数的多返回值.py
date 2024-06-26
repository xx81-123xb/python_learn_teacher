"""
演示函数的多返回值示例
"""


# 演示使用多个变量，接收多个返回值
def test_return():
    return 1, "hello", True,"abc"


x, y, z,f = test_return()
print(x)
print(y)
print(z)

result = test_return()
print(type(result))
result = (1,)
print(type(result))
for it in result:
    print(it)

index = result.index(1)
print(index)


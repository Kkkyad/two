# 基础打印语句
print("Hello, World!")
print('你好，世界！')

# 变量打印
name = "Alice"
age = 25
print(name)
print(age)

# 格式化打印 - f-string（推荐）
print(f"我的名字是 {name}，今年 {age} 岁")
print(f"计算结果：2 + 3 = {2 + 3}")

# 格式化打印 - format方法
print("我的名字是 {}，今年 {} 岁".format(name, age))
print("我的名字是 {0}，今年 {1} 岁".format(name, age))

# 格式化打印 - % 格式化
print("我的名字是 %s，今年 %d 岁" % (name, age))

# 多个值打印
print("姓名:", name, "年龄:", age)
print("值1", "值2", "值3", sep=" | ")  # 自定义分隔符
print("这行不换行", end="")  # 不换行
print(" 接着打印")

# 列表和字典打印
numbers = [1, 2, 3, 4, 5]
person = {"name": "Bob", "age": 30}
print("数字列表:", numbers)
print("个人信息:", person)

# 循环打印
for i in range(1, 6):
    print(f"第 {i} 次循环")

for num in numbers:
    print(f"数字: {num}")

# 条件打印
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
else:
    print("需要努力")

# 错误调试打印
def debug_function(x, y):
    print(f"DEBUG: x={x}, y={y}")
    result = x + y
    print(f"DEBUG: 计算结果={result}")
    return result

# 文件路径打印
import os
print("当前工作目录:", os.getcwd())

# 时间戳打印
import datetime
current_time = datetime.datetime.now()
print(f"当前时间: {current_time}")
print(f"格式化时间: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

# 数据类型打印
data = [1, "hello", 3.14, True]
for item in data:
    print(f"值: {item}, 类型: {type(item)}")

# 异常处理中的打印
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"错误发生: {e}")

# 进度显示打印
import time
print("处理中", end="")
for i in range(5):
    print(".", end="", flush=True)
    time.sleep(0.5)
print(" 完成!")

# 美化输出
print("="*50)
print("系统信息".center(50))
print("="*50)
print(f"Python 版本: 3.x")
print(f"操作系统: Windows/Linux/Mac")
print("="*50)
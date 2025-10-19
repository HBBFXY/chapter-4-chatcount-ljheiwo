# 从键盘获取输入的一行字符
input_str = input("请输入一行字符：")

# 初始化各类型字符的计数变量
letter_count = 0  # 英文字符计数
digit_count = 0   # 数字计数
space_count = 0   # 空格计数
other_count = 0   # 其他字符计数

# 遍历输入的每个字符
for char in input_str:
    if char.isalpha():  # 判断是否为英文字符（字母）
        letter_count += 1
    elif char.isdigit():  # 判断是否为数字
        digit_count += 1
    elif char.isspace():  # 判断是否为空格
        space_count += 1
    else:  # 其他情况则为其他字符
        other_count += 1

# 按照要求格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
# 这个文件用于编写代码

# 删除字符
# 如 'I am a student' 删除 'abcdefg'里面的任意的字符

a = 'I am a student'
b = 'abcdefg'
res = ''
for i in a:
    if (i not in b):  # 关键字 in 表示 检查字符串是否包含指定的字符串
        res += i
print(res)

# 方法二
a = 'I am a student'
b = 'abcdefg'
for i in b:
    a = a.replace(i, '')
print(a)

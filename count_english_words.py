# 计算一个文件中英文单词的数目

f = open('test.txt')
lines = f.readlines()
# print(lines)
count = {}
for line in lines:
    words = line.strip().split(' ')
    # print(words)
    for word in words:
        if word not in count:
            count[word] = 0
        count[word] += 1

for key in count:
    print(key, count[key])

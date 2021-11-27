import re
import copy


输入文件名 = 'text4split.txt'
with open(输入文件名, 'r', encoding='utf-8') as f:
    文本 = f.read()

分段列表 = []
分段列表 = re.split('\n\n', 文本)

分句列表 = []
for 段 in 分段列表:
    句分割 = re.split('([\.|\?|;|:])', 段)
    句分割 = ["".join(i).strip() for i in zip(句分割[0::2],句分割[1::2])]
    分句列表.append(句分割)

复制分句列表 = copy.deepcopy(分句列表)

for i in range(len(分句列表)):
    for j in range(len(分句列表[i])):
        词分割 = re.split(' ', 分句列表[i][j])
        复制分句列表[i][j] = 词分割
print(复制分句列表)

输出文件 = 'wordList.txt'
with open(输出文件, 'w') as f:
    f.write(str(复制分句列表))

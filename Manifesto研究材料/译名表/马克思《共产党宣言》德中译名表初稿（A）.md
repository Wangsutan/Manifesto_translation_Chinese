# 马克思《共产党宣言》德中译名表初稿（A）

我筛选译名表候选词的代码如下（Jupyter Notebook中的，已更新排序方法，以无视首字母大小写）：

```python
import re


inputFile = r"Manifest_der_Kommunistischen_Partei.md"
with open(inputFile, "r", encoding='utf-8') as f:
    text = f.read()
# print(text)
```


```python
pattern = u"\[[[0-9a-zA-Z].*]\(.*\)"
result = re.sub(pattern, "", text)
print(result)
```


```python
from nltk import word_tokenize
import string
```


```python
tokens = []
for token in word_tokenize(result):
    if token not in string.punctuation:
        tokens.append(token)

text_tokens = [token for token in tokens]
# print(text_tokens)
```


```python
from nltk.corpus import stopwords
from collections import Counter  
```


```python
print(type(text_tokens))
```

```python
filtered = [w for w in text_tokens if w not in stopwords.words('german')]
print(type(filtered))
```

```python
count = Counter(filtered)
print(count)
```

```python
dicts = dict(count)
dictLen = len(dicts)
print(dictLen)
```

```python
sorted_dicts = sorted(dicts.items(), key=lambda asd: asd[0].lower(), reverse=False)
print(type(sorted_dicts))

outputFile = 'sorted_dicts_new.txt'
with open(outputFile, 'w') as f:
    f.writelines(str(sorted_dicts))
    print("\nOK, already got the dictionary!")

```

现同步将已添加汉译的初稿等内容发出来，供大家参考。今天是A：

```
略
```

2021-06-03
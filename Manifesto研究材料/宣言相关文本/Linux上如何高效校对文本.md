# Linux上如何高效校对文本——以马克思《宣言》二份版本的校对为例

我翻译马克思的《宣言》，最初用的MIA的在线德文网页版（Karl Marx u. Friedrich Engels. Manifest der Kommunistischen Partei[M/OL].https://www.marxists.org/deutsch/archiv/marx-engels/1848/manifest/index.htm, Zuletzt aktualisiert am 19 Juli 2019.），据网页上的标注，它又源自马克思、恩格斯的一个全集版（Karl Marx u. Friedrich Engels, Werke, Bd. 4, S. 459–493; Dietz Verlag Berlin, 1974.）。全文的翻译首先是依据这个网页版。然后我又参考了一份影印版（Karl Marx u. Friedrich Engels, Werke, Bd. 4, S. 459–493; Dietz Verlag Berlin, 1977.）。这一版比网页版所依据的底本还新一些。我用这个影印版初步校对了页码、分段、注释等部分。

随后，我又开始对比上述二版本之间的差别，以期完善我的版本依据及翻译质量。

昨日（2021年7月10日），开始了对比工作。当天我是人工肉眼对比的，初步完成了无标题开篇、第一章、第四章的对比、校对工作，并借此完善译稿。

但这样的人工作业方式，效率太低。今日突然发现，用Deepin自带的《文档查看器》（版本：5.9.6），切换至“选择工具”，可以复制影印版的PDF中的字符，并且准确率极高。於是我就想到：能否运用技术手段，取代无聊、低效、易错的人工作业方式。

经查，得知diff命令可以实现对比之需要。

我将MEW的影印版中的文字，主要依页面而分别复制摘取出来，粘贴到SciTE界面中，形成纯文本文件。要注意将同一段中断开的字句重新接在一起。并相应地依据这样复制出来的字符，从此前保留的一份MIA的德文文字版中，取出相应的字符。要注意删掉多余的空格，以便更好地逐字符地对比。这样主要是在满足人眼之需要，而不是diff之需要。在处理二份文本时，都要注意处理好注释的问题。删掉注释，之后在我所处理的德文全文整理稿中，再加上。网页版中残留的HTML格式标记，能帮助整理者更好地定位各种注释所在的位置。

随后，用diff查看此二份文件存在什么样的区别。以MEW的文本为标准，确定异文，在此过程中，不断地统一此二份文本，然后重复使用diff查找区别，直至没有区别。同时，进一步完善译文。

相应命令及其结果，例如：

```
wst@wst-PC:~/Desktop$ diff mew_2.txt mia_2.txt -Bw
6c6
< Sie unterläßt aber keinen Augenblick, bei den Arbeitern ein möglichst klares Bewußtsein über den feindlichen Gegensatz zwischen Bourgeoisie und Proletariat herauszuarbeiten, damit die deutschen Arbeiter sogleich die gesellschaftlichen und politischen Bedingungen, welche die Bourgeoisie mit ihrer Herrschaft herbeiführen muß, als ebenso viele Waffen gegen die Bourgeoisie kehren können, damit, nach dem Sturz der reaktionäien Klassen in Deutschland, sofort der Kampf gegen die Bourgeoisie selbst beginnt. 
---
> Sie unterläßt aber keinen Augenblick, bei den Arbeitern ein möglichst klares Bewußtsein über den feindlichen Gegensatz zwischen Bourgeoisie und Proletariat herauszuarbeiten, damit die deutschen Arbeiter sogleich die gesellschaftlichen und politischen Bedingungen, welche die Bourgeoisie mit ihrer Herrschaft herbeiführen muß, als ebenso viele Waffen gegen die Bourgeoisie kehren können, damit, nach dem Sturz der reaktionären Klassen in Deutschland, sofort der Kampf gegen die Bourgeoisie selbst beginnt.
wst@wst-PC:~/Desktop$ diff mew_2.txt mia_2.txt -Bw
```

从上述运行结果看，有一段有区别，区别在於：从影印版复制而来的文本中出现了差错“reaktionäien”。但是经修改之后，再用diff重查，就没有区别了。若同时（如有必要）完善了相应的德文整理稿篇幅，并（如有必要）完善了相应的译稿，那么就算结束了相应篇幅的校对工作。

运用本文所说的各种技术手段，能大幅提高校对整理的效率。毕竟，优秀的程序员讨厌低效、重复。

我还录下了一段这样的校对过程，供大家参考。

---

在整理校对过程中，发现MIA版本中有一些比较明显的异文，在语法和逻辑上也成立。但我这次不想专门把这些地方也标注出来。我目前只满足於以MEW（1977年版）为底本。

按理说，MIA所依据的文献，同MEW影印版这一文献，是由同一出版社所出版的一系列的东西，而且相距仅有约3年。为何会出现这么些相对於1977年影印版的重大异文？这些异文是来自1974年MEW底本，还是来自整理过程等等？另外，若这些异文果有其依据，那么究竟该如何确定采取什么样的异文为原本？进一步问：异文又出现在马克思或恩格斯所负责的哪些版本中呢？现在当然没法搞明白这些问题。
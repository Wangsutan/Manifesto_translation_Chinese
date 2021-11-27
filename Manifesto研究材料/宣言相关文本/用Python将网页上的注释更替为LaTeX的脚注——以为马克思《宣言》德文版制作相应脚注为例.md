# 用Python将网页上的注释更替为LaTeX的脚注——以为马克思《宣言》德文版制作相应脚注为例

目前，我打算专门制作一份德文版《宣言》的纯文本文件，并采用\LaTeX 的各种标记语言。

我已经初步实现了用Python自动从网页文件重新制作\LaTeX 的脚注。

代码如下：

```

```

这里处理的文件，是从德文版的马克思主义文库下载相应网页后，再复制到纯文本文件中，不是直接用网页文件。

用列表保存文件名，以提高代码灵活性，方便日后整合各章。这里暂只用第一章的德文文本。

代码中大量使用了正则表达式，确实比较复杂，要多多注意。比如，我为注释增添相应的脚注标注`\footnote{.*}`时，发现会识别为换页`\f`，应专门调整为`r"\\footnote{%s}" % note" `

运行结果如下（部分，系代码所处理的文本之末段）：

```
Die wesentliche \footnote{39. 1848, 1872, 1883: wesentlichste} Bedingung für die Existenz und für die Herrschaft der Bourgeoisklasse ist die Anhäufung des Reichtums in den Händen von Privaten, die Bildung und Vermehrung des Kapitals; die Bedingung des Kapitals ist die Lohnarbeit. Die Lohnarbeit beruht ausschließlich auf der Konkurrenz der Arbeiter unter sich. Der Fortschritt der Industrie, dessen willenloser und widerstandsloser Träger die Bourgeoisie ist, setzt an die Stelle der Isolierung der Arbeiter durch die Konkurrenz ihre revolutionäre Vereinigung durch die Assoziation. Mit der Entwicklung der großen Industrie wird also unter den Füßen der Bourgeoisie die Grundlage selbst hinweggezogen \footnote{40. 1848, 1872: weggezogen}, worauf sie produziert und die Produkte sich aneignet. Sie produziert vor allem ihren \footnote{41. 1848, 1872: ihre} eigenen Totengräber. Ihr Untergang und der Sieg des Proletariats sind gleich unvermeidlich.
```

原来正文中只是中括号里加上注释的数字，现在替换成了注释本身。

当然，代码还需要优化。这里是先放出来，供大家参考。

2021-6-27
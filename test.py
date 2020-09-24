import MeCab
m = MeCab.Tagger()
a = m.parse("오늘은 좋은날, 행복한 삶을 누리자.")
print(a)

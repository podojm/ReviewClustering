from konlpy.tag import Hannanum
hannanum = Hannanum()
print(hannanum.analyze(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
print("\n")

# 은전한닙 프로젝트
from konlpy.tag import Mecab
mecab = Mecab()

print(mecab.pos(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))


from konlpy.tag import Twitter
twitter = Twitter()
print(twitter.pos(u'다맘에들어요 다다다다다!!!!!!길이감도 좋고 핏도 좋고 배송도 빠르고 기분너무좋아요ㅋㅋㅋ감사합니당'))
print(twitter.pos(u'다맘에들어요 다다다다다!!!!!!길이감도 좋고 핏도 좋고 배송도 빠르고 기분너무좋아요ㅋㅋㅋ감사합니당',  True, True))


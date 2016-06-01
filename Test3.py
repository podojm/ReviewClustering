import konlpy
import nltk
from konlpy.tag import Twitter
#stremmer를 형용사,동사에 붙여보자!!


twitter = Twitter()
# POS tag a sentence

# 문장단위로 끊어서 해봐!

#sentence = u'좋은 사과'
#sentence = u'다맘에들어요 다다다다다!!!!!!길이감도 좋고 핏도 좋고 배송도 빠르고 기분너무좋아요ㅋㅋㅋ감사합니당'
#sentence = u'이 제품 가격대비완전좋아요^^~화질 좋고~~음향좋고~~^^.배송은 아주 만족스럽습니다~~^^'
sentence = u'배송이 엄청빠르네요ㅎㅎ후기에서 결점이 있다고하던데..무결점으로 주문해서 그런지 결점이 하나도없네요ㅎㅎ가성비는 전 브랜드를 통합해서 최고인거같네요ㅎㅎ추천합니다.'
#sentence = '양말이생각보다퀄리티도좋고~~그림도너무이쁘네요~~~다음에또사야겟어요~~잘신겠습니다~~~~'



#sentence = '좋네요 번창하세여'
# '만족합니다'
#sentence = '금요일 오전 주문에 토요일 오전 배송도착 \r\n불량화소가 대충 몇개 있긴하지만 충분히 감안하고 쓸만합니다'
#sentence = '아주마음에들어요'
#sentence = '너무맘에들어요 ㅎㅂㅎ!!'
# '잘 받았어요~ 잘 신을게요^♡^'

#sentence = '양말싸게잘산듯'
# '싼 가격에 잘샀네요~'
# '양말  싸게 잘 구입한것 같습니딘ㅎㅎ'


# '아주 만족합니다! 적극적으로 추천합니다 '
# '만족합니다~~'
# '잘받앗어여 ~'
#sentence = '저렴하게 잘 샀어요'
# '잘받았습니다 '
# '잘받았습니다 제품 만족합니다!'
# '대박 상품!!'
# '모두 맘에 쏙들어요^^'
# '고맙릅니다'
# '양말 자체는 에쁜데.. 두번 신으니깐 빵꾸나요 ㅋㅋㅋㅋ'
# '아직못받앗는데요ㅜㅜ'

# '괜챦아요!!'
# '싼가격에 잘샀어요'
# '양말이 거기서 거기지 뭔 후기를 쓰래 ㅡ ㅡ'
# '잘신을께요'
# '마음에 들어요'
# '굿ㅋㅋㅋㅈㅋ'
# '색상 디자인 만족합니다요~~'
# '완전 마음에 들어요/뿌뜻 ㅋㅋ'
# '잘신을게영 ㅎㅎㅎ'
# '양말 품질 만족합니다'
# '만족합니다'
# '네.잘받았습니다 .'

# '잘받았어요'


#words = konlpy.tag.Twitter().pos(sentence) #품사태깅
words = twitter.pos(sentence, False, True);
print(words)
print("\n")


file =open("/Users/lunjm/PycharmProjects/ReviewClustering/dic/Noun/ShoppingNoun.txt")
nounDic = {}
score = file.readline()
for x in file:
    x = x.replace('\n', '')
    nounDic[x] = score

file.close()

print(nounDic.keys())
# print(nounDic.count())


print(nounDic.get('양말'))





# Define a chunk grammar, or chunking rules, then chunk
grammar = """
NP: {<N.*>*<Suffix>?}   # Noun phrase
ADV: {<Adv.*>*}
ADJ: {<Adj.*>*}            # Adjective phrase
"""
parser = nltk.RegexpParser(grammar) #grammer 별로 구분

chunks = parser.parse(words) #구문분석
print("# Print whole tree")
print(chunks.pprint())

purchaseReview = []
beforeLabel = ""
beforeWord = ""
temp = ""
print("\n# Print Noun, Adjective phrases only")
for subtree in chunks.subtrees():
    if subtree.label() == 'NP' :
        temp = ''.join(e[0] for e in list(subtree))
        if len(temp) != 0 :
            beforeLabel = 'NP'
            beforeWord = temp
        print("명사", ''.join(e[0] for e in list(subtree))),
    elif subtree.label() == 'APJ' :
        word = ''.join(e[0] for e in list(subtree))
        if len(temp) != 0 and (beforeLabel == 'NP') :
            purchaseReview.append(beforeWord +' '+ word)
        else :
            purchaseReview.append(word)
        beforeLabel = 'AP'
        before = word
        print("형용사", ''.join((e[0] for e in list(subtree))))
        # print(subtree.pprint())

print(purchaseReview)
# Display the chunk tree
#chunks.draw()

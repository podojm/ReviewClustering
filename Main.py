import Model
import NLP
import operator
from collections import OrderedDict

class RurchaseReview :

    @staticmethod
    def replace_all(text, dic) :
        for i, j in dic.items():
            text = text.replace(i, j)
        return text


#패션양말 285975213, 지역딜 305051958, 슈퍼마트 187600137, 모니터 - 267120649
#세제 - 267299457, #외장하드 - 269272529, 텐트 - 183424165, 교육 - 252096529, 패션가방 - 285475713
#팔찌 - 172124033, #노트북 - 272747233, #차량용 방향제 - 304648642, #강아지용품 - 264534073, #신발 - 318001914



daoReview = Model.review();
data = daoReview.getReview(285975213);
nlp = NLP.NLPProcessing;

reps = {'(':'', ')':'', ',':'', "'":'', '\r\n\r\n':'', '\r\n':''}

totalReview = {}

for row in data:

    sentence = format(row)
    sentence = RurchaseReview.replace_all(sentence, reps)
    print(sentence)
    words = nlp.posTagging(sentence)
    print(words)
    chunks = nlp.makeParseTree(words)
    purchaseReview = nlp.getPurchaseReview(chunks)
    print(purchaseReview)
    if len(purchaseReview) != 0 :
        for review in purchaseReview :
            if (len(review) != 1) :
                if (review in totalReview.keys()) :
                    totalReview[review] += 1
                else :
                    totalReview[review] = 1

sortedData = OrderedDict(sorted(totalReview.items(), key = lambda x:x[1]))

for i, j in sortedData.items() :
     print(i, ',', j)


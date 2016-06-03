from dao import DAO
from nlp import NLP
from util import BeforeProcessing
from util import FileReader
from util import API
from collections import OrderedDict


#스코어링 & 새로운 패턴추가 매소드 2
class PurchaseReview :

    # 패션양말 285975213, 지역딜 305051958, 슈퍼마트 187600137, 모니터 - 267120649
    # 세제 - 267299457, #외장하드 - 269272529, 텐트 - 183424165, 교육 - 252096529, 패션가방 - 285475713
    # 팔찌 - 172124033, #노트북 - 272747233, #차량용 방향제 - 304648642, #강아지용품 - 264534073, #신발 - 318001914
    # 원피스 - 317711958, 307410130

    daoReview = DAO.Review
    nlp = NLP.NLPProcessing
    bP = BeforeProcessing.BeforeProcessing
    api = API.API

    adjDic = FileReader.fileReader.getDicData('Adj')
    advDic = FileReader.fileReader.getDicData('Adv')
    nounDic = FileReader.fileReader.getDicData('Noun')
    # negaAdjDic = FileReader.fileReader.getDicData('NegativeAdj')


    reviewResult = {}
    data = daoReview.getReview(223487501)
    for row in data:
        sentence = format(row)
        # print(sentence)
        sentence = bP.pruningSentence(sentence)
        print(sentence)
        words = nlp.posTagging(sentence)
        print(words)
        #chunks = nlp.makeParseTree(words) #기존 패턴
        chunks = nlp.makeParseTree2(words)
        # print(chunks)

        #purchaseReview = api.getPurchaseReview(chunks, adjDic, advDic, nonDic, negaAdjDic) #기존 패턴
        purchaseReview = api.getPurchaseReview2(chunks, adjDic, advDic, nounDic)
        for data in purchaseReview:
            if data in reviewResult.keys() :
                count = reviewResult[data][1] + 1
                reviewResult[data] = [purchaseReview[data], count]
            else :
                reviewResult[data] = [purchaseReview[data], 1]



    # sortedData = OrderedDict(sorted(reviewResult.items(), key=lambda x: x[1]))

    # for i, j in sortedData.items():
    #      print(i, ',', j[0], ',', j[1])

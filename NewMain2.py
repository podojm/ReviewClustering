from dao import DAO
from nlp import NLP
from util import BeforeProcessing
from util import FileReader
from util import API
from collections import OrderedDict

#스코어링 + 새로운 패턴(태깅까지만 하고 형용사 중심으로 앞, 뒤 조사)
class PurchaseReview :

    # 패션양말 285975213, 지역딜 305051958, 슈퍼마트 187600137, 모니터 - 267120649
    # 세제 - 267299457, #외장하드 - 269272529, 텐트 - 183424165, 교육 - 252096529, 패션가방 - 285475713
    # 팔찌 - 172124033, #노트북 - 272747233, #차량용 방향제 - 304648642, #강아지용품 - 264534073, #신발 - 318001914

    daoReview = DAO.Review
    nlp = NLP.NLPProcessing
    bP = BeforeProcessing.BeforeProcessing
    api = API.API

    adjDic = FileReader.fileReader.getDicData('Adj')
    advDic = FileReader.fileReader.getDicData('Adv')
    nounDic = FileReader.fileReader.getDicData('Noun')

    reviewResult = {}
    data = daoReview.getReview(285975213)
    for row in data:
        sentence = format(row)
        sentence = bP.pruningSentence(sentence)
        # print(sentence)
        words = nlp.posTagging(sentence)
        # print(words)
        chunks = []
        for word, pos in words:
            if pos == 'Noun' or pos == 'Adjective' or pos == 'Adverb' or pos =='Verb':
                oneInfo = {}
                oneInfo[pos] = word
                chunks.append(oneInfo)




        reviewResult = {}
        candidateList = []
        startIndex = 0
        for index, chunk in enumerate(chunks) :
            if chunk.get('Adjective') or chunk.get('Verb') :
                endIndex = index+1
                oneReview = '';
                for index in range(startIndex, endIndex) :
                    for word in list(chunks[index].values()):
                        oneReview += word + " "
                candidateList.append(oneReview)
                startIndex = endIndex


        for oneReview in candidateList:
            print(oneReview)
        # for candidate in candidateList:
        #     for word in candidate:
        #         listWord = list(word.values())
        #         for word in listWord :
        #             print(word, end = " ")
        #     print()


        # chunks = nlp.makeParseTree(words)
        # print(chunks)

    #     purchaseReview = api.getPurchaseReview(chunks, adjDic, advDic, nounDic, negaAdjDic)
    #     for data in purchaseReview:
    #         reviewResult[data] = purchaseReview[data]
    #
    # sortedData = OrderedDict(sorted(reviewResult.items(), key=lambda x: x[1]))
    #
    # for i, j in sortedData.items():
    #     print(i, ',', j)

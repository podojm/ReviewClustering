from nlp import NLP
from util import BeforeProcessing

#TODO getPurchaseReview1~2 별로 공통 부분 추출 및 리팩토링 필요
class API:

    def getScoring(word, dic):
        nlp = NLP.NLPProcessing
        ngramList =nlp.getNgramList(word)

        score = 0
        for gram in ngramList:
            if dic.get(gram) != None:
                score += dic.get(gram)

        return score


    # return - 명사 사전에 매칭된 단어들의 인덱스
    def getWordIndex(sentence, dic):
        bP = BeforeProcessing.BeforeProcessing
        nlp = NLP.NLPProcessing

        nounIndexList = {}
        splitedSentence = bP.splitSentenceWithList(sentence)
        print('잘려진 문장 : ', splitedSentence)
        for index, word in enumerate(splitedSentence) :
            ngramList = nlp.getNgramList(word)
            for gram in ngramList:
                if dic.get(gram) != None:
                    nounIndexList[index] = gram
        return nounIndexList




    # getPurchaseReview   NewMain   Scoring
    def getPurchaseReview(chunks, adjDic, advDic, nounDic, negaAdjDic):

        purchaseReviews = {}
        beforeLabel = ""
        beforeWord = ""
        beforeScore = 0;
        temp = ""

        for subtree in chunks.subtrees():
            if subtree.label() == 'NP':
                word = ''.join(e[0] for e in list(subtree))
                if len(word) != 0:
                    beforeLabel = 'NP'
                    beforeWord = word
                    beforeScore = API.getScoring(word, nounDic)
                    beforeScore += API.getScoring(word, advDic)
                    # print("명사", ''.join(e[0] for e in list(subtree))),
            elif subtree.label() == 'AP':
                word = ''.join(e[0] for e in list(subtree))
                if (word != 'r'):
                    if len(word) != 0 and beforeLabel == 'NP':
                        score = 0
                        score += API.getScoring(word, adjDic)
                        score += API.getScoring(word, negaAdjDic)

                        purchaseReview = beforeWord + ' ' + word
                        purchaseReviews[purchaseReview] = score + beforeScore
                    else:
                        score = 0
                        score += API.getScoring(word, adjDic)
                        score += API.getScoring(word, advDic)
                        score += API.getScoring(word, negaAdjDic)

                        purchaseReview = word
                        purchaseReviews[purchaseReview] = score + beforeScore

                beforeLabel = 'AP'
                before = word

        return purchaseReviews


    # getPurchaseReview  NewMain 새로운 로직 뽑는거
    def  getPurchaseReview2(chunks, adjDic, advDic, nounDic):

        purchaseReviews = {}
        beforeLabel = ""
        beforeWord = ""
        beforeScore = 0;

        for subtree in chunks.subtrees():
            if subtree.label() == 'NP':
                word = ''.join(e[0] for e in list(subtree))
                if len(word) != 0:
                    beforeLabel = 'NP'
                    beforeWord = word
                    beforeScore = API.getScoring(word, nounDic)
                    beforeScore += API.getScoring(word, advDic)
                    # print("명사", ''.join(e[0] for e in list(subtree))),
            elif subtree.label() == 'ADV':
                word = ''.join(e[0] for e in list(subtree))
                if len(word) != 0 and beforeLabel == 'NP':
                    beforeScore += API.getScoring(word, advDic)
                    beforeWord = beforeWord + ' ' + word
            elif subtree.label() == 'ADJ':
                word = ''.join(e[0] for e in list(subtree))
                if (word != 'r'):
                    if len(word) != 0 and beforeLabel == 'NP':
                        score = 0
                        score += API.getScoring(word, adjDic)
                        # score += API.getScoring(word, negaAdjDic)

                        purchaseReview = beforeWord + ' ' + word
                        purchaseReviews[purchaseReview] = score + beforeScore
                    else:
                        score = 0
                        score += API.getScoring(word, adjDic)
                        # score += API.getScoring(word, negaAdjDic)

                        purchaseReview = word

                        purchaseReviews[purchaseReview] = score
                beforeLabel = 'AP'
                before = word
                # print("형용사", ''.join((e[0] for e in list(subtree))))

        return purchaseReviews

    def getPurchaseReview3(candidateList, adjDic, advDic, nounDic):

        result = {}
        for candidate in candidateList:
            review = ''
            score = 0
            for part in candidate:
                for pos, word in part.items():
                    review += word + " "
                    if pos == 'Noun' :
                        score += API.getScoring(word, nounDic)
                        score += API.getScoring(word, advDic)
                    elif pos == 'Adjective' :
                        score += API.getScoring(word, adjDic)
                    elif pos == 'Adverb' :
                        score += API.getScoring(word, advDic)
                    elif pos == 'Verb' :
                        score += API.getScoring(word, adjDic)

            result[review] = score;

        return result


from nlp import NLP


#TODO getPurchaseReview1~3 별로 공통 부분 추출 및 리팩토링 필요
class API:

    def getScoring(word, dic):
        nlp = NLP.NLPProcessing
        ngramList =nlp.getNgramList(word)

        score = 0
        for gram in ngramList:
            if dic.get(gram) != None:
                score += dic.get(gram)

        return score

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
    def getPurchaseReview2(chunks, adjDic, advDic, nounDic):

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
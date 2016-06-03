
import nltk
from konlpy.tag import Twitter

class NLPProcessing :

    # 품사태깅 및 어근추출
    def posTagging(sentence):
        twitter = Twitter()
        words = twitter.pos(sentence, True, True);
        return words

    #구문분석
    def makeParseTree(words):
        grammar = """
        NP: {<N.*>*<Suffix>?}   # Noun phrase
        VP: {<V.*>*}            # Verb phrase
        AP: {<A.*>}            # Adjective phrase
        """
        parser = nltk.RegexpParser(grammar)  # grammer 별로 구분
        chunks = parser.parse(words)  # 구문분석ß

        return chunks

    # 구문분석
    def makeParseTree2(words):
        grammar = """
        NP: {<N.*>*<Suffix>?}   # Noun phrase
        ADJ: {<Adj.*>}            # Adjective phrase
        ADV: {<Adv.*>*}            # Adverb phrase
        """
        parser = nltk.RegexpParser(grammar)  # grammer 별로 구분
        chunks = parser.parse(words)  # 구문분석ß

        return chunks

    # Ngram
    def getNgramList(data):
        result = []
        words = data.split(' ')
        for word in words:
            wordLen = len(word)
            for n in range(wordLen):
                n += 1
                for i in range(wordLen - n + 1):
                    result.append(word[i:i + n])

        return result

    #getPurchaseReview    OldMain 버젼
    def getPurchaseReview(chunks):

        purchaseReview = []
        beforeLabel = ""
        beforeWord = ""
        temp = ""
        #print("\n# Print Noun, Adjective phrases only")
        for subtree in chunks.subtrees():
            if subtree.label() == 'NP':
                temp = ''.join(e[0] for e in list(subtree))
                if len(temp) != 0:
                    beforeLabel = 'NP'
                    beforeWord = temp
                # print("명사", ''.join(e[0] for e in list(subtree))),
            elif subtree.label() == 'AP':
                word = ''.join(e[0] for e in list(subtree))
                if (word != 'r') :
                    if len(temp) != 0 and beforeLabel == 'NP' :
                        purchaseReview.append(beforeWord + ' ' + word)
                    # else :
                    #     purchaseReview.append(word)
                beforeLabel = 'AP'
                before = word
                # print("형용사", ''.join((e[0] for e in list(subtree))))

        return purchaseReview








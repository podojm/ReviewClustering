class BeforeProcessing:

    def pruningSentence(sentence):

        #TODO 제거하는 패턴 다시 확인하기
        pruningPattern = {'(': '', ')': '', ',': '', '\"':'', "\'": '', '/':'', '\n':'', '\r':''}

        for i, j in pruningPattern.items():
            sentence = sentence.replace(i, j)

        return sentence

    #단어별로 띄어쓰기
    def splitSentenceWithList(sentence):

        result = []
        for word in sentence.split():
            result.append(word)

        return result
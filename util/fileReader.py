import os
class fileReader :
    def getDicData(path):

        COMMON_FILE_PATH = "/Users/lunjm/PycharmProjects/ReviewClustering/dic/"

        fileNames = []
        for root, dirs, files in os.walk(COMMON_FILE_PATH + path):
            for file in files:
                fileNames.append(file)

        dic = {}
        for fileName in fileNames:
            file = open(COMMON_FILE_PATH + path + "/" + fileName)
            score = int(file.readline())
            for x in file:
                x = x.replace('\n', '')
                dic[x] = score

        file.close()
        return dic
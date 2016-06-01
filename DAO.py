import pymysql

class review :

    def getReview(self, mainDealSrl) :
        connection = pymysql.connect(host='devdb.tmonc.net',
                                     port=3306,
                                     user='TM_DDL2_COMUSER',
                                     password='TM_DDL2_COMUSER1234!!',
                                     charset='utf8mb4')
        sql = "SELECT contents FROM ticketmonster.review WHERE main_deal_srl = {}".format(mainDealSrl)

        cur = connection.cursor()
        cur.execute(sql)

        connection.close()
        return cur



from tools.Tools import *


class Stock:
    def __init__(self, calculateAmount, calculateUnit, lotUnit, stockCode, stockId, roundUp = True):
        self.calculateAmount = calculateAmount
        self.calculateUnit = calculateUnit
        self.lotUnit = lotUnit
        self.roundUp = roundUp

        self.stockCode = stockCode
        self.stockId = stockId
        self.tid = 0
        self.assetMargin = 0
        self.isMarginIpo = 1

    def generate_request_data(self, lots):
        if self.roundUp:
            buy2Decimal = round_decimals_up(self.calculateAmount * lots / self.calculateUnit, 2)
        else:
            buy2Decimal = round(self.calculateAmount * lots / self.calculateUnit, 2)
        buyAmount = int(buy2Decimal * 1000)
        cashPart = int(round_decimals_up(buy2Decimal / 10, 2) * 1000)
        resultData = {
            "stockCode": self.stockCode,
            "stockId": self.stockId,
            "buyAmount": buyAmount,
            "buyCount": lots * self.lotUnit,
            "cashPart": cashPart,
            "tid": 0,
            "assetMargin": 0,
            "isMarginIpo": 1,
        }
        # print(str(resultData))
        return resultData


Bairongyun = Stock(160602243.0, 10000, 500, "06608", 1515)

Meijiayin = Stock(2727207.9, 1000, 2000, "06939", 1512)

Baidu = Stock(148986357.5, 10000, 50, "09888", 1510)

Qichezhijia = Stock(254337388.6, 10000, 100, "02158", 1509)

Guanglian = Stock(6818019.75, 2500, 5000, "01413", 1505)

Jiujiuwang = Stock(3787788.75, 1000, 5000, "01927", 1506)

Sensong = Stock(39595018.40, 10000, 1000, "02155", 1507)

Zhaoyun = Stock(46463542.00, 10000, 500, "06601", 1508, False)

Saishengyaoye = Stock(94947238.00, 10000, 500, "06600", 1504, False)

Zhaoyanxinyao = Stock(152521627.00, 10000, 500, "06127", 1503)

requestBody = {
    "stockCode": "01024",
    "stockId": 1497,
    "buyAmount": 232317710,
    "buyCount": 2000,
    "cashPart": 23231780,
    "tid": 0,
    "assetMargin": 0,
    "isMarginIpo": 1,
}

requestBodyXinTong = {
    "accountId": 17448263,
    "assetMargin": 0,
    "buyAmount": 246458790,
    "buyCount": 20000,
    "isMarginIpo": 1,
    "cashPart": 24645880,
    "stockId": 1498,
    "tid": 0,
    "password": "db2c098d411a0bca565c3946e805ed93",
    "stockCode": "02160",
    "csrf": "H26OjNGYEtG4TzQcv0H3ng==-+rWRittDf2CRu2oeHSgiSb+c68A=",
    "r_token": "sf2dyKj6nIkP2to/d2xLRFWj6GY="
}

requestBodyBeikang = {
    "accountId": 17448263,
    "assetMargin": 0,
    "buyAmount": 13817850,
    "buyCount": 500,
    "isMarginIpo": 1,
    "cashPart": 1381790,
    "stockId": 1500,
    "tid": 0,
    "password": "db2c098d411a0bca565c3946e805ed93",
    "stockCode": "02170",
    "csrf": "H26OjNGYEtG4TzQcv0H3ng==-+rWRittDf2CRu2oeHSgiSb+c68A=",
    "r_token": "sf2dyKj6nIkP2to/d2xLRFWj6GY="
}

requestBodyNuohui = {
    "accountId": 17448263,
    "assetMargin": 0,
    "buyAmount": 161571920,
    "buyCount": 6000,
    "isMarginIpo": 1,
    "cashPart": 16157200,
    "stockId": 1502,
    "tid": 0,
    "password": "db2c098d411a0bca565c3946e805ed93",
    "stockCode": "06606",
    "csrf": "H26OjNGYEtG4TzQcv0H3ng==-+rWRittDf2CRu2oeHSgiSb+c68A=",
    "r_token": "sf2dyKj6nIkP2to/d2xLRFWj6GY="
}
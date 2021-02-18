from .settings.User import *
from .settings.Stocks import *
from .futurequests.ApplyIpoRequest import *
from .futurequests.ApplyDetailsRequest import ApplyDetailsRequest

current_user = LiXiaoQing
apply_stock = Zhaoyanxinyao


def start_process():
    while True:
        message = start_request()
        if "额度不足" in str(message):
            pass
        elif "已申购过" in str(message):
            print("Already applied! duplicated")
            break
        else:
            print("Finally got it!")
            break


def start_request():

    details_response = ApplyDetailsRequest(current_user, apply_stock).start()
    print("ApplyDetailsRequest --- response = " + str(details_response))

    apply_response = ApplyIpoRequest(current_user, apply_stock).start()
    print("ApplyIpoRequest --- response = " + str(apply_response))
    message = apply_response['message']
    return message

from .settings.User import *
from .settings.Stocks import *
from .futurequests.ApplyIpoRequest import *
from .futurequests.ApplyDetailsRequest import ApplyDetailsRequest
import threading

# current_user = [Zhaojing, Fanbin, Lixue, LiangDong, LiXiaoQing]
current_user = [LiXiaoQing]
apply_stock = Saishengyaoye


def start_process():
    thread_array = []
    for user in current_user:
        thread = threading.Thread(target=start_thread,
                         args=(user,))
        thread.start()
        thread_array.append(thread)

    for thread in thread_array:
        thread.join()
    do_on_finish()


def start_thread(user):
    while True:
        message = start_request(user)
        if "额度不足" in str(message):
            pass
        elif "已申购过" in str(message):
            print(user.name + "Already applied! duplicated")
            break
        else:
            print(user.name + "Finally got it!")
            break


def start_request(user):

    details_response = ApplyDetailsRequest(user, apply_stock).start()
    print(str(user.name) + "ApplyDetailsRequest --- response = " + str(type(details_response)))

    apply_response = ApplyIpoRequest(user, apply_stock).start()
    print("ApplyIpoRequest --- response = " + str(apply_response))
    message = apply_response['message']
    user.result_message = message
    return message

def do_on_finish():
    print("result -------------------------------------- ")
    for user in current_user:
        print(user.name + " = " + user.result_message)
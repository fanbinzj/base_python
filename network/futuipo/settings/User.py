
class User:
    def __init__(self, name, cookie, account_id, password, r_token, csrf="", apply_lots = 1):
        self.name = name
        self.cookie = cookie
        self.account_id = account_id
        self.password = password
        self.r_token = r_token
        self.csrf = csrf
        self.apply_lots = apply_lots
        self.result_message = ""


CookieZj = "futu-csrf=NutWpgsyk8p9IOOm/+M9ejLij74=; tgw_l7_route=b4566513c2529d8fe89aaa84feaae1a6; cipher_device_id=1616125808978712; device_id=135dafa90bbdb23d; locale=zh-cn; main_brokers=ewogICJtYWluX2Jyb2tlcnMiIDogWwogICAgMSwKICAgIDIKICBdCn0=; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22178489acf2a54f-04049bafa-76171b18-181760-178489acf2bed%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22178489acf2a54f-04049bafa-76171b18-181760-178489acf2bed%22%7D; uid=17448263; user_attribution=1; web_sig=PLN9nf%2BmuZVcmT5O9LQSpbXzl06kL2%2FBM%2BzaSAcxlvrG67xDl%2FJgp5W7%2Bd8yErnW66XkRr5aAR39E2z9R%2FM3JwjxLnhp2pOtZNQRNrZ8QiU%3D"

Zhaojing = User("Zhaojing", CookieZj, 17448263, "db2c098d411a0bca565c3946e805ed93", "sf2dyKj6nIkP2to/d2xLRFWj6GY=",
                "Sp/HvsqXicWyPcLMVOEOqQ==-UD1nBo9WX6kynSvQieg2cU1TPec=")

CookieFB = "futu-csrf=VQi5H4Hxh/yd4pohFgkySmJk8fk=; tgw_l7_route=e1cf5f455bf3a97480a66b829cc4a35a; cipher_device_id=1616125723186959; device_id=135dafa90bbdb23d; locale=zh-cn; main_brokers=ewogICJtYWluX2Jyb2tlcnMiIDogWwogICAgMSwKICAgIDIKICBdCn0=; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221784899857229a-062ea4d13-76141b18-181760-17848998574664%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221784899857229a-062ea4d13-76141b18-181760-17848998574664%22%7D; uid=11256759; user_attribution=1; web_sig=tvGlyIhtoENcslDj2RCc9Z4iQyNkrLtNIbC4%2B3WvHJK2%2FLrhT4%2BBRKRi2hkhK8%2FOfqXzJLFyLUkshsuZ4iry6g%2BX0gIHe8GdJEch%2F85ZVvI%3D"

Fanbin = User("Fanbin", CookieFB, 11256759, "db2c098d411a0bca565c3946e805ed93", "JwGorD/T8BwCJhIAVemm7+Xl2t0=",
              "QfVOEcdzzgbSphswu/0GmA==-llvLKZI2EMW8qNT7ljedMsJkWPE=")

CookieLX = "futu-csrf=eeikRMYaSdhn/gL5LODRqsCSjkU=; tgw_l7_route=e1cf5f455bf3a97480a66b829cc4a35a; cipher_device_id=1616125599111590; device_id=135dafa90bbdb23d; locale=zh-cn; main_brokers=ewogICJtYWluX2Jyb2tlcnMiIDogWwogICAgMSwKICAgIDIKICBdCn0=; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221784897a101fc-0f8299f48-653a5568-181760-1784897a1021c%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221784897a101fc-0f8299f48-653a5568-181760-1784897a1021c%22%7D; uid=17782642; user_attribution=1; web_sig=ub4cMlbivgxjDrN57niRFE81lUz%2B%2Fcm8c79EunaDd49sd%2BtVZSrjy3x0ARK8EUChiONkhdJktCKNfZgoyt4C6ouj02tW6b0uXTQVmByJvd0%3D"

Lixue = User("Lixue", CookieLX, 17782642, "db2c098d411a0bca565c3946e805ed93", "CTz5EwkBXeHuCotvnMtK0qRzgRo=",
             "IsiQbT2pt5kC7gHcyCDS5A==-arz56a0TBFpp7eVVKKzOZgtFIGU=")

CookieLD = "futu-csrf=UE9QyyoupKFyy1KNq5yronbiJM8=; tgw_l7_route=6ea9211773138bacbfa1506ee9f918a2; cipher_device_id=1616109318937148; device_id=135dafa90bbdb23d; locale=zh-cn; main_brokers=ewogICJtYWluX2Jyb2tlcnMiIDogWwogICAgMSwKICAgIDIKICBdCn0=; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv1Rgsi%2Fui11GO%2FNnZemf4FR3hmbDu8KKDXETUnZY0XMBjyNIJHs1ylMVV898%2BgisvP%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22178479f327a3a6-07a078774-76171b18-181760-178479f327c499%22%7D; uid=17318381; user_attribution=1; web_sig=HbSBOdQgwkUdMKGyeDUB3vnWq64ktkxM%2BQm4yGNPhGB4WM7UZeqCgXFD%2B4C0z5NYsOCSEQgeBDFc3GqbC%2FVZIwz7tjd4YWlAJ9j9BPOgqmY%3D"
LiangDong = User("LiangDong", CookieLD, 17318381, "db2c098d411a0bca565c3946e805ed93", "95cJ4/vOML2LxKvrR5hSXGgN6Vo=",
              "OX1ulDZ1yR+1HCVUICMd5w==-iPtOhhNQXRpzc8OFqNfBeS3TvJo=")

CookieLXQ = "futu-csrf=yoL93TWxXQgMh9Rs9a2s8J6eDEw=; tgw_l7_route=976640a459854e77ec38972046609c17; cipher_device_id=1616124987733974; device_id=135dafa90bbdb23d; locale=zh-cn; main_brokers=ewogICJtYWluX2Jyb2tlcnMiIDogWwogICAgMSwKICAgIDIKICBdCn0=; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv11jQETcoCBx%2By2r2La7S4KHhmbDu8KKDXETUnZY0XMBiuYvcKlutoFILWSvNjSVgn%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22178488e47833b-0e67b7089-653a5568-181760-178488e4784e3%22%7D; uid=21263432; user_attribution=1; web_sig=GVmtVIOd%2F9kwuveNZf9CpRxplnHg8ARNFOYcB5jA%2FQrS2cQCQ9lvc7Op8TLK2Xb%2Bs1eEy85BYQvZ5VMQFLYrxCUSogd%2BnBUMn9xI7c0s%2FZw%3D"

LiXiaoQing = User("LiXiaoQing", CookieLXQ, 21263432, "db2c098d411a0bca565c3946e805ed93", "m1ri2gnVRK/fX0p1bjy/Vjoxs20=",
                  "up+VpAorifLCcSdsH4dviw==-s7rLGz1zyypbEWUdUCVBFpeKWAc=", apply_lots=1)

CookieDC = "futu-csrf=OQeMVgzRk9Lv4gKIqJP10mSMmEc=; cipher_device_id=1611800272931535; device_id=1611800272931535; sajssdk_2015_cross_new_user=1; _gcl_au=1.1.1488342976.1611819338; _fbp=fb.1.1611819354043.381292380; _gid=GA1.2.307438622.1611819364; UM_distinctid=17747ebe0d4358-03729fdd02087a-326f7006-1fa400-17747ebe0d5bab; account_side_nav_state=0%2C0%2C1%2C1%2C0%2C0%2C0%2C0%2C0; uid=11905480; web_sig=V07vJ5zI8hbalwkGFWSVkImOTm1kqQZRy%2FOCxYavj03DvXGygTwIp0v7%2B8ZYqDrmVAOwjF%2B1hD8k%2B9i4TNM55VkXOx%2FKcbTkqRl5ReQm%2BiVgHKu%2Fzk3VnC7ELCKQs%2B8f; locale=zh-cn; _uetsid=79d981b0613b11eb96bfa36d5893389a; _uetvid=79d9bbc0613b11eb8b374b336adcb675; _ga=GA1.1.1212070980.1611819364; tgw_l7_route=8f112f9488cffa9272ac4adb176127dd; _ga_K1RSSMGBHL=GS1.1.1611823928.2.1.1611823984.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv144llW1kBLnYY2pluE%2BmVZnhmbDu8KKDXETUnZY0XMBh2vuAolibsuTsUKvYZNKxc%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217746c85d48aa3-01f8f2ff09c563-326f7006-1764000-17746c85d491178%22%7D"

Dingcong = User("Dingcong", CookieDC, 11905480, "db2c098d411a0bca565c3946e805ed93", "kpnItR24tONv2EXWqddw4iMFs3c=",
                "K6YwKCg3VZiGqthCzOXF3Q==-3lmYcgtE9PE3uYpNIsK8ko4tTlg=")

CookieXX = "futu-csrf=OQeMVgzRk9Lv4gKIqJP10mSMmEc=; cipher_device_id=1611800272931535; device_id=1611800272931535; sajssdk_2015_cross_new_user=1; _gcl_au=1.1.1488342976.1611819338; _fbp=fb.1.1611819354043.381292380; _gid=GA1.2.307438622.1611819364; uid=17282401; web_sig=2TyVkbAtaQmNgcanQDn9Cv7NwQM62jti3AI8GmDv3LeGIpkZ37CrI3ddrfVTk2RfX9e%2B%2BaG%2FpQRothvz8FDKeBRVbEbsnQEW97gBOWk4jDgRC6InfIjqtc4GQl2gfASW; locale=zh-cn; UM_distinctid=17747ebe0d4358-03729fdd02087a-326f7006-1fa400-17747ebe0d5bab; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv1HoaMEGwOFtKeeCkkAUGRqHhmbDu8KKDXETUnZY0XMBhsduHfOAuHysZcTNGeDMaG%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217746c85d48aa3-01f8f2ff09c563-326f7006-1764000-17746c85d491178%22%7D; account_side_nav_state=0%2C0%2C1%2C1%2C0%2C0%2C0%2C0%2C0; _uetsid=79d981b0613b11eb96bfa36d5893389a; _uetvid=79d9bbc0613b11eb8b374b336adcb675; _gat_UA-71722593-2=1; _ga=GA1.1.1212070980.1611819364; tgw_l7_route=b36289c8b42caf5830982fcca07000e2; _ga_K1RSSMGBHL=GS1.1.1611819363.1.1.1611819723.0"

Xiuxiu = User("Xiuxiu", CookieXX, 17282401, "db2c098d411a0bca565c3946e805ed93", "QWRc4O3vEZPWmFNxdIY9famnfH8=",
              "oqWqyP/6esEPPPEMFF4ghA==-1nKiM2vLecsO5qAl6M51j2pHjQY=")

CookieYY = "futu-csrf=cP+Bkx83RbgMDqhAdFZO8aMydj4=; tgw_l7_route=9ac6f67204e4823e967934802391dcfe; cipher_device_id=1616125523639152; device_id=135dafa90bbdb23d; locale=zh-cn; main_brokers=ewogICJtYWluX2Jyb2tlcnMiIDogWwogICAgMQogIF0KfQ==; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221784896767f1fb-03d05b07e-653a5568-181760-178489676800%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221784896767f1fb-03d05b07e-653a5568-181760-178489676800%22%7D; uid=24325416; user_attribution=1; web_sig=pfq7yVA8KViH7rAPNFLNe1AZSe9rn3fUh%2B%2FmJ91PnAjb326X%2BjYltON3HtBfUFDJ%2BNle7h%2BiBGY7SdGyOj7DelNGQ3ojbiTYhxQeT%2BAo2to%3D"

Yangyang = User("Yangyang", CookieYY, 24325416, "db2c098d411a0bca565c3946e805ed93", "5g8mnaoWW3MSX9p/40p2x/qYbv8=")

currentUser = LiXiaoQing
# currentStock =



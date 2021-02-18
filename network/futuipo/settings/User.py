
class User:
    def __init__(self, cookie, account_id, password, r_token, csrf, apply_lots = 1):
        self.cookie = cookie
        self.account_id = account_id
        self.password = password
        self.r_token = r_token
        self.csrf = csrf
        self.apply_lots = apply_lots
        self.result_message = ""


CookieZj = "cipher_device_id=1608107671817181; _gcl_au=1.1.2029423239.1609467477; _fbp=fb.1.1609467479165.1328713019; UM_distinctid=176bbbce4db1f6-0cb7edd00af081-163b6153-1fa400-176bbbce4dc8df; futu-csrf=5sGjScyZNf2R8YIev94tOrFmYpQ=; account_side_nav_state=0%2C0%2C1%2C1%2C0%2C0%2C0%2C0%2C0; device_id=1608107671817181; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv1JO78fRMyrx%2BVOrd%2BsWrsvHhmbDu8KKDXETUnZY0XMBiqPBC2WTc9lcIghBTFwykQ%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221766aafbf59583-0b5da1f78bd219-326e7907-1764000-1766aafbf5ab08%22%7D; locale.sig=kzyT92OiO3iDIp4BhTf7a2E2xf0; locale=zh-cn; _gid=GA1.2.1378379479.1612490237; uid=17448263; web_sig=dK7g%2BHw%2F4J5o3BA4x5qoMp8oYPAFUEP1OOUgx6D34hePy1r3qUWsghUcHHaK6Frqqhko56ecHUEXfQYUBM8ntqCKMdq%2Fe1pAXncI%2BZTeQMgzJfMLDo7WSaIgjOxYMFVI; _uetsid=791592a0675511ebb5c6331ba1bc7a20; _uetvid=e58438005f9e11ebb064c105cf53e7ae; _ga_K1RSSMGBHL=GS1.1.1612490236.5.1.1612490260.0; _ga=GA1.1.815010162.1609467487; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv1JO78fRMyrx%2BVOrd%2BsWrsvHhmbDu8KKDXETUnZY0XMBiqPBC2WTc9lcIghBTFwykQ%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221766aafbf59583-0b5da1f78bd219-326e7907-1764000-1766aafbf5ab08%22%7D; tgw_l7_route=9cbbf626c4d6b56aefba377124e4f025"

Zhaojing = User(CookieZj, 17448263, "db2c098d411a0bca565c3946e805ed93", "sf2dyKj6nIkP2to/d2xLRFWj6GY=",
                "Sp/HvsqXicWyPcLMVOEOqQ==-UD1nBo9WX6kynSvQieg2cU1TPec=")

CookieFB = "uid=11256759; web_sig=KTM6UBQzitTpR7vDcpInJCVe9GseSLSkkn0dP0IBtr9ciZGv%2FR9%2F4hErRkZaG6%2Fpe44I6seULkr6F%2Ft9RAz7dx0YVh7Q6Hp5%2FzracSKNfX%2FP6ufdJFqoso0827ixo0is; futu-csrf=XepLX+u0zacpKca0IiG4oR0no0g=; cipher_device_id=1612492471187142; device_id=1612492471187142; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv1%2Bp%2BiBkNgf1dTmtZyjQFI2HhmbDu8KKDXETUnZY0XMBjKv0ake6uZ9cBVD4hP6K%2Fe%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fpassport.futunn.com%2F%22%7D%2C%22%24device_id%22%3A%22177700a7bc180f-0e60b03d0bd0d4-326f7006-2073600-177700a7bc2b71%22%7D; locale=zh-cn"

Fanbin = User(CookieFB, 11256759, "db2c098d411a0bca565c3946e805ed93", "JwGorD/T8BwCJhIAVemm7+Xl2t0=",
              "QfVOEcdzzgbSphswu/0GmA==-llvLKZI2EMW8qNT7ljedMsJkWPE=")

CookieLX = "uid=17782642; web_sig=PD1sJkhsqFNwmARG%2BTiZFMU5auns6MgcPtDJNUFuZgEp5AB0hbWLlQIQpJngFZU2%2BWKg5jPbtSEOn3u5%2FFwhHe14px33yceAZN7ZkTVYVUeoKo4Ybh%2FTuEp14pXm1peP; tgw_l7_route=9a11ccec84663afb3786dd2c3ab64f23; futu-csrf=Ds50cJX9vqRfD04Skc8frpVRwXE=; cipher_device_id=1612492710472598; device_id=1612492710472598; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv10LFYgDaLPOVRhz2Bx%2B6Pc3hmbDu8KKDXETUnZY0XMBha48R80HJV5FW4%2BXR9wNVW%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fpassport.futunn.com%2F%22%7D%2C%22%24device_id%22%3A%22177700e210e329-0374e1e4f0875-326f7006-2073600-177700e210fa87%22%7D; locale=zh-cn"

Lixue = User(CookieLX, 17782642, "db2c098d411a0bca565c3946e805ed93", "CTz5EwkBXeHuCotvnMtK0qRzgRo=",
             "IsiQbT2pt5kC7gHcyCDS5A==-arz56a0TBFpp7eVVKKzOZgtFIGU=")

CookieLD = "uid=17318381; web_sig=dSX8Csa6LOSHDfCwxNIJTigXrm8GEajb2kH8y5sGy7QXBjrIXFyX0WSHsxmMo83oMWN%2BAbCUBhHniIA17alSP9BgxLq3picl17y8dF4e7FE4x3avR%2Bog8f7NkY8CkbQ5; futu-csrf=lPF4ePFS4TCCSMRXn+K5AU5+YFg=; cipher_device_id=1612492849503068; device_id=1612492849503068; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv1Rgsi%2Fui11GO%2FNnZemf4FR3hmbDu8KKDXETUnZY0XMBjyNIJHs1ylMVV898%2BgisvP%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fpassport.futunn.com%2F%22%7D%2C%22%24device_id%22%3A%2217770103f7d5d0-0c589f9915b56b-326f7006-2073600-17770103f7eb25%22%7D; locale=zh-cn"

LiangDong = User(CookieLD, 17318381, "db2c098d411a0bca565c3946e805ed93", "95cJ4/vOML2LxKvrR5hSXGgN6Vo=",
              "OX1ulDZ1yR+1HCVUICMd5w==-iPtOhhNQXRpzc8OFqNfBeS3TvJo=")

CookieLXQ = "uid=21263432; web_sig=UsOdNjs2eJgePrAgnU5sASQfJp0wDDJgVY1F5FVya1j9PFlxqDvivGXXACedDMAW2klxQRVY4JfT9SlPdABKbzZJHUxpcx1ppkE9zFnAJtsxGeU%2FDI8%2FWPnSzC%2B%2BHlfG; futu-csrf=kSONzTxLdOCrorhdzV8lN3ssies=; cipher_device_id=1613634120354817; device_id=1613634120354817; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv11jQETcoCBx%2By2r2La7S4KHhmbDu8KKDXETUnZY0XMBiuYvcKlutoFILWSvNjSVgn%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fpassport.futunn.com%2F%22%7D%2C%22%24device_id%22%3A%22177b416a94f769-08fd07ec248817-33657509-2073600-177b416a950b21%22%7D; locale=zh-cn"

LiXiaoQing = User(CookieLXQ, 21263432, "db2c098d411a0bca565c3946e805ed93", "m1ri2gnVRK/fX0p1bjy/Vjoxs20=",
                  "up+VpAorifLCcSdsH4dviw==-s7rLGz1zyypbEWUdUCVBFpeKWAc=", 25)

CookieDC = "futu-csrf=OQeMVgzRk9Lv4gKIqJP10mSMmEc=; cipher_device_id=1611800272931535; device_id=1611800272931535; sajssdk_2015_cross_new_user=1; _gcl_au=1.1.1488342976.1611819338; _fbp=fb.1.1611819354043.381292380; _gid=GA1.2.307438622.1611819364; UM_distinctid=17747ebe0d4358-03729fdd02087a-326f7006-1fa400-17747ebe0d5bab; account_side_nav_state=0%2C0%2C1%2C1%2C0%2C0%2C0%2C0%2C0; uid=11905480; web_sig=V07vJ5zI8hbalwkGFWSVkImOTm1kqQZRy%2FOCxYavj03DvXGygTwIp0v7%2B8ZYqDrmVAOwjF%2B1hD8k%2B9i4TNM55VkXOx%2FKcbTkqRl5ReQm%2BiVgHKu%2Fzk3VnC7ELCKQs%2B8f; locale=zh-cn; _uetsid=79d981b0613b11eb96bfa36d5893389a; _uetvid=79d9bbc0613b11eb8b374b336adcb675; _ga=GA1.1.1212070980.1611819364; tgw_l7_route=8f112f9488cffa9272ac4adb176127dd; _ga_K1RSSMGBHL=GS1.1.1611823928.2.1.1611823984.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv144llW1kBLnYY2pluE%2BmVZnhmbDu8KKDXETUnZY0XMBh2vuAolibsuTsUKvYZNKxc%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217746c85d48aa3-01f8f2ff09c563-326f7006-1764000-17746c85d491178%22%7D"

Dingcong = User(CookieDC, 11905480, "db2c098d411a0bca565c3946e805ed93", "kpnItR24tONv2EXWqddw4iMFs3c=",
                "K6YwKCg3VZiGqthCzOXF3Q==-3lmYcgtE9PE3uYpNIsK8ko4tTlg=")

CookieXX = "futu-csrf=OQeMVgzRk9Lv4gKIqJP10mSMmEc=; cipher_device_id=1611800272931535; device_id=1611800272931535; sajssdk_2015_cross_new_user=1; _gcl_au=1.1.1488342976.1611819338; _fbp=fb.1.1611819354043.381292380; _gid=GA1.2.307438622.1611819364; uid=17282401; web_sig=2TyVkbAtaQmNgcanQDn9Cv7NwQM62jti3AI8GmDv3LeGIpkZ37CrI3ddrfVTk2RfX9e%2B%2BaG%2FpQRothvz8FDKeBRVbEbsnQEW97gBOWk4jDgRC6InfIjqtc4GQl2gfASW; locale=zh-cn; UM_distinctid=17747ebe0d4358-03729fdd02087a-326f7006-1fa400-17747ebe0d5bab; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22ftv1HoaMEGwOFtKeeCkkAUGRqHhmbDu8KKDXETUnZY0XMBhsduHfOAuHysZcTNGeDMaG%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217746c85d48aa3-01f8f2ff09c563-326f7006-1764000-17746c85d491178%22%7D; account_side_nav_state=0%2C0%2C1%2C1%2C0%2C0%2C0%2C0%2C0; _uetsid=79d981b0613b11eb96bfa36d5893389a; _uetvid=79d9bbc0613b11eb8b374b336adcb675; _gat_UA-71722593-2=1; _ga=GA1.1.1212070980.1611819364; tgw_l7_route=b36289c8b42caf5830982fcca07000e2; _ga_K1RSSMGBHL=GS1.1.1611819363.1.1.1611819723.0"

Xiuxiu = User(CookieXX, 17282401, "db2c098d411a0bca565c3946e805ed93", "QWRc4O3vEZPWmFNxdIY9famnfH8=",
              "oqWqyP/6esEPPPEMFF4ghA==-1nKiM2vLecsO5qAl6M51j2pHjQY=")

currentUser = LiXiaoQing
# currentStock =



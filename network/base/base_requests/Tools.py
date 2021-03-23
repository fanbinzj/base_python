
def build_headers(cookie, additional_headers_dict):
    return {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G34 /sa-sdk-ios/sensors-verify/sdreport.moomoo.com?production  FutuNN_iPhone/11.5.1308 AppType/MooMoo CliLang/zh-cn ClientSkinType/3 ClientFont/1.0 (im:1; nnc:1; news:1; trade:1; quote:1; other:1) RequestSource/WebView",
        "X-Requested-With": "XMLHttpRequest",
        **additional_headers_dict,
    }
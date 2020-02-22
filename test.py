import urllib.request
import urllib.parse


def process():

    youtube_url = "https://www.youtube.com/"
    baidu_url = "https://wwwz.baidu.com/s?wd=python%203%20urllib&rsv_spt=1&rsv_iqid=0xd0bc59bb0000f3c2&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=15&rsv_sug1=7&rsv_sug7=100&rsv_sug2=0&inputT=3403&rsv_sug4=3403"

    baidu_res = urllib.request.urlopen(baidu_url)
    # youtube_res = urllib.request.urlopen(youtube_url)

    print(baidu_res)
    # print(youtube_res)

    print(baidu_res.read())
    # print(youtube_res.read().decode())


if __name__  == "__main__":
    process()
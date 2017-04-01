# encoding=utf-8
# cookie池，随机获取一个cookie

import Util

# cookie列表
cookieList = [
    '_T_WM=8a1dfbed5a670ca1259050b666fedf8bALF=1492966383SCF=AhHh7nS36n0U5wp6_ZibkBgP71wWBg0HJREDjWQMPVKTSmgbM85vc7y-wHf215gOgwqGdqw4sOMzHRwbT0UL-Hk.SUB=_2A2510T6vDeRxGeBO41cU8ybFzTmIHXVXOkLnrDV6PUJbktBeLRbikW13c8Bi4K0kd9vxkjlloNeiXW_1Gg..SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWGFAy81SZs2zG5ikpRfmWO5JpX5o2p5NHD95QcehnfSKeR1KqfWs4Dqcjr9sRLxK.L1K.L12eLxKML1hBLBoqLxKqLBo-L1h-LxKMLB-eL1K8bSUHB=0auwZE5IosRnd2SSOLoginState=1490374399'
]

# 随机获取一个cookie
def getRandomCookie():
    cookieLength = len(cookieList)
    randomNum = Util.getRandomNum(0, cookieLength - 1)
    cookie = cookieList[randomNum]

    return cookie

# test method
if __name__ == '__main__':
    print getRandomCookie()

def loadUserInfo(file):
     userInfo = {}
    # file = open(file,"r")
    # lines = file.readlines()
    # for i in lines:
    #     if len(i) == 0:
    #         break
    #     if i.startswith('#'):
    #         continue
    #     print(i)
    #     key,value = i.split("=")
    #     userInfo[key] = value
    # print(userInfo)

    for line in open(file,"r").readlines():
        if len(line)>0 and not line.startswith("#"):
            dict([line.strip().split("=")])


loadUserInfo("userInfo")
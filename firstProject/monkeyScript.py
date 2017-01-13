import os
import subprocess


def getDevices():
    str = []
    output = subprocess.check_output(["adb", "devices"])
    a1 = output.decode('ascii')
    a2 = a1.strip().split("\n")
    for j in range(1, len(a2)):
        a3 = a2[j].strip().split()
        print(a3[0])
        str.append(a3[0])
    return str
getDevices()
for i in getDevices():
    cmd = "adb -s {0} shell monkey -p com.shundaojia.travel.passenger --throttle 500 --hprof -s 1000 -v -v -v 500 " \
          ">monkeyLog".format(i)+i+".txt"
    print(cmd)
    os.system(cmd)

# list comprehension
# print("\n".join(str(i) for i in [1, 2, 3]))
# exit(0)
# print(getDevices())


# f1 = open("getAPK.txt", "r")
# lines1 = f1.readlines()
# print(lines[1])
# print(lines.__len__())
#
# for line in range(1, lines.__len__()):
#     a = lines[line].split()
#     print(a[0])
#     cmd1 = "adb -s "+a[0]+" ls data/data >getAPK.txt"
#     os.system(cmd1)
#     for line1 in range(2,lines1.__len__()):
#         a1 = lines1[line1].split()
#         print(a1[-1])
#         if a1[-1].__eq__("com.shundaojia.travel.passenger"):
#             cmd2 = "adb -s "+a[0]+" shell monkey -p "+a1[-1]+" --throttle 500 --hprof -s 1000 -v -v -v 1000 >log2.txt"
#             os.system(cmd2)
#             break




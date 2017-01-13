import os
print 'hhh'
package = "com.shundaojia.travel.passenger"
cmd = "adb -s 192.168.56.101:5555 shell monkey -p{0} --throttle 500 --hprof -s 1000 -v -v -v 500 >log.txt".format(package)
cmd1 = "adb -s 192.168.56.101:5555 shell monkey -f mon.txt 500"

#os.system(cmd)
os.system(cmd1)
#  monkey -p com.shundaojia.travel.passenger --throttle 500 --hprof -s 1000 -v -v -v 80



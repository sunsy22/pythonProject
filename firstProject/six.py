import os
print 'hhh'
package = "com.shundaojia.travel.passenger"
cmd = "adb -s 192.168.56.102:5555 shell monkey -p com.android.settings --throttle 500 --hprof -s 1000 -v -v -v 500"
os.system(cmd)
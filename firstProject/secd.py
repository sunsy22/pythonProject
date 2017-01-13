import StringIO
import subprocess
import os


def main():
    cmd = "adb shell ps"
    s = StringIO.StringIO


    output = subprocess.check_output("adb shell ps")

    buf = StringIO.StringIO(output)
    for line in buf:
        print line
        if "com.android.commands.monkey" in line:
            fragments = line.split()
            pid = fragments[1]
            subprocess.call("adb shell kill -9 " + pid)
            return


if __name__ == '__main__':
    main()
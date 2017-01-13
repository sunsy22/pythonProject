import string
import StringIO

s = StringIO.StringIO()
s.write("aaaaa")
lines = ['xxxxx','bbbbbb']
s.writelines(lines)
s.seek(0)
print s.read()
s.getvalue()
s.write("kkkkkkkk")
s.seek(10)
print s.readline()
print s.len
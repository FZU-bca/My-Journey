f = open("D:/text.txt","r",encoding="utf-8")
print(type(f))
#print(f.read(10))
print(f.read())
lines=f.readlines()
print(type(lines))
print(lines[0])
f = open("D:/text.txt","r",encoding="gbk")
print(lines)
f = open("D:/text.txt","r",encoding="gbk")
line=f.readline()
print(line)
for line in f:
    print(line)


f.close()
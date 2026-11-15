with open("py code\26\11\15\26111502.py", "r") as f:
    print(f.readlines())
    i=read(f)
    times=i.count('asdasdasd')
    print(times)

count=0
with open("py code\26\11\15\26111502.py", "r") as f:
    for line in f:
        line=line.strip()
        words=line.split()
       for word in words:
           if word == "asdasdasdasd":
               count+=1


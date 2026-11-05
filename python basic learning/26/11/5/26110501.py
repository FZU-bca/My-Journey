#practice fo continue and break sentence
#for i in range(1,4)
#    print("sentence1")
#    continue
#    print("sentence2")
#the result is that the sentence2 will not be printed because the "continue"sentence break the code
for i in range(1,10):
    print("sentence1")
    for j in range(1,6):
        print("sentence2")
        continue
        print("sentence3")
    print("sentence4")

for i in range(1,10):
    print("sentence1")
    break
    print("sentence2")
print("sentence3")


for i in range(1,10):
    print("sentence1")
    for i in range(1,6):
        print("sentence2")
        break
        print("sentence3")

    print("sentence4")
#the learning of the using of "continue" and "break"



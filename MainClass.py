limit = int(input())

for i in range(limit+1):
    print("\n"+str(i)+"\n")
    for x in range(11):
        print(str(i)+"x"+str(x)+"="+str(i*x))

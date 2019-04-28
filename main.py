import time


print("----------- Primzahlen-Generator V01 -----------")


lasttime = time.time()
print(f"it is {lasttime}")

n = 1
primenumbers = [2, 3]
n = primenumbers[-1]
found = False



while n<1000000:
    n += 2
    found = False
    for i in primenumbers:
        if n%i==0:
            found= True
            break

    if found==False :
        now = time.time()
        primenumbers.append(n)
        print(f"{len(primenumbers)} : {primenumbers[-1]}  -  {round(now-lasttime, 6)} sec")
        lasttime = now

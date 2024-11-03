lower=int(input("Enter lower number limit here:"))
upper=int(input("Enter upper number limit here:"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
# OUTPUT:
# Enter lower number limit here:5
# Enter upper number limit here:15
# 5
# 7
# 11
# 13

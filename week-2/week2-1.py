def calculate(min,max):
    sum = 0
    if(max > min):
        for i in range(min,max+1):
            sum += i
        print(sum)
    # else:
    #     print("Wrong Input")

calculate(1,3)
calculate(4,8)

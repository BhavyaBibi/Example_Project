#Program check if a number is prime or not

num=29

#if user from outside

flag = False


if num ==1:
    print("number is not a prime number")
elif num>1:
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


        #output 
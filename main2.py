# having numbers 1 to 10 in reverse order but skip the number 5
slick=int(input("enter the number for your variable"))

while slick>0:
    slick=slick-1
    if slick==5:
     continue
    print('\n current value:',slick)
year=int(input("請輸入年"))
month=int(input("請輸入月"))
day=int(input("請輸入日"))
number=year//1000+year%1000//100+year%100//10+year%10+month//10+month%10+day//10+day%10
print(number)
while number>10:
    print((number//10)+(number%10))
    break
     



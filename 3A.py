a=int(input("請輸入三角形A邊長度："))
b=int(input("請輸入三角形B邊長度："))
c=int(input("請輸入三角形C邊長度："))
if a+b>c and b+c>a and c+a>b:
    print("可以成為三角形")
else:
    print("無法成為三角形")
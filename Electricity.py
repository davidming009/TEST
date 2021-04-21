x=float(input("電費度數"))

if x <= 120:
    y=x*2.10
    z=x*2.10
    print("Summer months:",y)
    print("Non-Summer months:",z)
elif x >= 121 or x <= 330:
    y=120*2.10+(x-120)*3.02
    z=120*2.10+(x-120)*2.68
    print("Summer months:",y)
    print("Non-Summer months:",z)
elif x >= 331 or x <= 500:
    y=120*2.10+(330-120)*3.02+(x-330)*4.39
    z=120*2.10+(330-120)*2.68+(x-330)*3.61
    print("Summer months:",y)
    print("Non-Summer months:",z)
elif x >= 501 or x <= 700:
    y=120*2.10+(330-120)*3.02+(500-330)*4.39+(x-500)*4.97
    z=120*2.10+(330-120)*2.68+(500-330)*3.61+(x-500)*4.01
    print("Summer months:",y)
    print("Non-Summer months:",z)

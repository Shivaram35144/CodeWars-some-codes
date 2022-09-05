#Credit Card Mask

# return masked string
def maskify(cc):
    
    if len(cc)>=4:
        actual=cc[-4::]
    else:
        actual=cc
    n=len(cc)-4
    s=""
    for i in range(n):
        s+="#"
    s+=actual
    print(s)
    print(len(cc))
    print(actual)
    
maskify("SF$SDfgsd2eA")

    

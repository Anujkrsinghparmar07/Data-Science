print("Hello")
print("Welcome to Mathematical equations", 'To Continue With Maths')
i = 1
while True:
    for i in range(10):
        print('y=f(x)', 'z=(x,y)')
        print("where f(x)=x^2+2;x>=5", 'and f(x)=x^3;x<5')
        x = int(input('Value of x'))
        if x >= 5:
            y = x ** 2 + 2
    else:
        y = x ** 3
    print(y)
    print("x=", x, '  y=', y)
    z = (x, y)
    print("z=", z)
print("Thank you")

def secant(func,x,y,n):
    def f(x):
        f=eval(func)
        return f
    for i in range(1,n):
        fx=f(x)
        fy=f(y)

        z= x-(fx/((fx-fy)/(x-y)))

        x=y
        y=z

        print("rots are: ", z ,"after ",n, " ripetitions")

secant("x**2 - 6", 1,6, 10 )


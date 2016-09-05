import turtle

def square(t, length):
    print(t)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    t.lt(90)
    t.fd(length)
    turtle.done()



def polygon(t, length, n):
    print(t)
    for i in range(n):
        t.fd(length)
        t.lt(360.00/n)
    turtle.done()

bob = turtle.Turtle()
polygon(bob, 50, 6)

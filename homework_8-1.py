def add_everything_up(a, b):
    try:
        print(a + b)
        # ((a.isinteger() or a.isfloat()) and b.isstring()) or ((b.isinteger() or b.isfloat()) and a.isstring()):
    except TypeError:
        print(str(a) + str(b))

add_everything_up(5, 'h')
add_everything_up('hello, ', 3.14)
add_everything_up(10.56455, 11)


class DemoException(Exception):
    """
    custom exception
    """
    pass

def handler_exception():
    print("-> start")

    while True:
        try:
            x = yield
        except DemoException:
            print("-> run demo exception")
        else:
            print("-> recived x:", x)
    raise RuntimeError("this line should never run")

he = handler_exception()
next(he)

he.send(10)
he.send(20)

he.throw(DemoException)

he.send(40)
he.close()
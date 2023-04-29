def foo(bar):
    match x := bar:
        case "something":
            print("it's something")
        case _:
            print(x)

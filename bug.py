def foo(bar):
    match x := bar:
        case "and":
            print("now")
        case "for":
            print("something")
        case "completely":
            print("different")
        case _:
            print(x)

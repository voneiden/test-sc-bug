def foo(bar):
    match x := bar:
        case "cq_editor":
            print("ok")
        case _:
            logger.warning(
                f"Unsupported show_object source module ({x}) - visualizing as edges"
            )

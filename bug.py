def show(show_object=None):
    if show_object is None:
        import __main__

        show_object = __main__.__dict__.get("show_object")

    if show_object is None:
        raise ValueError(
            "Unable to visualize job, no show_object provided or found"
        )

    match source_module := show_object.__module__.split(".")[0]:
        case "cq_editor":
            visualize_f = 2
        case "ocp_vscode":
            visualize_f = 3
        case _:
            logger.warning(
                f"Unsupported show_object source module ({source_module}) - visualizing as edges"
            )
            visualize_f = 3

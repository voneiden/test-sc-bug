def show(show_object):
    match source_module := show_object.__module__.split(".")[0]:
        case "cq_editor":
            pass
        case "ocp_vscode":
            pass
        case _:
            logger.warning(
                f"Unsupported show_object source module ({source_module}) - visualizing as edges"
            )

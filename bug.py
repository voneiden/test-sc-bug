def show(show_object=None):
    match source_module := show_object.__module__.split(".")[0]:
        case _:
            logger.warning(
                f"Unsupported show_object source module ({source_module}) - visualizing as edges"
            )
            visualize_f = 3

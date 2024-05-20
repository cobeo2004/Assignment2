
class ExportError(Exception):
    """Exception if redundant names attempted exporting"""

    def __init__(self, name, errMessage="Object already exported") -> None:
        self.name = name
        self.err = errMessage
        super().__init__(f'ExportError: {self.name} {self.err}')


def __attr_build_export__(__all__=None):
    """__attr_build_export__: Export decorator for controlling export objects

    Args:
        __all__ (objects | functions, optional): _description_. __all__ Array, defualt is None.

    Raises:
        ExportError: Raise if there are any redundant names attempted exporting

    Returns:
        tuple[Any | list, (obj: Any) -> (str | Any)]: __all__ array and export function
    """
    if __all__ is None:
        __all__ = []

    def export(obj):
        name = obj if isinstance(obj, str) else obj.__name__
        if name in __all__:
            raise ExportError(f'{name} already exported')
        __all__.append(name)
        return obj
    return __all__, export


all_array, export = __attr_build_export__()

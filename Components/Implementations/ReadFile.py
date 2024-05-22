from Components.Interfaces.IReadFile import IReader
from Components.Decorator.Export import export


@export
class ReadFile(IReader):
    def readAll(self, fn: str):
        lines = []
        flattened = []

        tell, query = [], []
        with open(fn) as f:
            for line in f:
                lines.append(line.strip().lower().split(";"))

        for subList in lines:
            for value in subList:
                flattened.append(value)

        try:
            queryIndex = flattened.index("ask")
        except ValueError:
            queryIndex = len(flattened)

        for value in flattened[:queryIndex]:
            if value not in ["", "tell", "ask"]:
                tell.append(value.replace(" ", ""))

        if queryIndex + 1 < len(flattened):
            query = flattened[queryIndex + 1].replace(" ", "")
        else:
            query = ""

        return tell, query

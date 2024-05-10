from Components.Interfaces.IReadFile import IReader


class ReadFile(IReader):
    def readAll(self, fn: str) -> None:
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

    def parseSymbolsSentences(self, teller: str) -> None:
        symbols = set()
        sentences = []
        for sentence in teller:
            symbols.update(r'\b[a-zA-Z] [a-zA-Z0-9]*\b', sentence)
            sentences.append(sentence)
        return symbols, sentences

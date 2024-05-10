class ILogicalSentence:
    def __init__(self, *args) -> None:
        self.args = args

    def eval(self, model):
        pass

    def symbol(self):
        return set()

    def __repr__(self) -> str:
        pass

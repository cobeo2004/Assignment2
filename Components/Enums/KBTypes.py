from enum import Enum
from Components.Decorator.Export import export


@export
class KBType(Enum):
    HF = 1
    GS = 2

    @staticmethod
    def getKBType(type: str):
        if type == 'HF':
            return KBType.HF
        elif type == 'GS':
            return KBType.GS
        else:
            raise Exception("Unknown sentence type.")

    @staticmethod
    def isKBType(type):
        if type is KBType.HF or type is KBType.GS:
            return True
        return False

from enum import Enum, unique, auto

@unique
class 语法(Enum):
    模块 = auto()
    所有语句 = auto()
    语句 = auto()
    表达式 = auto()
    赋值语句 = auto()
    显示语句 = auto()
    量 = auto()
    名称 = auto()
    常量 = auto()

    def 成分(self, *所有成分):
        文本 = []
        for 成分 in 所有成分:
            if isinstance(成分, Enum):
                文本.append(成分.name)
            else:
                文本.append(成分)
        return self.name + " : " + " ".join(文本)

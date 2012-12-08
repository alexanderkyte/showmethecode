# import defs

derivativeDefNeeded = False
integralDefNeeded = False
functionTable == {}

class ParseNode:
    __slots__ = ('lst')
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return str(self.lst)

class ExpressioNode:


class ArithmeticNode:
    __slots__ = ("op", "l-value", "r-value")
    def __init__(self, lst):
        self.op = lst[0]
        self.l-value = lst[1]
        self.r-value = lst[2]
    def eval(self):
        if op == "+":
            return l-value.eval() + " + " + r-value.eval()

        elif op == "*":
            return l-value.eval() + " * " + r-value.eval()

        elif op == "/":
            return l-value.eval() + " / " + r-value.eval()

        elif op == "-":
            return l-value.eval() + " - " + r-value.eval()

class LiteralNode:
    __slots__ = ('val')
    def __init__(self, lst)
        self.val = lst[1]

    def __str__(self):
        return str(self.val)

    def eval(self):
        return str(self.val)

class SummationNode:
    __slots__ = ("returnStr", "lst")
    def __init__(self, inputlst):
        lst = lst
    
    def eval(self):
        self.returnStr = "sum = 0 \n"
        self.returnStr += "\tfor x in range(" + str(lst[1]) + " , " + str(lst[2]) + ":\n"
        self.returnStr += "\t sum += " + lst[3].eval() + "\n"
        return returnStr

class DerivativeNode:
    __slots__ = ("function", "point", "returnStr")
    def __init__(self, lst):
        self.function = lst[0]
        if not isisntance(self.function, FunctionNode)
            raise TypeError("Can only take a function as arg 1.")
        self.args = ""
        for i in lst[1:]:
            if args == "":
                args += i
            else:
                args += ", " + i
    def eval(self):
        returnStr = ""
        returnStr += "derivativeWrapper( " + self.function.name + " , " + self.args  + " )\n"


class IntegralNode:
    __slots__ = ("function", "lower", "upper")
    def __init__(self, lst):
        self.function = lst[0]
        self.lower = lst[1]
        self.upper = lst[2]
        if not isisntance(self.function, FunctionNode)
            raise TypeError("Can only take a function as arg 1.")
    
    def eval(self):
        returnStr = ""
        returnStr += "derivativeWrapper( " + self.function.name + " , " + self.lower  + self.upper + " )\n"
        return returnStr


class FunctionAppNode:
    def __init__(self, lst):
        self.name = lst[0]
        args = ""
        lst = lst.split()
        for i in lst:
            if args == "":
                args += i
            else:
                args += ", " + i

        fullString = self.name + "( " + args  + " )\n"
    
    def eval(self):
        return self.fullString

class FunctionDefNode:
    __slots__ = ("name", "args", "expression")
    def __init__(self, name, args, expression):
        self.name = name
        self.args = args
        self.expression = expression

    def eval(self):
        return "def " + self.name + "( " + self.args + "):\n" + "\nreturn " + self.expression

def parseFunction(lst):
    # of the form (function f (x) (expression)
    name = lst[1]
    args = str(lst[2])[1]
    expression = ExpressionNode(lst[3])
    functionTable[name] == expression

    return FunctionDefNode(name, args, expression)

def parenParser(parseList, l_brack="(", r_brack=")"):
    #assumes the 0-th index is an open parenthesis, skips it to allow recursion
    returnList = list()
    i = 1

    while i < len(parseList):
        if parseList[i] == l_brack:
            node = parenParser(parseList[i:])
            returnList.append(node)
            i += len(node.lst) + 2 #skips current open bracket, the length of the list, and the ending bracket.
        elif parseList[i] == r_brack:
            return ParseNode(returnList[0:i])
        else:
            returnList += parseList[i]
            i += 1


def nodeDecider(node):
    op = node.lst[0]

    if op == "+" or  op == "-" or op == "*" or op == "/":
        return ArithmeticNode(node.lst)
    
    elif op == "quote":
        return LiteralNode(node.lst)

    elif op == "summation":
        return SummationNode(node.lst)

    elif op == "derivative":
        derivativeDefNeeded = True
        return DerivativeNode(node.lst)
    
    elif op == "expression":
        return ExpressionNode(node.lst)

    elif op == "=":
        return VarAssign

    elif op == "function":
        return parseFunction(node.lst)

    elif op == "integral":
        derivativeDefNeeded = True
        return IntegralNode(node.lst)

    elif op in functionTable:
        return FunctionAppNode(node.lst):
        
"""
def main():
    returnStr = """ """
    if derivativeDefNeeded == True:
        returnStr += defs.derivDefintion
    
    if integralDefNeeded == True:
        returnStr += defs.integralDefinition
"""


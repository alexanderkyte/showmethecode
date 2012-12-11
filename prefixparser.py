import defs

derivativeDefNeeded = False
integralDefNeeded = False
functionTable = {}

class EmptyNode:
    __slots__ = ()
    def __str__(self):
        return None

class ParseNode:
    #lst should really be "data", as its the data pointer in the linked list, but I like lst, since most of the time its a list
    __slots__ = ('lst', "next")
    def __init__(self, lst):
        self.lst = lst
        self.next = EmptyNode()

    def __str__(self):
        return str(self.lst)

class ArithmeticNode:
    __slots__ = ("op", "lvalue", "rvalue")
    def __init__(self, lst):
        self.op = lst[0]
        temp = []
        temp += lst[1]
        temp += lst[2]
        
        for i in [0, 1]:
            if isinstance(temp[i], ParseNode):
                temp[i].lst = nodeDecider(temp[i])
                temp[i] = temp[i].lst.eval

        self.lvalue = temp[0]
        self.rvalue = temp[1]

    def eval(self):
        if self.op == "+":
            return "(" + self.lvalue + " + " + self.rvalue + ")"
        elif self.op == "*":
            return "(" + self.lvalue + " * " + self.rvalue + ")"
        elif self.op == "/":
            return "(" + self.lvalue + " / " + self.rvalue + ")"
        elif self.op == "-":
            return "(" + self.lvalue + " - " + self.rvalue + ")"


class LiteralNode:
    __slots__ = ('val')
    def __init__(self, lst):
        self.val = lst[0]

    def __str__(self):
        return str(self.val)

    def eval(self):
        return str(self.val)

class SummationNode:
    __slots__ = ("lower", "upper", "function")
    def __init__(self, lst):
        self.function = lst[1]
        self.lower = lst[2]
        self.upper = lst[3]
        if self.function not in functionTable:
            raise ValueError("Need to define function first.")

    def eval(self):
        returnStr = "summationWrapper(" + self.function + ", " + self.lower + ", " + self.upper + ")\n" + defs.summationDefinition
        return returnStr

    def __str__(self):
        return self.eval

class DerivativeNode:
    __slots__ = ("function", "point", "returnStr")
    def __init__(self, lst):
        self.function = lst[1]
        if self.function not in functionTable:
            raise ValueError("Need to define function first.")
        self.point = lst[2]

    def eval(self):
        returnStr = "derivativeWrapper(" + self.function + ", " + self.point  + ")\n"
        return returnStr + defs.derivDefinition

    def __str__(self):
        return self.eval

class IntegralNode:
    __slots__ = ("function", "lower", "upper")
    def __init__(self, lst):
        self.function = lst[0]
        self.lower = lst[1]
        self.upper = lst[2]
        if self.function not in functionTable:
            raise TypeError("Can only take a function as arg 1.")
    
    def eval(self):
        returnStr = "integralWrapper(" + self.function + ", " + self.lower + ", " + self.upper + " )\n" + defs.integralDefinition
        return returnStr

    def __str__(self):
        return self.eval


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

    def __str__(self):
        return self.eval


class FunctionDefNode:
    __slots__ = ("name", "args", "expression")
    def __init__(self, name, args, expression):
        self.name = name
        self.args = args
        self.expression = expression

    def eval(self):
        return "def " + self.name + "(" + self.args + "):\n" + "\treturn " + self.expression

    def __str__(self):
        return self.eval


def parseFunction(lst):
    # of the form (function f {x} (expression)
    name = lst[1]
    args = str(lst[2])
    args = args[1:]
    args = args[:-1]
    expression = lst[3]
    functionTable[name] = expression
    return FunctionDefNode(name, args, expression)

def parenParser(parseList, l_brack="(", r_brack=")"):
    i = 0
    parseList = parseList[1:] # strips opening parenthesis
    while i < len(parseList):
        if parseList[i] == r_brack:
            rootNode = ParseNode(parseList[0:i])
            if i < (len(parseList)-1):
                rootNode.next = parenParser(parseList[i+1:])
            return rootNode
        else:
            i += 1


class VarAssignNode:
    __slots__ = ("var", "value")
    def __init__(self, lst):
        self.var = lst[1]
        self.value = lst[2]

    def eval(self):
        return self.var + " = " + self.value

    def __str__(self):
        return self.eval

def nodeDecider(node):
    op = node.lst[0]

    if op == "+" or  op == "-" or op == "*" or op == "/":
        return ArithmeticNode(node.lst)

    elif op == "quote":
        return LiteralNode(node.lst[1:])

    elif op == "summation":
        return SummationNode(node.lst)

    elif op == "derivative":
        return DerivativeNode(node.lst)
    
    elif op == "=":
        return VarAssignNode(node.lst)
    
    elif op == "function":
        return parseFunction(node.lst)

    elif op == "integral":
        return IntegralNode(node.lst[1:])

    elif op in functionTable:
        return FunctionAppNode(node.lst)

    else:
        return LiteralNode(node.lst)

def listEater(node):
    while not isinstance(node, EmptyNode):
        node.lst = nodeDecider(node)
        node = node.next

def listEvaller(node):
    returnStr = ""
    while not isinstance(node, EmptyNode):
        returnStr += node.lst.eval() + "\n"
        node = node.next
    return returnStr


def mainLoop(inputString):
    inputString = inputString.split()
    node = parenParser(inputString)
    listEater(node)
    returnStr = listEvaller(node)
    print(returnStr)

if __name__ == "__main__":
    mainLoop("( + 1 2 ) ( quote 12 ) ( 12 ) ( function name {x} x+2+3 ) ( derivative name 10  ) ( integral name 1 100 ) ( summation name 1 100 ) ( = x 3 ) ")


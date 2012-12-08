class parseNode:
    __slots__ = ('lst', 'next')
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return str(self.lst)



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
            return parseNode(returnList[0:i])
        
        else:
        
            returnList += parseList[i]
            i += 1


def nodeDecider(node):
    op = node.lst[0]

    if op == "+":
    elif op == "-":
    elif op == "*":
    elif op == "/":
    elif op == "summation":
    elif op == "derivative":
    elif op == "=":
    elif op == "function":
    elif op == "integral":

"""
    elif op == "-":
    elif op == "-":
    elif op == "-":
    elif op == "-":
    elif op == "-":
"""

print(parenParser("( 1 2 ( 3 4 ) 5 6 )"))

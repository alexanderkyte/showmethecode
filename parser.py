class Parser:
    def __init_(self):
        symtbl = {}
    def scanner(self):
    def peek(self):
        pass
        #integrate whitespace skipping
    def parseExpression(self)
    def parseFunctionDefiniton(self):
        # demand that function definitions be of the form f (x) = expression
        key = line[0] # after splitting. work in progress.
        i = 0
        while line[i] != "=":
            i += 1
        expression = line[i+2:] #+2 because we expect one whitespace after the = sign.
        result = str(key) + " = lambda" 
        variables = parseParenthesis:
        varstr = ""
        for var in variables:
            if len(varstr) == 0:
                varstr += str(var)
            else:
                varstr += " "
                varstr += str(var)
        varstr += ":"
        varstr += expression
        print(varstr)


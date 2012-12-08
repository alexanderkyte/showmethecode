class Parser:
    def __init_(self, expression):
        self.symTbl = {}
        self.expression = expression
        
    def tokenizer(self):
       pass

    def peek(self):
        return self.expression[self.index:self.index+1]
        #integrate whitespace skipping
    
    def parseExpression(self):

    def parseFunctionDefiniton(self):
        # demand that function definitions be of the form f (x) = expression
        key = line[0] # after splitting. work in progress.
        i = 0
        while line[i] != "=":
            i += 1
        expression = line[i+2:] 
        result = str(key) + " = lambda" 
        variables = parseParenthesis:
        varstr = ""
        for var in variables:
            if len(varstr) == 0:
                varstr += str(var)
            else:
                varstr += " "
                varstr += str(var)
        varstr += ":" + expression
        self.symTbl[key] = varstr
        return varstr

    def parseParens():



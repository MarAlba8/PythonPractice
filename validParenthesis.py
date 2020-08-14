class ValidParenthesis: 
    def __init__(self):
        self.symbol = []

    def add_symbol(self, symbol):
        if symbol == '(':
            self.symbol.append(symbol)
        elif symbol == ')' and len(self.symbol) != 0:
            if self.symbol.pop() == 'x':
                self.symbol.append('x')
        elif symbol == ')' and len(self.symbol) == 0:
            self.symbol.append('x')
                                
    def valid(self):
        if len(self.symbol) != 0:
            return False
        return True


strg = input("String: ")
vp = ValidParenthesis()

for c in strg:
    vp.add_symbol(c)

print(vp.valid())

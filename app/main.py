import sys


class Scanner:
    single_character_tokens = {
    "(": "LEFT_PAREN",
    ")": "RIGHT_PAREN",
    "{": "LEFT_BRACE",
    "}": "RIGHT_BRACE",
    "*": "STAR",
    ".": "DOT",
    ",": "COMMA",
    "+": "PLUS",
    "-": "MINUS",
    ";": "SEMICOLON",
    "=": "EQUAL",
    ">": "GREATER",
    "<": "LESS",
    "!": "BANG",
    "/": "SLASH",
    }

# Dictionary for double-character tokens
    double_character_tokens = {
    "==": "EQUAL_EQUAL",
    ">=": "GREATER_EQUAL",
    "<=": "LESS_EQUAL",
    "!=": "BANG_EQUAL",
    "//": "COMMENT",  
    }

    reserved = {
    'and': 'AND',
    'class': 'CLASS',
    'else': 'ELSE',
    'false': 'FALSE',
    'for': 'FOR',
    'fun': 'FUN',
    'if': 'IF',
    'nil': 'NIL',
    'or': 'OR',
    'print': 'PRINT',
    'return': 'RETURN',
    'super': 'SUPER',
    'this': 'THIS',
    'true': 'TRUE',
    'var': 'VAR',
    'while': 'WHILE'
    }

    def __init__(self, file_contents):
        self.file_contents = file_contents
        self.index = 0
        self.line_number = 1
        self.tokens = []

    def is_at_end(self):
        return self.index >= len(self.file_contents)
    
    def peek(self):
        return self.file_contents[self.index]

    def print_token(self, token, char, literal = None):
        if literal == None: 
            literal = "null"
        print(f"{token} {char} {literal}")

    def comment_out(self):
        while not self.is_at_end() and self.peek() != '\n':
            self.index += 1
        self.line_number += 1 # because we hit a new line character to break out of the while loop
    
    def get_string(self):
        string = ""
        while not self.is_at_end() and self.peek() != '"'  : 
            if (self.peek() == "\n"):
                self.line_number += 1
            string += self.peek()
            self.index += 1
         
        if self.is_at_end():
            return "Error: Unterminated string."
        
        if self.peek() == '"':
            self.index += 1
            return "\""+string+"\""
        
    def get_number(self,number):
        while not self.is_at_end() and (self.peek().isdigit() or self.peek()=="."): 
            if (self.peek() == "\n"):
                self.line_number += 1
            number += self.peek() + ""
            self.index += 1
        return number
    
    def remove_zeroes(self, number):
        length = len(number)
        if not "." in number:
            return number
        for n in number[::-1]:
            if n=="0":
                length -= 1
            else:
                break
        literal = number[0:length]
        if literal[-1] == ".":
            literal = literal[0:-1]
        return literal
       
    def get_word(self, word):
        while not self.is_at_end() and self.peek() != " " and self.peek() != "\n" and self.peek() not in self.single_character_tokens: 
            # if (self.peek() == "\n"):
            #     self.line_number += 1
            word += self.peek()
            self.index += 1
        return word


    def scan_tokens(self):
        error = False
        while self.index < len(self.file_contents):
            c = self.file_contents[self.index]
            self.index += 1

            if c in [" ", "\t", "\n"]:
                if c == '\n':
                    self.line_number += 1
                continue
            elif c in ["=","<",">","!","/"] and not self.is_at_end():  #POTENTIAL ERROR WITH / if input it =/ then itll think its a comment - maybe split if statements so comment has its own  
                next_c = self.peek()
                match next_c:
                    case '=':
                        self.print_token(self.double_character_tokens.get(c+next_c), c+next_c)
                        self.index += 1
                    case '/':
                        self.comment_out()
                        self.index += 1
                    case _:
                        self.print_token(self.single_character_tokens.get(c), c)
            elif c in self.single_character_tokens:
                self.print_token(self.single_character_tokens.get(c), c)
            elif c == '"':
                string = self.get_string()
                if string[0]+string[-1] == "\"\"":
                    self.print_token("STRING",string, string[1:-1])
                else:
                    error = True
                    sys.stderr.write(f"[line {self.line_number}] {string}\n")
            elif c.isdigit():
                number = self.get_number(c)
                literal = self.remove_zeroes(number)

                if "." in literal:
                    self.print_token("NUMBER", number, literal)
                else: 
                    self.print_token("NUMBER",number, literal+".0")
            elif c.isalpha() or c == "_":
                word = self.get_word(c)
                if word in self.reserved:
                    self.print_token(self.reserved.get(word),word)
                else: 
                    self.print_token("IDENTIFIER", word)
            else:
                error = True
                sys.stderr.write(f"[line {self.line_number}] Error: Unexpected character: {c}\n")
            

        print("EOF  null")
        return error



def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    # if file_contents:
        # raise NotImplementedError("Scanner not implemented")
    # else:
        # print("EOF  null") 

    scanner = Scanner(file_contents)
    error = scanner.scan_tokens()

    if(error):
        exit(65)
    else:
        exit(0)
        
if __name__ == "__main__":
    main()

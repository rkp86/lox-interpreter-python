import sys


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

    line_number = 0
    error = False
    found_equal = False
    found_g = False 
    found_l = False
    found_n = False
    found_s = False
    token = ""
    # for line in file_contents:
    #     print(line, end='')

    for line in file_contents:
        line_number += 1
        for i in range(len(line)):
            c = line[i]   #getting the character

            # Scanning Assignment & Equality Operators (pt1)
            if found_equal:
                found_equal = False
                if c == "=" :
                    token = "EQUAL_EQUAL"
                    print(f"{token} ={c} null")
                    continue
                print(f"{token} = null")
            elif found_g:
                found_g = False
                if c == "=" :
                    token = "GREATER_EQUAL"
                    print(f"{token} >{c} null")
                    continue
                print(f"{token} > null")
            elif found_l:
                found_l = False
                if c == "=" :
                    token = "LESS_EQUAL"
                    print(f"{token} <{c} null")
                    continue
                print(f"{token} < null")
            elif found_n:
                found_n = False
                if c == "=" :
                    token = "BANG_EQUAL"
                    print(f"{token} !{c} null")
                    continue
                print(f"{token} ! null")
            elif found_s:
                found_s = False
                if c == "/" :
                    token = "COMMENT"
                    break
                print(f"{token} / null")


            match c: 
                # Scanning Single-character tokens
                case "(":
                    token = "LEFT_PAREN" 
                case ")":
                    token = "RIGHT_PAREN" 
                case "{":
                    token = "LEFT_BRACE"
                case "}":
                    token = "RIGHT_BRACE" 
                case "*":
                    token = "STAR" 
                case ".":
                    token = "DOT" 
                case ",":
                    token = "COMMA"
                case "+":
                    token = "PLUS" 
                case "-":
                    token = "MINUS"
                case "/":
                    token = "SLASH"
                case ";":
                    token = "SEMICOLON"

                # Scanning Assignment & Equality Operators (pt2)

                case "=":
                    token = "EQUAL"
                    found_equal = True
                    if (line_number != len(file_contents)):
                        continue
                case ">":
                    token = "GREATER"
                    found_g = True
                    if (line_number != len(file_contents)):
                        continue
                case "<":
                    token = "LESS"
                    found_l = True
                    if (line_number != len(file_contents)):
                        continue
                case "!":
                    token = "BANG"
                    found_n = True
                    if (line_number != len(file_contents)):
                        continue
                case "/":
                    token = "SLASH"
                    found_s = True
                    if (line_number != len(file_contents)):
                        continue
                case _:
                    error = True
                    sys.stderr.write(f"[line 1] Error: Unexpected character: {c}\n")
                    continue


            print(f"{token} {c} null")

    print("EOF  null")

    if(error):
        exit(65)
    else:
        exit(0)
        
if __name__ == "__main__":
    main()

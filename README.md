[![progress-banner](https://backend.codecrafters.io/progress/interpreter/4c6c3931-82b2-4933-a2ba-955da283743d)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This is a starting point for Python solutions to the
["Build your own Interpreter" Challenge](https://app.codecrafters.io/courses/interpreter/overview).

This challenge follows the book
[Crafting Interpreters](https://craftinginterpreters.com/) by Robert Nystrom.

In this challenge you'll build an interpreter for
[Lox](https://craftinginterpreters.com/the-lox-language.html), a simple
scripting language. Along the way, you'll learn about tokenization, ASTs,
tree-walk interpreters and more.

Before starting this challenge, make sure you've read the "Welcome" part of the
book that contains these chapters:

- [Introduction](https://craftinginterpreters.com/introduction.html) (chapter 1)
- [A Map of the Territory](https://craftinginterpreters.com/a-map-of-the-territory.html)
  (chapter 2)
- [The Lox Language](https://craftinginterpreters.com/the-lox-language.html)
  (chapter 3)

# Base Stages:

1. Ensure you have `python (3.12)` installed locally
2. Run `./your_program.sh` to run your program, which is implemented in
   `app/main.py`.
3. Commit your changes and run `git push origin master` to submit your solution. Test output will be streamed to your terminal.

This stage involves building a scanner for the Lox interpreter. It will scan through source code and group tokens such as keywords, operators, punctuation, whitespace, and literals (strings, numbers).

This stage is thoroughly explained in: Chapter 4
[Scanning](https://craftinginterpreters.com/scanning.html).

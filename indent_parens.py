from typing import List

"""
Implement an algorithm that takes in a string containing a parenthesized expression and prints it out with all sibling expressions at the same indent level, each on its own line.

Definitions:
A parenthesized expression consist of an opening parenthesis, one or more expressions separated by one or more spaces, and a closing parenthesis. 
An expression is either a word or a parenthesized expression. 

Sample input and output:
Input: (hi)

(
  hi
)


Input: (hi hello)

(
  hi
  hello
)


Input: (hi hello (bye))

(
  hi
  hello
  (
    bye
  )
) 

Input: (hi hello (bye (hey) goodbye))

(
  hi
  hello
  (
    bye
    (
      hey
    )
    goodbye
  )
)
"""

def flush_word_to_storage(word: List[str], level: int, indented: List[str]):
    if word:
        padding = level * '\t'
        line = padding + "".join(word)
        if line:
            indented.append(line)
        word.clear()

def indent_string(input_str: str) -> str:
    indented = []
    level = 0
    word = []
    
    for ch in input_str:
        if ch == '(':
            flush_word_to_storage(word, level, indented)
            indented.append(level * '\t' + '(')
            level += 1
        elif ch == ')':
            flush_word_to_storage(word, level, indented)
            level -= 1
            if level < 0:
                raise ValueError("Input string cannot have unbalanced parentheses!")
            indented.append(level * '\t' + ')')
        elif ch == ' ':
            flush_word_to_storage(word, level, indented)
        else:
            word.append(ch)
    
    if level != 0:
        raise ValueError("The input string does not have balanced parentheses!")
    
    return "\n".join(indented)

if __name__ == "__main__":
    print(indent_string("(hi         hello (bye (hey) goodbye))"))
    print(indent_string(""))
    print(indent_string("(hi hello(bye))"))
    print(indent_string("(hi hello)"))
    print(indent_string("(hi)"))
    print(indent_string(""))
    print(indent_string("bro"))

    try:
        indent_string("))((()))")
        assert False
    except:
        print("Expected a failure here!")

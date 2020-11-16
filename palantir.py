# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Write a function to determine whether the given UTF-8 string (composed of potentially a number of letters) is valid.

For example

boolean isValidUtf8String(String input) {}


3 kinds of UTF-8 characters:
1-byte: 0xxxxxxx
2-byte: 110xxxxx 10xxxxxx
3-byte: 1110xxxx 10xxxxxx 10xxxxxx

// valid single byte character
Input: "01010101"
Output: true

// valid multi-byte character
Input: "1100000010111111"
Output: true


// multiple characters
Input: "110000001011111100000000"
Output: true

// doesn't match pattern
Input: "11111111"
Output: false
"""

"""
StringParser -> countTotalNumberOfByteDvisions(string) -> 1-3+
OneByteRule: validateString(String[] string) -> Boolean
TwoByteRule: validateString(String[] string) -> Boolean
PrefixCheck: matchesPrefix(String beginning) -> Boolean
ThreeByteRule
"""
def is_valid_utf8(string):
    n = len(string)
    prefixes = ["0", ["110", "10"], ["1110", "10", "10"]]
  
    pointer = 0
    # 
    while pointer < n:
        for prefix_rule in prefixes:
            for sub_rule in prefix_rule:
                if string.starts_with(prefix_rule):
                    continue_with_rule = True
                    
        # Perform validation depending on the number of bytes of the string

        

def matches_prefix(string, prefix):
    return string.starts_with(prefix)
    
class PrefixRule(object):
    def __init__(self, string, prefix_rule):
        self.string = string
    
    def is_valid(string):
        pass

if __name__ == "__main__":
    assert is_valid_utf8("01010101")
    assert not is_valid_utf8("11111111")
    assert is_valid_utf8("1100000010111111")
    assert is_valid_utf8("110000001011111100000000")
    assert is_valid_utf8("")

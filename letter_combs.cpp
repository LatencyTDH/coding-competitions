#pragma GCC push_options
#pragma GCC optimize("unroll-loops")

#include <string>
#include <unordered_map>
#include <stack>
#include <vector>
#include <iostream>

using namespace std;

vector<string> letterCombinations(string digits) {
    const size_t n = digits.size();
    vector<string> visited;
    if (n == 0) {
        return visited;
    }
    stack<string> st;
    st.push("");
    unordered_map<int, string> num2letters = {
        {2, "abc"}, {3, "def"}, {4, "ghi"}, {5, "jkl"},
        {6, "mno"}, {7, "pqrs"}, {8, "tuv"}, {9, "wxyz"}
    };
    while (!st.empty()) {
        string letters = st.top();
        st.pop();
        const size_t i = letters.size();
        if (i == n) {
            visited.emplace_back(letters);
        } else {
            string val = num2letters[digits[i] - '0'];
            for (auto it = val.begin(); it != val.end(); ++it) {
                st.emplace(letters + *it);
            }
        }
    }
    return visited;
}

int main(int argc, char** argv) {
    vector<string> output = letterCombinations(argv[1]);
    for (auto it = output.begin(); it != output.end(); ++it) {
        std::cout << *it << std::endl;
    }
    return 0;
}

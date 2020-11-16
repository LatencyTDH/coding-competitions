from typing import List, Set, Tuple
import collections

CodeMetadata = collections.namedtuple(
    'CodeMetadata', ['leading_char_freqs', 'distinct_letters'])


def find_digit_string(queries: List[List[Tuple[int, str]]]) -> str:
    analysis = analyze_query_responses(queries)
    secret = ''

    for letter, freq in analysis.leading_char_freqs.most_common():
        secret += letter

    missing_char = (analysis.distinct_letters - set(secret)).pop()
    secret = missing_char + secret
    
    return secret


def analyze_query_responses(
        queries: List[List[Tuple[int, str]]]) -> CodeMetadata:
    freq_as_leading = collections.defaultdict(int)
    distinct_letters = set()

    for _, response in queries:
        freq_as_leading[response[0]] += 1
        for char in response:
            if char not in distinct_letters:
                distinct_letters.add(char)

    return CodeMetadata(collections.Counter(freq_as_leading), distinct_letters)


def main():
    tcs = int(input())
    for case in range(1, tcs + 1):
        matrix = []
        U = input()
        for i in range(10 ** 4):
            num, code = input().split()
            num = int(num)
            matrix.append((num, code))
        ans = find_digit_string(matrix)
        print("Case #{}: {}".format(case, ans))


if __name__ == '__main__':
    main()

import re

VOWELS = {"a", "e", "i", "o", "u"}


def construct_regexes(query: str) -> list[re.Pattern]:
    tiers = [re.compile(query), re.compile(r"(?i)" + query)]
    final_regex = r"(?i)"
    for char in query:
        if char.lower() in VOWELS:
            final_regex += r"[aeiou]"
        else:
            final_regex += char

    tiers.append(re.compile(final_regex))
    return tiers


def find_one_match(word_list: list[str], regexes: list[re.Pattern]) -> str:
    for regex in regexes:
        for word in word_list:
            if regex.fullmatch(word) is not None:
                return word


def spellcheck(word_list: list[str], query: str) -> None:
    regexes = construct_regexes(query)
    best_word = find_one_match(word_list, regexes)
    return best_word if best_word is not None else ""

def spellchecker(word_list: list[str], queries: list[str]):
    return [spellcheck(word_list, query) for query in queries]

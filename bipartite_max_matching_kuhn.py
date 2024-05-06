import collections
import unittest


class MaximumMatcher:
    def __init__(self, graph: list[list[int]], rows: int, cols: int):
        self.graph = graph
        self.rows = rows
        self.cols = cols

    def max_matching(self) -> list[int]:
        matches = [-1] * self.cols

        def try_kuhn(v: int) -> bool:
            if v in used:
                return False

            used.add(v)
            for to in self.graph[v]:
                if matches[to] == -1 or try_kuhn(matches[to]):
                    matches[to] = v
                    return True

            return False

        used = set()
        preassigned = set()
        for v in self.graph:
            for u in self.graph[v]:
                if matches[u] == -1:
                    matches[u] = v
                    preassigned.add(v)
                    break

        for v in self.graph:
            if not v in preassigned:
                used = set()
                try_kuhn(v)

        return [(index, target) for index, target in enumerate(matches) if target != -1]


class MatchingTester(unittest.TestCase):
    def test_problem_assignment_matching(self):
        problems = {
            0: ["array"],
            1: ["dp"],
            2: ["trees", "dp"],
            3: ["graph", "trees", "array", "dp"],
            4: ["graph"],
        }

        preferences = {
            "A": ["graph"],
            "B": ["graph", "trees", "array", "dp"],
            "C": ["dp"],
            "D": ["array"],
            "E": ["graph"],
        }

        ppl_to_problems = collections.defaultdict(list)
        for person in preferences:
            for problem in problems:
                tags = problems[problem]
                if any(tag in preferences[person] for tag in tags):
                    ppl_to_problems[person].append(problem)

        matcher = MaximumMatcher(ppl_to_problems, len(preferences), len(problems))
        matchings = matcher.max_matching()
        print(matchings)


if __name__ == "__main__":
    unittest.main()

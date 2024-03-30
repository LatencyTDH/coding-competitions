import unittest


class ParseMachine:
    def __init__(self, word, abbr):
        self.state = None
        self.word = word
        self.abbr = abbr
        self.word_cursor = 0
        self.abbr_cursor = 0
        self.initialize_state()

    def initialize_state(self) -> None:
        start_ch = self.abbr[0]
        if start_ch.isdigit():
            self.state = NumberState(self)
        elif start_ch.isalpha():
            self.state = LetterState(self)
        else:
            raise ValueError("Invalid initial character")

    def transition(self, new_state) -> None:
        self.state.on_exit()
        self.state = new_state
        self.state.on_entry()

    def increment_cursor(self, adjust: int) -> None:
        self.word_cursor += adjust

    def get_current_abbreviation(self) -> str:
        return self.abbr[self.abbr_cursor]

    def is_end(self) -> bool:
        return self.word_cursor >= len(self.word) or self.abbr_cursor >= len(self.abbr)

    def parse(self) -> bool:
        try:
            while not self.is_end():
                self.state.parse()
            self.transition(EndState(self))
        except ValueError:
            return False
        return True


class State:
    def __init__(self, parse_machine):
        self.parse_machine = parse_machine

    def on_entry(self) -> None:
        return

    def on_exit(self) -> None:
        return

    def parse(self) -> None:
        return


class EndState(State):
    def on_entry(self) -> None:
        if self.parse_machine.word_cursor != len(self.parse_machine.word):
            raise ValueError("Invalid word after parsing all characters")
        if self.parse_machine.abbr_cursor != len(self.parse_machine.abbr):
            raise ValueError("Invalid abbreviation!")


class LetterState(State):
    def parse(self) -> None:
        char = self.parse_machine.get_current_abbreviation()

        if char.isdigit():
            self.parse_machine.transition(NumberState(self.parse_machine))
            return
        if char != self.parse_machine.word[self.parse_machine.word_cursor]:
            raise ValueError("[LetterState] Letter did not match expected")

        self.parse_machine.word_cursor += 1
        self.parse_machine.abbr_cursor += 1


class NumberState(State):
    def __init__(self, parse_machine):
        super().__init__(parse_machine)
        self.value = 0

    def on_exit(self) -> None:
        self.parse_machine.increment_cursor(self.value)

    def parse(self) -> None:
        char = self.parse_machine.get_current_abbreviation()
        if char.isalpha():
            self.parse_machine.transition(LetterState(self.parse_machine))
            return

        if char.isdigit():
            if self.value == 0 and char == "0":
                raise ValueError("Initial digit cannot start with 0!")
            self.value = 10 * self.value + int(char)
        else:
            raise ValueError(
                "Invalid character detected in abbreviation while in NumberState!"
            )
        self.parse_machine.abbr_cursor += 1


class TestParseMachine(unittest.TestCase):
    def test_valid_parse(self):
        word = "apple"
        abbr = "a3e"
        parser = ParseMachine(word, abbr)
        self.assertTrue(parser.parse())

    def test_invalid_parse(self):
        word = "apple"
        abbr = "ap4"
        parser = ParseMachine(word, abbr)
        self.assertFalse(parser.parse())

    def test_invalid_initial_character(self):
        word = "apple"
        abbr = "1ap"
        parser = ParseMachine(word, abbr)
        self.assertFalse(parser.parse())

    def test_initial_digit_zero(self):
        word = "apple"
        abbr = "a03"
        parser = ParseMachine(word, abbr)
        self.assertFalse(parser.parse())

    def test_invalid_word_after_parsing_all_characters(self):
        word = "apple"
        abbr = "applez"
        parser = ParseMachine(word, abbr)
        self.assertFalse(parser.parse())

    def test_invalid_abbreviation(self):
        word = "apple"
        abbr = "ape"
        parser = ParseMachine(word, abbr)
        self.assertFalse(parser.parse())

    def test_rest(self):
        test_cases = [
            ("substitution", "s10n", True),
            ("substitution", "sub4u4", True),
            ("substitution", "12", True),
            ("substitution", "su3i1u2on", True),
            ("substitution", "substitution", True),
            ("substitution", "substition1", False),
            ("internationalization", "i19", True),
            ("substitution", "s55n", False),
            ("substitution", "s010n", False),
            ("substitution", "s0ubstitution", False),
        ]
        for word, abbr, expected_result in test_cases:
            parser = ParseMachine(word, abbr)
            actual_result = parser.parse()
            self.assertEqual(
                expected_result, actual_result, f"Word: {word}, Abbreviation: {abbr}"
            )


if __name__ == "__main__":
    unittest.main()

import unittest


class ValidatorTest(unittest.TestCase):
    def test_should_check_for_digits_in_test(self):
        validator = Validator()
        self.assertEqual(validator.has_at_least_1_number("1234DRf"), True)
        self.assertEqual(validator.has_at_least_1_number("DRf"), False)

    def test_should_check_for_one_lower_case_character(self):
        validator = Validator()
        self.assertEqual(validator.has_lowercase_character("1234DRf"), True)
        self.assertEqual(validator.has_lowercase_character("DRG"), False)

    def test_should_check_for_one_upper_case_character(self):
        validator = Validator()
        self.assertEqual(validator.has_uppercase_character("1234DRf"), True)
        self.assertEqual(validator.has_uppercase_character("sde"), False)

    def test_should_check_for_one_special_character(self):
        validator = Validator()
        self.assertEqual(validator.has_special_character("1234DRf@"), True)
        self.assertEqual(validator.has_special_character("1234DRf#"), True)
        self.assertEqual(validator.has_special_character("1234DRf$"), True)
        self.assertEqual(validator.has_special_character("sde!^"), False)

    def test_if_password_is_atleast_6_character(self):
        validator = Validator()
        self.assertEqual(validator.is_at_least_6_characters("1234DRf@"), True)
        self.assertEqual(validator.is_at_least_6_characters("1234"), False)

    def test_if_password_is_atmost_16_characters(self):
        validator = Validator()
        self.assertEqual(validator.is_at_most_16_characters("1234567890123456"), True)
        self.assertEqual(
            validator.is_at_most_16_characters("12345678912345671234567891234567"),
            False,
        )

    def test_validate_permutations_of_password(self):
        validator = Validator()
        self.assertEqual(validator.validate("12345"), False)
        self.assertEqual(validator.validate("AB@123456"), False)
        self.assertEqual(validator.validate("ABc@123456"), True)
        self.assertEqual(validator.validate("AB@1234567898765"), False)
        self.assertEqual(validator.validate("ABc@1234567898"), True)


class Validator:
    def has_at_least_1_number(self, password):
        for character in password:
            if is_digit(character):
                return True
        return False

    def has_lowercase_character(self, password):
        for character in password:
            if is_lower_case(character):
                return True
        return False

    def has_uppercase_character(self, password):
        for character in password:
            if is_upper_case(character):
                return True
        return False

    def has_special_character(self, password):
        for character in password:
            if is_special(character):
                return True
        return False

    def is_at_least_6_characters(self, password):
        return len(password) >= 6

    def is_at_most_16_characters(self, password):
        return len(password) <= 16

    def validate(self, password):
        return (
            self.has_at_least_1_number(password)
            and self.has_lowercase_character(password)
            and self.has_uppercase_character(password)
            and self.has_special_character(password)
            and self.is_at_most_16_characters(password)
            and self.is_at_least_6_characters(password)
        )


# Helper funtions
def is_alpha(element):
    return element.isalpha()


def is_digit(element):
    return element.isdigit()


def is_lower_case(element):
    return element.islower()


def is_upper_case(element):
    return element.isupper()


def is_special(element):
    special_characters = ["$", "#", "@"]
    return element in special_characters

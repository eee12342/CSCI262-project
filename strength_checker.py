import string
import getpass


# the strength checker acts as the engine of the program
class StrengthChecker:
    def __init__(self):
        self.passwords = {} # here we'll store every password created and associated information, e.g. strength score

    def get_password_input(self):
        """Creates a Password object from the user input."""
        psw = getpass.getpass("Enter your password: ")
        psw_obj = Password(psw)

        print(vars(psw_obj)) # just for testing


class Password:
    def __init__(self, characters):
        self.characters = characters
        self.lower_count, self.upper_count, self.num_count, self.wspace_count, self.special_count = self.get_char_counts()

    def get_char_counts(self, lower=True, upper=True, num=True, wspace=True, special=True):
        args = [lower, upper, num, wspace, special]
        counts = [0 for _ in range(5)] # keeps the counts of how many times each kind of character appears
        for char in self.characters:
            if char in string.ascii_lowercase:
                counts[0] += 1
            elif char in string.ascii_uppercase:
                counts[1] += 1
            elif char in string.digits:
                counts[2] += 1
            elif char == " ":
                counts[3] += 1
            # must be a special character
            else:
                counts[4] += 1

        return [counts[i] for i in range(5) if args[i]]

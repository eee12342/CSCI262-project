from strength_checker import StrengthChecker
import random
import datetime
import json
import urllib.request
from subs import SUBS as subs


FILE_PATH = "passwords.json"


def space_calc(password: str):
    lower_used = upper_used = special_used = number_used = False
    possible_char = 0
    length = len(password)

    for char in password:
        if char.isupper():
            upper_used = True
        elif char.islower():
            lower_used = True
        elif char.isdigit():
            number_used = True
        else:
            special_used = True
    
    if lower_used:
        possible_char += 26
    if upper_used:
        possible_char += 26
    if special_used:
            possible_char += 128
    if number_used:
        possible_char += 10
        
    password_space = 0
    password_space = possible_char ** length
    return password_space



def sub_letters(password:str, sub_chance: float = 0.6): # by itself, this does very little, as dictionary attacks account for this
    subbed_password = ""
    for char in password:
    # check if the character has substitutions available and randomly decide if to use it or not
        if char in subs and random.random() < sub_chance:
        # pick a random substitution from the list for that character
            subbed_password += random.choice(subs[char])
        else:
        # keep the original character
            subbed_password += char

    return subbed_password

def generate_random():
    # pull todays wordle form the new york times api, alter it with sub_letters
    # then add a random number and symbol
    
    # get today's date in YYYY-MM-DD format
    today = datetime.date.today().strftime("%Y-%m-%d")
    url = f"https://www.nytimes.com/svc/wordle/v2/{today}.json"

    try:
        # fetch the json data from the nyt wordle api w
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode("utf-8"))
            wordle_answer = data.get("solution", "crane")

    except Exception:
        # fallback list of wordle type words in case of no internet connection during marking
        fallback_words = ["crane", "slate", "audio", "orbit", "prism", "ghost"]
        wordle_answer = random.choice(fallback_words)

    # randomly capitalise some letters before substitution to increase variance
    mixed_case_wordle = "".join(
        char.upper() if random.random() < 0.5 else char.lower()
        for char in wordle_answer
    )

    # mutate the Wordle word using sub_letters (lower sub_chance of 0.75 to make the completely random word possible to remember)
    mutated_wordle = sub_letters(mixed_case_wordle, sub_chance=0.3)

    # add a random separator symbol and 2 random digits to guarantee all character sets are hit
    separators = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "="]
    sep = random.choice(separators)
    digits = f"{random.randint(10, 99)}"

    return f"{sep}{mutated_wordle}{digits}"


def read_from_file() -> dict:
    with open(FILE_PATH) as pswd_file:
        data = json.load(pswd_file)
        return data


def save_to_file(data) -> None:
    with open(FILE_PATH, "w") as pswd_file:
        json.dump(data, indent=4)


print(read_from_file())

for i in range (0,4):
    new = sub_letters("Lyndong") + generate_random()
    print(new)
    print(f"Strength: {space_calc(new)}")

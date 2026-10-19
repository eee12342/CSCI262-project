from strength_checker import StrengthChecker
import getpass
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
        json.dump(data, pswd_file, indent=4)


def find_password(dictionary):
    key = input("Enter the name of the service the password is used for: ").strip().lower()
    result = dictionary.get(key)
    if not result:
        print(f"There is no password currently stored under the service named '{key}'.")
        return 

    print(f"The password currently stored for {key} is '{result}'")
    return key, result


def create_password(dictionary):
    service_name = input("Enter the name of the service the password is attached to: ").strip().lower()
    new_pass = getpass.getpass("Enter the new password: ")
    dictionary[service_name] = new_pass
    save_to_file(dictionary)
    print("New password saved to file")


pswd_data = read_from_file()
current_service = ""
current_pass = ""
program_active = True
while program_active:
    if current_pass:
        action = input("What would you like to do next? Enter 'm' to add subtitute characters to your passsword, 's' to save the current password, 'q' to quit: ").strip().lower()
    else:
        action = input("What would you like to do next? Enter 'r' to retrieve a stored password, 'c' to create a new password, 'q' to quit: ").strip().lower()

    if action == "q":
        break
    elif action == "r":
        current_service, current_pass = find_password(pswd_data)
    elif action == "c":
        create_password(pswd_data)
    elif action == "s":
        pswd_data[current_service] = current_pass
        save_to_file(pswd_data)
    elif action == "m":
        current_pass = sub_letters(current_pass) + generate_random()
        print(f"The substituted password is {current_pass}")



for i in range (0,4):
    new = sub_letters("Lyndong") + generate_random()
    print(new)
    print(f"Strength: {space_calc(new)}")

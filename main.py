from strength_checker import StrengthChecker


engine = StrengthChecker()
engine.get_password_input()
def space_calc(password: str):
    lower_used = False
    upper_used = False
    special_used = False
    number_used = False
    possible_char = 0
    length = len(password)
    for i in password:
        if i.isupper():
            upper_used = True
            
        elif i.islower():
            lower_used = True
        elif i.isdigit():
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


import random
import datetime
import json
import urllib.request
def space_calc(password: str):
    lower_used = False
    upper_used = False
    special_used = False
    number_used = False
    possible_char = 0
    length = len(password)
    for i in password:
        if i.isupper():
            upper_used = True
            
        elif i.islower():
            lower_used = True
        elif i.isdigit():
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
    # mapping characters to a list of possible like reddit typing, symbol, or case swap
    subs = {
    "a": ["@", "4", "^", "A"],
    "A": ["@", "4", "^", "a"],
    "b": ["8", "6", "B"],
    "B": ["8", "6", "b"],
    "c": ["(", "<", "{", "[", "C"],
    "C": ["(", "<", "{", "[", "c"],
    "d": ["D", ")"],
    "D": ["0", ")", "d"],
    "e": ["3", "&", "E"],
    "E": ["3", "&", "e"],
    "f": ["#", "F"],
    "F": ["#", "f"],
    "g": ["9", "6", "&", "G"],
    "G": ["9", "6", "&", "g"],
    "h": ["#", "H"],
    "H": ["#", "h"],
    "i": ["1", "!", "|", "I"],
    "I": ["1", "!", "|", "i"],
    "j": ["]", ";", "J"],
    "J": ["]", ";", "j"],
    "k": ["<", "K"],
    "K": ["<", "k"],
    "l": ["1", "!", "|", "L"],
    "L": ["1", "!", "|", "l"],
    "m": ["M", "w"],
    "M": ["m", "W"],
    "n": ["N", "~"],
    "N": ["n", "~"],
    "o": ["0", "*", "O"],
    "O": ["0", "*", "o"],
    "p": ["9", "?", "P"],
    "P": ["9", "?", "p"],
    "q": ["9", "Q"],
    "Q": ["9", "q"],
    "r": ["R", "?"],
    "R": ["r", "2"],
    "s": ["$", "5", "z", "S"],
    "S": ["$", "5", "Z", "s"],
    "t": ["7", "+", "T"],
    "T": ["7", "+", "t"],
    "u": ["v", "U", "_"],
    "U": ["V", "u", "_"],
    "v": ["^", "V"],
    "V": ["^", "v"],
    "w": ["W", "vv"],
    "W": ["w", "VV"],
    "x": ["%", "*", "X"],
    "X": ["%", "*", "x"],
    "y": ["?", "Y"],
    "Y": ["?", "y"],
    "z": ["2", "%", "Z"],
    "Z": ["2", "%", "z"],
    }
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


for i in range (0,4):
    
    print(sub_letters("Lyndong") + generate_random())
    
    
    
    
    
    
    
    
    

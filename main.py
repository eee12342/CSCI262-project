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
print(space_calc("fghbgvrffwefwfw"))
    
    
    
    

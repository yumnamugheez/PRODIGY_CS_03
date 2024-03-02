import re

def check_password_strength(password):
    # Define criteria for password strength
    length_criteria = 8
    uppercase_criteria = re.compile(r'[A-Z]')
    lowercase_criteria = re.compile(r'[a-z]')
    number_criteria = re.compile(r'[0-9]')
    special_character_criteria = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')

    # Check password against criteria
    length_check = len(password) >= length_criteria
    uppercase_check = bool(uppercase_criteria.search(password))
    lowercase_check = bool(lowercase_criteria.search(password))
    number_check = bool(number_criteria.search(password))
    special_character_check = bool(special_character_criteria.search(password))

    # Calculate overall strength score
    strength_score = sum([length_check, uppercase_check, lowercase_check, number_check, special_character_check])

    # Provide feedback to the user based on the strength score
    if strength_score == 5:
        return "Password is strong!"
    elif strength_score >= 3:
        return "Password is moderately strong."
    elif strength_score >= 1:
        return "Password is weak. Consider improving it."
    else:
        return "Password does not meet minimum criteria."

def main():
    password = input("Enter your password: ")
    strength_feedback = check_password_strength(password)
    print(strength_feedback)

if __name__ == "__main__":
    main()

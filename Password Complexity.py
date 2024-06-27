import re
def check_password_complexity(password):
    # Define regex patterns for different criteria
    len_regex = r'.{8,}'  # At least 8 characters long
    uppercase_regex = r'[A-Z]'  # Contains uppercase letter
    lowercase_regex = r'[a-z]'  # Contains lowercase letter
    digit_regex = r'\d'  # Contains digit
    special_char_regex = r'[\W_]'  # Contains special character
# Check if password meets all criteria
    if (re.search(len_regex, password) and
        re.search(uppercase_regex, password) and
        re.search(lowercase_regex, password) and
        re.search(digit_regex, password) and
        re.search(special_char_regex, password)):
        return True
    else:
        return False
# Example usage:
if __name__ == "__main__":
    password = input("Enter your password: ")
    if check_password_complexity(password):
        print("Password is strong and meets complexity criteria.")
    else:
        print("Password does not meet complexity criteria. Please ensure it is at least 8 characters long and includes uppercase letters, lowercase letters, digits, and special characters.")

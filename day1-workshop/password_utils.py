def check_password_length(password):
    return len(password) >= 6

def check_uppercase(password):
    return any(ch.isupper() for ch in password)

def check_lowercase(password):
    return any(ch.islower() for ch in password)

def check_digit(password):
    return any(ch.isdigit() for ch in password)

def is_valid_password(password):
    return (check_password_length(password) 
            and 
            check_uppercase(password)
            and
            check_lowercase(password)
            and
            check_digit(password)
            )

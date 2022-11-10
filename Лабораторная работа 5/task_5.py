import random
import string
n = 8

uppercase_string = string.ascii_uppercase
lowercase_string = string.ascii_lowercase
digits_string = string.digits
password_sample = ''.join((uppercase_string, lowercase_string, digits_string))

def get_random_password() -> str:
    generated_password = random.sample(password_sample, n)
    return ''.join(generated_password)

print(get_random_password())
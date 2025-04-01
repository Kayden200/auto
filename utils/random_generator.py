import random
import string

def generate_random_name():
    first_names = ["John", "Emily", "Michael", "Sarah", "David", "Emma"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller"]
    return random.choice(first_names), random.choice(last_names)

def generate_random_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=12))

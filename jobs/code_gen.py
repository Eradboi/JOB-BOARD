import random, string


def create_slug_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))


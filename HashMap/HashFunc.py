# Getting Hash value for a key


def get_hash(key):
    sum = 0
    for x in key:
        sum += ord(x)

    return sum % 100

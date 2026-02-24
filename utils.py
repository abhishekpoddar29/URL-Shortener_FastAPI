import random
import string

def gen_short_url(length: int=6)->str:
    char=string.ascii_lowercase +string.digits
    short_url=''.join(random.choice(char) for _ in range(length))
    return short_url


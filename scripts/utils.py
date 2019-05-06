import re
import string

# ---------- REMOVE PUNCTUATION FROM STRING -----------
def is_punct(t):
    return re.match(f'[{string.punctuation}]+$', t) is not None

# ---------- GET COUNTRY FROM LOCATION TAG ------------
def get_country(location):
    fields = location.split(', ')
    return fields[-1] if len(fields) > 1 else 'Unknown'

# ---------- GET CLEAN LOCATION FROM LOCATION TAG ------------
def get_cleanlocation(location):
    fields = location.split(', ')
    return ', '.join(fields[-2:]) if len(fields) > 2 else location
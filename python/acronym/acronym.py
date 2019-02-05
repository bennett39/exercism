import re

def abbreviate(words):
    return ''.join(list_first_letters(clean_string(words))).upper()

def clean_string(string):
    return re.sub(r"['_]", '', string)

def list_first_letters(string):
    return re.findall(r"\b[A-Za-z]", string)

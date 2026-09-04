"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Return the title in title case."""
    return title.title()

def check_sentence_ending(sentence):
    """Return True if the sentence ends with a period."""
    return sentence.endswith('.')

def clean_up_spacing(sentence):
    """Remove extra whitespace from the beginning and end of the sentence."""
    return sentence.strip()

def replace_word_choice(sentence, old_word, new_word):
    """Replace all instances of old_word with new_word in the sentence."""
    return sentence.replace(old_word, new_word)
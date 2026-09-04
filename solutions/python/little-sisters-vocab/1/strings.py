"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    return "un"+word

def make_word_groups(vocab_words):
    """Return a string with the prefix applied to each word."""
    prefix = vocab_words[0]
    
    prefixed_words = [prefix + word for word in vocab_words[1:]]
    
    all_parts = [prefix] + prefixed_words
    
    return ' :: '.join(all_parts)
def remove_suffix_ness(word):
    """Return the root word by removing the 'ness' suffix and restoring 'y' if needed."""
    
    root_word = word[:-4]
    if root_word.endswith('i'):
        root_word = root_word[:-1] + 'y'
        
    return root_word
def adjective_to_verb(sentence, index):
    """Extract the adjective from the sentence and turn it into a verb."""
    words = sentence.split()
    
    adjective = words[index]
    
    adjective = adjective.strip('.,!?')
    
    return adjective + 'en'
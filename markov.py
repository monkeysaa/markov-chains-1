"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path, 'r') as f:
        file_string = f.read()

    return file_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    
    counter = 0
    for word in words[2:-1]:
        tup = (words[counter], words[counter + 1])
        if tup in chains:
            chains[tup].append(word)
        else:
            chains[tup] = [word]
        counter += 1
    
    # Add final key:value pair
    tup = (words[counter], words[counter+1])
    chains[tup] = [words[-1]]
        
    return chains

def make_tri_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2, word3)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each trigram (except the last) will be a key in chains.
    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there,' 'mary')]
        ['hi']

        >>> chains[('hi', 'there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    
    counter = 0
    # for n-grams, [start = n:-1]
    for word in words[3:-1]:
        # for n-grams, this would need to be looped, with highest
        # entry as words[counter + n-1]
        tup = (words[counter], words[counter + 1], words[counter + 2]) 
        if tup in chains:
            chains[tup].append(word)
        else:
            chains[tup] = [word]
        counter += 1
    
    # Must final tuple must be handled differently?
    # edit tup for n-grams
    tup = (words[counter], words[counter+1], words[counter+2])
    chains[tup] = [words[-1]]
        
    return chains


def make_text(chains):
    """Return text from chains."""
    
    capital_keys = []
    for c in chains:
        if c[0][0].isupper():
            capital_keys.append(c)

    link = choice(capital_keys)
    # longer for n-gram
    words = [link[0], link[1], link[2]]

    while link in chains:
        next_word = choice(chains[link])
        words.append(next_word)
        # longer for n-gram
        link = (link[1], link[2], next_word)

    return ' '.join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
# for n-grams, use updated function
chains = make_tri_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
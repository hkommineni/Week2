import itertools
import string
import base64


"""
    Author: Harish Kommineni

"""
# xor key with data, repeating key as and when necessary
def xor_data(solution, text):
    if len(solution) == 1:
        key = ord(solution)
        return ''.join(chr(ord(x) ^ key) for x in text)
    series = itertools.cycle(solution)
    return ''.join(chr(ord(x) ^ ord(y)) for x,y in itertools.izip(text, series))

ok = set(string.ascii_letters + ' ')

# ratio of ascii_letters and space to total length of the string
def ratio_count(s):
    count = sum(1 for x in s if x in ok)
    return count / float(len(s))

# This is to find the arithematic mean
def sum(distances):
    return sum(distances) / float(len(distances))

#
def pair(iterator):
    first_element, second_element = itertools.tee(iterator)
    next(second_element, None)
    return itertools.izip(first_element, second_element)

def genearte_distances(maxlen, blockcount, fdist, ciphertext):
    "for each keysize, yield mean of distances for first blockcount blocks"
    for keysize in range(1, maxlen+1):
        blocks = list(grouper(keysize, ciphertext))
        distances = [fdist(s1, s2) / float(keysize) for s1, s2 in pair(blocks[:blockcount])]
        yield sum(distances), keysize


#http://docs.python.org/2/library/itertools.html#recipes
def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)

# count bits that are different
def hamming(string1, string2):
    return sum(bin(ord(x) ^ ord(y)).count('1') for x,y in zip(string1, string2))

# This method returns list of decodings that are counted
def score_decodings(solutions, score_count, text):
    counts = []
    for key in solutions:
        plain_text = xor_data(key, text)
        score = score_count(plain_text)
        counts.append((score, key, plain_text))
    return sorted(counts, reverse=True)

# This is the main method that solves the problem
def hamming_problem():

    with open('w2p2.txt') as f:
        ciphertext = f.read()

        # Convert the cipher text to byte array.
        bytes = str.encode(ciphertext)
        base64.b64encode(bytes)

    groups = zip(*grouper(29, ciphertext, '\00'))
    blocks = [''.join(block) for block in groups]
    keys = [chr(x) for x in range(256)]

    key = []
    for block in blocks:
        best = score_decodings(keys, ratio_count, block)[0]
        key.append(best[1])

    key = ''.join(key)
    print (xor_data(key, ciphertext))
    print("Key: '%s'" % key)


if __name__ == '__main__':
    hamming_problem();
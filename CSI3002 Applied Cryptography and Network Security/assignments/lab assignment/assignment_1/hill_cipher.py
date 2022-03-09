import string
from collections import OrderedDict
import numpy as np
from ordered_set import OrderedSet
import pymatrix

def key_text_rule(key):
    for j in range(len(key)):
        for i in range(len(key)):
            if ((i%2==0) and (i+1!=len(key))):
                if ((key[i]) == (key[i+1])): 
                    near = i+1
                    key = key[:near] + 'x' + key[near:]
                    break

    if (len(key)%2!=0):
        key = key[:len(key)+1] + 'z'
        return key
    else:
        return key

if __name__ == '__main__':

    n = 2  ## input-1
    key = 'test'    ## input-2

    small_dict = dict()

    for index, letter in enumerate(string.ascii_lowercase):
           small_dict[letter] = index + 0

    plain_text = key_text_rule('welcome')  ## input-3
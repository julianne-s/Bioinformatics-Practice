# given a string of dna, return the reverse compliment string

import doctest

def reversecompliment(s):
    '''
    >>> reversecompliment("AAAACCCGGT")
    ACCGGGTTTT
    '''
    
    #initialize new compliment string
    sc = ''
    
    #iterate through each character in the DNA string, and add the compliment to the new DNA string
    for char in s:
        if char == 'A':
            sc += 'T'
        elif char == 'C':
            sc += 'G'           
        elif char == 'G':
            sc += 'C'    
        elif char == 'T':
            sc += 'A'     
    #initialize new reverse compliment string
    scr = sc[::-1]
    #print reverse compliment string
    print(scr)
    
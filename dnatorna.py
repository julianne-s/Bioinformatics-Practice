#create a function that takes a string of DNA (t) and returns a corresponding string of RNA (u)

import doctest

def dnatorna(t):
    '''
    >>> dnatorna("GATGGAACTTGACTACGTAAATT")
    GAUGGAACUUGACUACGUAAAUU
    '''
    
    #initialize RNA string
    u = ''
    
    #iterate through each character in the DNA string, and add the corresponding RNA letter
    for char in t:
        if char == 'A':
            u += 'A'
        elif char == 'C':
            u += 'C'           
        elif char == 'G':
            u += 'G'    
        elif char == 'T':
            u += 'U'     
     #print the resulting RNA string
    print(u)
    
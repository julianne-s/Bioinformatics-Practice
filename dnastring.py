import doctest


def dnastring(dna):
    '''
    >>> dnastring("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
    20 12 17 21
    '''
    # declare each variable, representing the count of nucleotides
    sumA = 0
    sumC = 0
    sumG = 0
    sumT = 0
    # iterate over each character in the string of dna & add 1 for each character
    for char in dna:
        if char == 'A':
            sumA += 1
        elif char == 'C':
            sumC += 1           
        elif char == 'G':
            sumG += 1    
        elif char == 'T':
            sumT += 1
    # print the resulting number of nucleotides in a given string        
    print(sumA, sumC, sumG, sumT)

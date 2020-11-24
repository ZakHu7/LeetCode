def flip(n):
    ## flip one bit to form longest chain of 1s

    a = bin(n)[2:]
    longest = 0
    current = 0
    flipped = False
    flippedLength = 0

    print(a)
    
    for c in a:
        if c == '1':
            current += 1
        else:
            if flipped:
                current -= flippedLength
                current += 1
            else:
                current += 1
                flipped = True
                flippedLength = current
        longest = max(longest, current)

    return longest

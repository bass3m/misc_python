from operator import itemgetter

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # some debugs, removed with itemgetter :)
    if text:
        text = text.upper()
        return (itemgetter(0,1)
                (sorted([(i,j+1,j+1-i,text[i:j+1]) 
                    for i in xrange(len(text)) 
                    for j in xrange(len(text)+1) if j > i and text[i:j] == text[j:i:-1]], 
                    key=itemgetter(2),reverse=True)[0]))
    else:
        return (0,0)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()

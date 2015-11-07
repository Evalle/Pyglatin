pyg = 'ay'
original = raw_input('Please, enter your word:')
word = original.lower()
first = word[0]
new_vowel = word + pyg # if first letter is vowel
new_consonant = word[1:] + first + pyg # if first letter is consonant

if len(original) > 0 and original.isalpha():
    if first == "a" or first == "e" or first == "i" or first ==  "o" or first == "u": 
        print "Ok, your word is VOWEL" 
        print "And your Pyglatin word is: " + new_vowel
    else:
        print "Ok, your word is starting with CONSONANT"
        print "And your Pyglatin word is: " + new_consonant
else:
    print 'empty'

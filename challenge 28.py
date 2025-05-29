#display the sentence & number
sentence=("Here is a sentence. How many letter 'e''s are there in it?")
numberE=0
for letter in sentence:
    if letter in "e":
        numberE +=1
        print("The number of e's in the sentence is:",numberE)
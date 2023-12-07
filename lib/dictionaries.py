
def word_frequency(sentence):
    # initialize empty dictionary
    frequencyDictionary = {}
    
    # split sentence where there is space
    splitSentence = sentence.split(" ")

    # iterate splitSentence
    for item in splitSentence:
        if item in frequencyDictionary:
            frequencyDictionary[item] += 1
        else:
            # add item to dictionary
            frequencyDictionary.update({item: 1})

    return frequencyDictionary

# test 
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

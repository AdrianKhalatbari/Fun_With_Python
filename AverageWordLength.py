import re


def calculateAverage(sentence):
    sentence = re.sub(r'[^a-zA-Z\d\s]', u' ', sentence, flags=re.UNICODE)
    sentence = re.split(' ', sentence)
    sentence = list(filter(None, sentence))
    wordLen = 0
    for word in sentence:
        if word != '':
            wordLen = wordLen + len(word)
    return round((wordLen / len(sentence)), 2)


# /////////////////////Test assignment example
def test_case_1():
    input = 'The quick brown fox jumps over the lazy dog'
    print('User input is:', input)
    assert calculateAverage(input) == 3.89, "Test_case_1 Should be 3.89"
    print('The average of word length is:', calculateAverage(input))
    print('-------------------------------')


# /////////////////////Test assignment example
def test_case_2():
    input = 'All sentences might...not be punctually, correct.'
    print('User input is:', input)
    assert calculateAverage(input) == 5.57, "Test_case_2 Should be 5.57"
    print('The average of word length is:', calculateAverage(input))
    print('-------------------------------')


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    print("Everything passed")

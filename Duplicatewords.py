from collections import Counter

def firstRepeat(input):
    words = input.split(' ')
    counts = Counter(words)
    for word in words:
        if counts[word] > 1:
            print(word)
            return

if __name__ == "__main__": 
    
    input_str = 'Ravi had been saying that he had been there'
    firstRepeat(input_str)
    
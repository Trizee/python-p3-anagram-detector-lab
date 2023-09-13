# your code goes here!

class Anagram:

    def __init__(self,word):
        self.word = word

    def match(self, array):
        arr = []
        for i in array:
            if sorted(i) == sorted(self.word):
                arr.append(i)
                print(arr)
        return arr

    
listen = Anagram('listen')

listen.match(['enlists', 'silent', 'inlets', 'banana'])

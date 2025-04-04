from copy import copy

class Wordplay():
    def __init__(self, words = None):
        if words is None:
            self.words = []
        else:
            self.words = copy(words)

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        out_list = []
        if self.words:
            out_list = [word for word in self.words if len(word) == n]
        return out_list


    def only(self, *args):
        args = set(args)
        out_list = []
        if self.words:
            for word in self.words:
                if len(word) == 1:
                    if word in args:
                        out_list.append(word)
                temp_word = set(word)
                if len(args ^ temp_word) == 0:
                    out_list.append(word)
        return out_list


    def avoid(self, *args):
        args = set(args)
        out_list = []
        if self.words:
            for word in self.words:
                temp_word = set(word)
                if len(args & temp_word) == 0:
                    out_list.append(word)
        return out_list

wordplay = Wordplay(['o', 'to', 'otto', 'abc', 't', 'dsa', 'a', 'b'])

print(wordplay.only('o', 't'))
print(wordplay.avoid('o', 't'))
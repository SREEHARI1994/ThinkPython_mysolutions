"""
this is the solution to the excercise on finding anagrams from word list, 
for solution to second part refer anagram_sets.py
"""
def make_word_list():
    words=[]
    fin=open("words.txt")
    for line in fin:
        words.append(line.strip().lower())
    return words

def find_anagrams(words):
    d={}
    for word in words:
        t=list(word)
        t=sorted(t)
        k=tuple(t)
        
        if k not in d:
            d[k]=[word]
        else:
            d[k].append(word)
    return d


if __name__ == "__main__":
    word_list=make_word_list()
   
    res_dict=find_anagrams(word_list)
    for value in res_dict.values():
        if len(value) > 1:
            print(len(value),value)



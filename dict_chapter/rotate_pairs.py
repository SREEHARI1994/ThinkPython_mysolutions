def make_word_dict():
    d={}
    f=open("words.txt")
    for line in f:
        word=line.strip().lower()
        d[word]=""
  
    return d


def rotate_word(word,n):
    rotated_word=""
    for letter in word:
        letter_code=ord(letter)
        start=ord('a')
        c = letter_code - start
        i = (c + n) % 26 + start
        rotated_word=rotated_word+ chr(i)
    return rotated_word


def find_rotate_pairs(word_dict,word):
    for i in range(1,14):
        rotated_word=rotate_word(word,i)
        if rotated_word in word_dict:
            print(word,i,rotated_word)


if __name__ == "__main__":
    
    word_dict=make_word_dict()

    for word in word_dict:
        

        find_rotate_pairs(word_dict,word)
    

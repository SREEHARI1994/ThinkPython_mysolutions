from rotate_pairs import make_word_dict
from pronounce import read_dictionary

def check_homophone(d):
    pronounce_dict=read_dictionary()
    
    for original_word in d:
        first_word=original_word[1:]
        second_word=original_word[0]+original_word[2:]
        if first_word not in d and second_word not in d:
            continue
        if pronounce_dict.get(original_word,0)==pronounce_dict.get(first_word,1)  and pronounce_dict.get(original_word,0)== pronounce_dict.get(second_word,1):
            print(original_word,first_word,second_word)
            
if __name__ ==  "__main__" :
    word_dict=make_word_dict()
    check_homophone(word_dict)
    

    


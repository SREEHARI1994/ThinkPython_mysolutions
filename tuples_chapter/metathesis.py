import anagram

def methathesis(d):
    for anagram_sets in d.values():
        anagram_sets.sort()
        for word1 in anagram_sets:
            for word2 in anagram_sets:
                # '<' operation to ensure each word is compared with the rest of words so as to avoid
                #repetetion
                if word1<word2 and no_of_diffLetters(word1,word2)==2:
                    print(word1,word2)

def no_of_diffLetters(word1,word2):
    #two words are anagrams found from previous excercises and hence it is assumed that they are off same length
    count=0
    for l in range(len(word1)):
        if word1[l]!=word2[l]:
            count += 1
    return count

if __name__== "__main__":
    word_list=anagram.make_word_list()
    res_dict=anagram.find_anagrams(word_list)
    methathesis(res_dict)
"""
this is the solution to the excercise on finding anagrams from word list, 
"""
def make_word_list(file_name):
    words=[]
    fin=open(file_name)
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

def print_anagrams(d):
	for value in d.values():
		if len(value) > 1:
			print(len(value),value)


def print_anagram_inorder(d):
	res_list=[]
	for value in d.values():
		if len(value) > 1:
			res_list.append((len(value),value))
	res_list.sort()
	for res in res_list:
		print(res)

def filtered_dict(d,n):
	new_dict={}
	for key,value in d.items():
		if len(key)==n:
			new_dict[key]=value
	return new_dict

if __name__ == "__main__":
	word_list=make_word_list("words.txt")
	res_dict=find_anagrams(word_list)
	print_anagrams(res_dict)
	print("Now printing anagrams in order of increasing length\n")
	print_anagram_inorder(res_dict)
	print("solution to bingo problem\n")
	bingo_dict=filtered_dict(res_dict,8)
	
	print_anagram_inorder(bingo_dict)
	print("The end")






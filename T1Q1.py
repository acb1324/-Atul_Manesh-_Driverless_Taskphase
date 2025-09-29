list_count=int(input("Enter the number of words required in the dictionary : "))
list_for_dic=[]

word_no=1

for i in range(list_count):

    strword_no=str(word_no)
    words = input("Enter word"+" "+strword_no+" : ")
    word_no += 1
    list_for_dic.append(words)


all_words = ""
for words in list_for_dic:
    all_words+= (words.lower())

dict1 = {}
for x in all_words:
    if 'a' <= x <= 'z':
        if x in dict1:
            dict1[x] += 1
        else:
            dict1[x] = 1

print(dict1)
class Selection:

    def selection_sort(self,strings):

        length = len(strings)

        for i in range(length):

            lowest = i

            for j in range(i + 1, length):
                if strings[j] < strings[lowest]:
                    lowest = j


            strings[i], strings[lowest] = strings[lowest], strings[i]

        return strings

strings=[]
no_of_strings = int(input("Enter the number of words required to sort : "))
for i in range(no_of_strings):
    words = input("Enter word" + " " + str(i+1) + " : ")
    strings.append(words.lower())
    #because otherwise if any letter of the word is in a different case it will not search for it in Q3
    #it also sorts capital first in the sort function as well so to remove that.3
obj=Selection()
sorted_list=obj.selection_sort(strings)
print(sorted_list)
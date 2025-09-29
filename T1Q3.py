class BinarySearcher:
    def binary_search(self, sorted_list, item):
        low = 0
        high = len(sorted_list)-1
        while low <= high:
            mid = (low+high)//2
            if sorted_list[mid] == item:
                return mid
            elif sorted_list[mid] < item:
                low = mid + 1
            else:
                high = mid - 1
        return -1

from T1Q2 import Selection , sorted_list

item=input("Enter the word to be searched : ").lower()
search=BinarySearcher()
index=search.binary_search(sorted_list, item)

if index == -1 :
    print("Sorry, the word is not present in the list")
else:
    print("Your sorted list is "+ str(sorted_list) )
    print(item+" is found at index "+str(index))

#it returns only lower case values to prevent the program from stopping if a different case word is given

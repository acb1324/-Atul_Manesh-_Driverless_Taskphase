from T2Q2 import creating_list

n=int(input("Enter the number of integers required in the list : "))
terms_string = input(f"Enter the "+str(n)+" integers : ")
splitting_terms = terms_string.split()
terms = [int(x) for x in splitting_terms]

def binary_search(sorted_list, term):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == term:
            return mid
        elif sorted_list[mid] < term:
            low = mid + 1
        else:
            high = mid - 1
    return low

def improved_hashing(terms):
    hash_table = [[] for _ in range(10)]
    for term in terms:
        index = term % 10
        sublist = hash_table[index]
        insert_pos = binary_search(sublist, term)
        sublist.insert(insert_pos, term)
    print("Your improved Hash table is " + str(hash_table))

creating_list(terms)
improved_hashing(terms)
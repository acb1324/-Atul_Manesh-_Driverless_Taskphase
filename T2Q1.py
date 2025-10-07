n=int(input("Enter the number of integers required in the list : "))
terms_string = input(f"Enter the "+str(n)+" integers : ")
splitting_terms = terms_string.split()
terms = [int(x) for x in splitting_terms]

def creating_list():
    the_2d_list = [[],[]]
    for term in terms:
        remainder = term % 10
        if remainder == 0:
            the_2d_list[0].append(term)
        elif remainder == 1:
            the_2d_list[1].append(term)

    print("Your 2D List is : "+str(the_2d_list))

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
        insert_position = binary_search(sublist, term)
        sublist.insert(insert_position, term)
    print("Your improved Hash table is " + str(hash_table))

creating_list()
improved_hashing(terms)
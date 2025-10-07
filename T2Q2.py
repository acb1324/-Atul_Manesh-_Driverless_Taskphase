def creating_list(terms):
    the_2d_list = [[],[]]
    for term in terms:
        remainder = term % 10
        if remainder == 0:
            the_2d_list[0].append(term)
        elif remainder == 1:
            the_2d_list[1].append(term)

    print("Your 2D List is : "+str(the_2d_list))
    return the_2d_list



def hashing(terms):
    hash_table = [[] for _ in range(10)]
    for term in terms:
        index = term % 10
        hash_table[index].append(term)
    print("Your Hash table is " + str(hash_table))
    return hash_table

if __name__ == "__main__":
    n=int(input("Enter the number of integers required in the list : "))
    terms_string = input(f"Enter the "+str(n)+" integers : ")
    splitting_terms = terms_string.split()
    terms = [int(x) for x in splitting_terms]

    creating_list(terms)
    hashing(terms)
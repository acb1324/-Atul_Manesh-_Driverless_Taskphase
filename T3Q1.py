def distance_calculation(point, ref_point):
    return abs(point[0] - ref_point[0]) + abs(point[1] - ref_point[1])


n=int(input("Enter the number of coordinates : "))

coordinate_list=[]
for i in range(n):
    item_input=input(f"Enter coordinate {i+1} in the format (x y) : ")
    items = item_input.split()
    item_x=int(items[0])
    item_y=int(items[1])
    coordinate_list.append([item_x,item_y])

reference_input=input("Enter the reference point coordinates in the format (x y) : ")
ref=reference_input.split()
reference_x=int(ref[0])
reference_y=int(ref[1])
ref_point=[reference_x,reference_y]

sorted_list=sorted(coordinate_list, key=lambda point: distance_calculation(point, ref_point))

print("The coordinates sorted in order of distance from reference is : ", sorted_list)


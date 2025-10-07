import csv

with open('QuestionTwo.csv', 'r') as csvfile:
 reader = [row[0].split(',') for row in csv.reader(csvfile)]
sorted_rows= sorted(reader, key=lambda row: int(row[0]))

modified_rows=[]
for index,row in enumerate(sorted_rows):
    if index % 2 == 1:
        modified_rows.append(row)

all_names = ''.join(row[1].strip() for row in modified_rows)

def min_ascii_diff(all_names):
    if len(all_names) < 2:
        return 0
    min_diff = abs(ord(all_names[1]) - ord(all_names[0]))
    for i in range(1, len(all_names) - 1):
        diff = abs(ord(all_names[i + 1]) - ord(all_names[i]))
        if diff < min_diff:
            min_diff = diff
    return min_diff



with open('Q2sortedrows.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(sorted_rows)

with open('Q2result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(modified_rows)

print("The original list is : ",reader)
print("The sorted list is : ",sorted_rows)
print("The modified list is : ",modified_rows)
print("The string with all the names is : ",all_names)
print("The minimum absolute ASCII difference in the string is : ",min_ascii_diff(all_names))

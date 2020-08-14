def insertion_sort(listN):
    for i, num in enumerate(listN):
        key = num
        j = i-1

        while (j >= 0 and listN[j] > key):
            listN[j+1] = listN[j]
            j=j-1
        
        listN[j+1] = key
    
    return listN


n = input("Len of the listN: ")
n = int(n)

listN = []

for i in range(n):
    num = input("Number: ")
    listN.append(int(num))

print("Unordered elements")
print(listN)

listS = insertion_sort(listN)

print("Elements sorted")
print(listS)

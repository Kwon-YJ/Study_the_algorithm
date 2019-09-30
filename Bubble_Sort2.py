list_= list(map(int, input().split()))

for j in range(len(list_)-1):
    for i in range(len(list_)-j-1):
        if list_[i] > list_[i+1]:
            temp = list_[i]
            list_[i] = list_[i+1]
            list_[i+1] = temp

print(list_)


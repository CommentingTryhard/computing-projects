def largest_even(numbers: list):
    holder = []
    flag = False
    for i in numbers:
        if i%2 == 0:
            holder.append(i)
            flag = True
        if flag == False:
            return -1
    return max(holder)
    # write your code
    # show your comment 
    # return a value

print(largest_even([1,2,3,4]))
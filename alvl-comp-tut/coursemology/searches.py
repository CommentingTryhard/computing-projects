from colourist import Color
import time
def prints(string):
    for i in string:
        print(i, end="")
        time.sleep(0.1)
    print(end=" ")

prints("Welcome to this tutorial on searches and algorithms.".format(Color.CYAN))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i -1 #j is the previous element
        while j >=0 and key < arr[j]: #checks if j is not negative, and if previous element is larger than current element
            arr[j+1] == arr[j] #rightward shift
            j-=1 #move leftwards
        arr[j+1] == key #once it has been sorted, new key is the next element to shift
    return arr

def bubble_sort(arr):
    for i in range(len(arr)-1):
        swapped = False
        for j in range(0, len(arr)-i-1): #-i because as i loops, there are less elements to sort through. -1 for index
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: # as if swapped = False, it means that it has already been fully sorted.
            break
    return arr

def merge_sort(arr):
    def pieceback(L, R):
        master = []
        i=j=0 #list index for left and right
        while (i<len(L)) and (j<len(R)): #while indexs do not out run the list
            if L[i] < R[j]: #checking if the left/right is larger
                master.append(L[i]) #smaller one is appended
                i+=1
            else:
                master.append(R[j])
                j+=1
        master.extend(L[i:]) #it appends the last character back in
        master.extend(R[j:])
        return master
    def msort(arr):
        if len(arr) <=1:
            return arr
        L = arr[:len(arr)//2] #leftward list
        R = arr[len(arr)//2:] #rightward list
        return pieceback(msort(L), msort(R)) #functions recursively as pieceback sorts through and literally piecesback the recursived lists
    
def quick_sort(arr):
    if len(arr) <=1:
        return arr
    mid = arr[0] #taking a arbitirary point as mid
    left = [less for less in arr[1:] if less < mid]
    right = [more for more in arr[1:] if more > mid]
    return quick_sort(left) + [mid] + quick_sort(right)

def linear_search(subj, arr):
    for i in arr:
        if i == subj:
            return arr.index(i)
    return False

def binary_search(subj, arr): #ints or ordered elements only
    mid = arr[len(arr)//2]
    if subj == mid:
        return subj
    if mid << subj: binary_search(subj, arr[mid:])
    else: return binary_search(subj, arr[:mid])



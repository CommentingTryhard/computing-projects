array = [1,7,4,6,9,2,3,5,8,0]
def split(array):
    left = array[:len(array)//2+1]
    right = array[len(array)//2+1:]
    array = [left,right]
    return split(array)


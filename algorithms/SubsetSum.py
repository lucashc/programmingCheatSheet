# Maximum subset sum (contiguous)
#Option 1:
def subsetsum(array,num):
    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)

#Option 2:
# use a binary number (represented as string) as a mask
def mask(lst, m):
    # pad number to create a valid selection mask
    # according to definition in the solution laid out
    m = m.zfill(len(lst))
    return map(lambda x: x[0], filter(lambda x: x[1] != '0', zip(lst, m)))

def subset_sum(lst, target):
    # there are 2^n binary numbers with length of the original list
    for i in range(2**len(lst)):
        # create the pick corresponsing to current number
        pick = mask(lst, bin(i)[2:])
        if sum(pick) == target:
            yield pick

# use 'list' to unpack the generator
from operator import itemgetter
#data = ((1,), (3,))
#map(itemgetter(0), data)
lst = subsetsum([1,2,3,4,5], 7)
print(lst)

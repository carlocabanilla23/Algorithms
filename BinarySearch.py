
items = [1,2,3,4,5,6,7,8,9,10,11]

def BinarySearch(item,itemlist):
    low = 0
    high = len(itemlist)
    mid = (high-low)/2

    if (itemlist[mid] < item):
       for i in range (mid,high):
            if(itemlist[i] == item):
                return i
    elif(itemlist[mid] > item):
        for k in range (mid,low-1,-1):
            if(itemlist[k] == item):
                return k

    else:
                return mid

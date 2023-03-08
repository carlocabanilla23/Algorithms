
def partition(num,i,k):
  low = i
  high = k
  mid = i + (k-i)/2
  pivot = num[mid]
  done = False

  while(done):
      while(num[low]<pivot):
          low = low + 1
      while(pivot < num[high]):
          high = high - 1
      if(low >= high):
          done = True
      else:
          temp = num[low]
          num[low] = num[high]
          num[high] = temp

          low = low + 1
          high = high - 1


      return high




def QuickSort(num,i,k):

    j =  partition(num,i,k)

    if(i>=k):
        return

    QuickSort(num,i,j)
    QuickSort(num,j+1,k)



num = {12,4,23,53,6,76,123}
numSize = 7

QuickSort(num,0,numSize-1)

for i in len(num):
    print(num[i] + " ")

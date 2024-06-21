def QuickSort1(arr,left,right):
    i = left
    j = right
    if i>=j:
        return
    pivot = arr[left]
    while i<j:
        while i<j and arr[j]>=pivot:
            j-=1
        arr[i]=arr[j]
        while i<j and arr[i]<pivot:
            i+=1
        arr[j]=arr[i]
    arr[i]=pivot
    QuickSort1(arr,left,i-1)
    QuickSort1(arr,i+1,right)


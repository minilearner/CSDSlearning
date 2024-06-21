def QuickSort(arr,left,right):
    if left<right:
        i = left
        j = right-1
        pivot = arr[right]

        while i<=j:
            while arr[i]<pivot and i<=right:
                i+=1
            while arr[j]>=pivot and j>=left:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[i],arr[right]=arr[right],arr[i]

        QuickSort(arr,left,i-1)
        QuickSort(arr,i+1,right)

arr = [22, 11, 88, 66, 55, 77, 33, 44]
QuickSort(arr, 0, len(arr) - 1)
print(arr)
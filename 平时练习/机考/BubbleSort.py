def bubbleSort(arr):
    s = len(arr)

    for i in range(s-1,-1,-1):
        swapped = False
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swapped = True
        if not swapped:
            break
# O(n^2)
# 
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(arr)
    print(' '.join(map(str, arr)))


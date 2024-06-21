def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i,n):
            if arr[j]<arr[min_index]:
                min_index =j
        arr[min_index],arr[i]=arr[i],arr[min_index]

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    SelectionSort(arr)
    print(' '.join(map(str, arr)))
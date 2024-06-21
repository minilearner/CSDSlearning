# 写递归式的排序代码，一定要假设已经写完了
def MergeSort(arr):
    n = len(arr)
    if n>1:
        mid = n//2
        L = arr[:mid]
        R = arr[mid:]
        MergeSort(L)
        MergeSort(R)
        left,right = 0,0
        k = 0
        while left<len(L) and right<len(R):
            if L[left]<R[right]:
                arr[k]=L[left]
                left+=1
            else:
                arr[k]=R[right]
                right+=1
            k+=1
        while left<len(L):
            arr[k]=L[left]
            left+=1
            k+=1
        while right<len(R):
            arr[k]=R[right]
            right+=1
            k+=1
if __name__ == '__main__':
 arr = [12, 11, 13, 5, 6, 7]
 MergeSort(arr)
 print(' '.join(map(str, arr)))



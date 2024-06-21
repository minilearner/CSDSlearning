class BinHeap:
    def __init__(self):
        #由于堆用列表表示时需要从1开始，所以预先开一个0数组
        self.heaplist = [0]
        self.currentsize = 0


    def percUp(self, i):
        #功能时把指定位置的结点合理移动到应该的位置
        while i//2>0:
            flag = True
            if self.heaplist[i]<self.heaplist[i//2]:
                self.heaplist[i],self.heaplist[i//2]=self.heaplist[i//2],self.heaplist[i]
                flag = False
            if flag:
                break
            i=i//2

    def insert(self, k):
        #一旦给堆添加新结构需要把他移动到合适位置
        self.currentsize+=1
        self.heaplist.append(k)
        self.percUp(self.currentsize)

    def percDown(self, i):
        #将指定的点下移至合适的位置
        while i*2<=self.currentsize:
            flag = True
            mc = self.minChild(i)
            if self.heaplist[i]>self.heaplist[mc]:
                self.heaplist[i],self.heaplist[mc]=self.heaplist[mc],self.heaplist[i]
                flag = False
            if flag:
                break
            i = mc

    def minChild(self, i):
        # 找到指定结点的最小的那个子结点
        if 2*i+1>self.currentsize:
            return 2*i
        else:
            return 2*i if self.heaplist[2*i]<self.heaplist[2*i+1] else 2*i+1

    def delMin(self):
        #取出栈顶元素
        s = self.heaplist[1]
        self.heaplist[1]=self.heaplist[self.currentsize]
        self.currentsize-=1
        self.heaplist.pop()
        self.percDown(1)
        return s
        #小心此时堆内只剩一个元素的情况
    def buildHeap(self, alist):
        #给定列表，构建堆对象
        i = len(alist)//2
        self.currentsize = len(alist)
        self.heaplist = [0]+alist
        while i>0:
            self.percDown(i)
            i-=1
n = int(input().strip())
heap = BinHeap()
for i in range(n):
    s=input().strip()
    if s[0]=="1":
        heap.insert(int(s.split()[1]))
    else:
        print(heap.delMin())





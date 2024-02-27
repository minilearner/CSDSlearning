# Assignment #2: 编程练习

Updated 0953 GMT+8 Feb 24, 2024

2024 spring, Complied by ==同学的姓名、院系==



**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知3月1日导入选课名单后启用。**作业写好后，保留在自己手中，待3月1日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：macOS Ventura 13.4.1 (c)

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

### 27653: Fraction类

http://cs101.openjudge.cn/practice/27653/



思路：



##### 代码

```python
# from math import gcd
class Fraction:
    def __init__(self,numer,denom):
        self.numer = numer
        self.denom = denom

    def add(self,frac2):
        tempn = self.numer*frac2.denom+self.denom*frac2.numer
        tempd = self.denom*frac2.denom
        s = gcd(tempn,tempd)
        n = tempn//s
        d = tempd//s
        frac3 = Fraction(n,d)
        return frac3

    def printf(self):
        print(f"{self.numer}/{self.denom}")
n1,d1,n2,d2 = map(int,input().split())
f1 = Fraction(n1,d1)
f2 = Fraction(n2,d2)
f3 = f1.add(f2)
f3.printf()


```



代码运行截图 ==（至少包含有"Accepted"）==



![image-20240227162917436](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240227162917436.png)

### 04110: 圣诞老人的礼物-Santa Clau’s Gifts

greedy/dp, http://cs101.openjudge.cn/practice/04110



思路：



##### 代码

```python
# 
n,w = map(int,input().split())
goods = []
for i in range(n):
    goods.append(list(map(int,input().split())))
goods=sorted(goods,key=lambda x:x[1]/x[0])
cnt = 0
index = 0

while w>0 and index<n:
    if w>=goods[index][1]:
        w-=goods[index][1]
        cnt +=goods[index][0]
    else:
        cnt+=goods[index][0]*w/goods[index][1]
        w=0
    index+=1
print("%.1f"%cnt)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240227163039482](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240227163039482.png)



### 18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/



思路：



##### 代码

```python
# 
_ = int(input())
def main():
    n, m, b = map(int, input().split())
    t_x = {}
    for j in range(n):
        t, x = map(int, input().split())
        if t in t_x:
            t_x[t].append(x)
        else:
            t_x[t] = [x]
    time = list(t_x.keys())
    time.sort()
    for t in time:
        y = 0
        if len(t_x[t]) <= m:
            y = sum(t_x[t])
        else:
            t_x[t].sort()
            t_x[t].reverse()
            y = sum(t_x[t][:m])
        b -= y
        if b <= 0:
            print(t)
            return
    print("alive")
for i in range(_):
    main()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240227163130867](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240227163130867.png)



### 230B. T-primes

binary search/implementation/math/number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：



##### 代码

```python
# 
M = 1000000
Num = [True]*M
su = []
for i in range(M):
    if Num[i]==True:
        su.append(i+2)
    index = 0
    while index<len(su) and (i+2)*su[index]-2<M :
        Num[(i+2)*su[index]-2]=False
        if (i+2)%su[index]==0:
            break
        index+=1
 
n = int(input())
s = input().split()
for i in range(n):
    l=int(s[i])**0.5
    if l!=int(l):
        print("NO")
        continue
    if Num[int(l)-2]:
        print("YES")
    else:
        print("NO")
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240227163307084](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240227163307084.png)



### 1364A. XXXXX

brute force/data structures/number theory/two pointers, 1200, https://codeforces.com/problemset/problem/1364/A



思路：



##### 代码

```python
#
n = int(input())
for k in range(n):
    L,x = map(int,input().split())
    shu = list(map(int,input().split()))
    if sum(shu)%x !=0:
        print(L)
        continue
    for i in range(L):
        shu[i]=[1,0][shu[i]%x==0]
 
 
    try:
        x1 = shu.index(1)
    except ValueError:
        print(-1)
        continue
    else:
        shu.reverse()
        x2 = shu.index(1)
        print(L-min(x1+1,x2+1))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==



![image-20240227163347926](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240227163347926.png)

### 18176: 2050年成绩计算

http://cs101.openjudge.cn/practice/18176/



思路：



##### 代码

```python
# 
M = 10000
num = [True]*M

for i in range(102):
    if num[i]:
        k = 2
        while (i+2)*k<(M+2):
            num[(i+2)*k-2]=False
            k+=1
m,n = map(int,input().split())


for i in range(m):
    aa = list(map(int,input().split()))
    cnt = 0
    for x in aa:
        c = x**0.5
        if int(c) == c and c>=2 and  num[int(c)-2]:
            cnt+=x



    if cnt==0:
        print(0)
    else:
        a = cnt/len(aa)
        print("%.2f"%a)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240227163516847](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240227163516847.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==






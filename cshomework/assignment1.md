# Assignment #1: 拉齐大家Python水平

Updated 0940 GMT+8 Feb 19, 2024

2024 spring, Complied by ==同学的姓名、院系==



**说明：**

1）数算课程的先修课是计概，由于计概学习中可能使用了不同的编程语言，而数算课程要求Python语言，因此第一周作业练习Python编程。如果有同学坚持使用C/C++，也可以，但是建议也要会Python语言。

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

### 20742: 泰波拿契數

http://cs101.openjudge.cn/practice/20742/



思路：



##### 代码

```python
# 
shu = [0 for i in range(31)]
shu[1]=1
shu[2]=1
for i in range(3,31):
    shu[i]=shu[i-1]+shu[i-2]+shu[i-3]
print(shu[int(input())])

```



代码运行截图 ==（至少包含有"Accepted"）==



![image-20240220154110272](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240220154110272.png)

### 58A. Chat room

greedy/strings, 1000, http://codeforces.com/problemset/problem/58/A



思路：



##### 代码

```python
# 
s = input()
def chat(s):
    ori = list("hello")
    pos=[-1]
    for i in range(5):
        x = s.find(ori[i],pos[-1]+1)
        if x==-1:
            return "NO"
        pos.append(x)
    return "YES"
 
print(chat(s))
```



代码运行截图 ==（至少包含有"Accepted"）==



![image-20240220154158284](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240220154158284.png)

### 118A. String Task

implementation/strings, 1000, http://codeforces.com/problemset/problem/118/A



思路：



##### 代码

```python
# 
string = input().lower()
 
yuan = ["a","o","e","i","y","u"]
new = ""
for i in string:
    if i not in yuan:
        new+=("."+i)
print(new)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240220154304719](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240220154304719.png)



### 22359: Goldbach Conjecture

http://cs101.openjudge.cn/practice/22359/



思路：



##### 代码

```python
# 
pri = [True for i in range(10003)]
pri[0]=False
pri[1]=False
prime = []
for i in range(2,10003):
    if pri[i]:
        prime.append(i)
    for j in prime:
        if i*j>=10003:
            break
        pri[i*j]=False
        if i%j==0:
            break

n = int(input())
for x in prime:
    if pri[n-x]:
        print(x,n-x)
        exit()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==



![image-20240220181756799](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240220181756799.png)

### 23563: 多项式时间复杂度

http://cs101.openjudge.cn/practice/23563/



思路：



##### 代码

```python
# 
n = list(input().split('+'))
a = [x.split('n^') for x in n]
b = sorted(a,key = lambda x : int(x[1]),reverse = True)
for i in b:
    if i[0] != '0' :
        print("n^%s" %i[1])
        break
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240220181818306](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240220181818306.png)



### 24684: 直播计票

http://cs101.openjudge.cn/practice/24684/



思路：



##### 代码

```python
# 
num = [0 for i in range(1000003)]
s = list(map(int,input().split()))
s.sort()
for x in s:
    num[x]+=1
maxn = max(num)
for i in range(0,1000003):
    if num[i]== maxn:
        print(i,end = " ")
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==



![image-20240220182425506](C:\Users\田济维\AppData\Roaming\Typora\typora-user-images\image-20240220182425506.png)

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“数算pre每日选做”、CF、LeetCode、洛谷等网站题目。==

复习一下python




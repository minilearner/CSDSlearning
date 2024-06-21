def tarjan(graph):
    n = len(graph)
    index = 0
    indices = [0]*n
    low_link = [0]*n
    on_stack = [False]*n
    stack = []
    sscs = []
    def dfs(node):
        nonlocal index,indices,low_link,on_stack,stack,sscs
        #说明刚到此节点，首先将此节点加入栈中，初始化其indice和lowlink
        index+=1
        stack.append(node)
        on_stack[node]=True
        indices[node]=index
        low_link[node]=index

        #进一步探索
        for i in graph[node]:
            #如果在栈中，说明形成了环，准备回退
            if on_stack[i]:
                low_link[node]=min(low_link[node],indices[i])
            #没探索过，则继续探索
            elif indices[i]==0:
                dfs(i)
                low_link[node]=min(low_link[node],low_link[i])
            #探索过却不在栈中的情况，只有可能是作为一个强连通单元被删除了，这种情况什么都不用做，因为不可能更新当前节点的indice
            #如果走了，只会把这个强连通单元再记录一遍
        """所有的都探索完了，回到此节点，显然一个强连通单元内所有节点能到的最早的节点是一样的，
        如果此节点所到的最早的节点是自己,则说明该节点是此强连通单元中第一个被拜访的，可以证明若能到达的最早节点相同
        那么必定属于同一个强连通单元，因为所有人都可以到达那个最早的，最早的可以到达所有人"""
        if indices[node]==low_link[node]:
            ssc=[]
            while stack:
                top = stack.pop()
                on_stack[top]=False
                ssc.append(top)
                if top == node:
                    break
            sscs.append(ssc)
    for i in range(n):
        if indices[i]==0:
            dfs(i)
    return sscs
graph = [[1], [2, 4], [3, 5], [0, 6], [5], [4], [7], [5, 6]]
print(tarjan(graph))




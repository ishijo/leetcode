class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dic = {i:[] for i in range(n)}

        for l,r in edges:
            dic[l].append(r)
            dic[r].append(l)

        def cycle(num,prev,visit): # 0
            if not dic[num]:
                return False
            for dep in dic[num]:
                if dep == prev:
                    continue
                if dep in visit:
                    return True
                visit.add(dep)
                if cycle(dep,num,visit):
                    return True
            
            #visit.remove(num)
                
        visit = set([0])

        if not cycle(0,None,visit) and len(visit)==n:
            return True
        return False

'''

{
    0: [1],
    1: [2,3,4],
    2: [3],
    3: [],
    4: []

    0: [1],
    1: [0,2,3,4],
    2: [1,3],
    3: [1,2],
    4: [1]
}

[[0,1],[0,2],[0,3],[1,4]]

{
    0: [1,2,3],
    1: [4],
    2: [],
    3: [],
    4: []
}




'''
        
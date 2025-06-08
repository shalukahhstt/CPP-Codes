def pathcheck(path,startp,endp):
    if startp != path[0][0]:
        return False
    prevp = startp
    for (p1,p2,c) in path:
        if p2 == endp:
            return True
        elif prevp == p1:
            prevp = p2
            print(p1,p2,end=",")
        else:
            return False
    return False

pataf = [('A','B',2),('B','C',3),('C','H',1),('H','D',11),('D','E',7),('E','G',3),('G','F',5)]
print(pathcheck(pataf,'A','F'))
t=[[1,'a',['cat'],2],[[[3]],'dog'],4, 5]
def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt
print(flatten(t))
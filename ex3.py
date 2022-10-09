def cacluate(*args):
    sum(args)
    ave=sum(args)/len(args)
    list=[]
    for i in args:
        if i>ave :
            list.append(i)
    return (ave,list)
print(cacluate(1,2,3,4,5,6))


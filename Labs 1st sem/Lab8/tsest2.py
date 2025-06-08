def MyFun(mylist):
  if len(mylist) > 0:
    mid = len(mylist)//2
    if mylist[mid] < 50:
      return MyFun(mylist[:mid-1]) + 1
    else:
      return MyFun(mylist[mid+1:]) + 1
  else:
    return 1

initlist = [12, 15, 72, 66, 23, 79, 35]
print (MyFun(initlist))
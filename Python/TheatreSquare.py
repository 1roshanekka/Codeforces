# import pdb
# pdb.set_trace()
import math
#1A
n, m, a = map(int, input().split())
count = 0
countx = 0
county = 0

SqArea = n*m
TileArea = a*a
AreaLeft = SqArea-TileArea
#flagstone size is (a x a) meters
countx = math.ceil(n/a)
count = count + countx
if(countx*TileArea!=SqArea):
    county = math.ceil(m/a)
    count = count + county
    print(countx*county)
elif(count*TileArea==SqArea):
    print(count)

'''
else:
    for i in range(n):
        x = x - a
        countx = countx + 1
        count = count + countx
        if(x<0):
            allow = allow +1
        if( -a<=x<n or (count*TileArea>SqArea and allow==1)) :
            continue
        else:
            break
    if(count*TileArea!=SqArea):
        for j in range (m):
            y = y - a
            county = county + 1
            count = count + county
            if(y<0):
                allowy = allowy +1
            if( -a<=y<m or (count*TileArea>SqArea and allowy==1) ):
                continue
            else:
                break
    print(countx*county)
    '''

'''
else:
    for i in range(n):
        x = x + a
        countx = countx + 1
        if( (not x>=n or (n-x>0) ) and count*TileArea!=SqArea) :
            continue
        else:
            break
    if(count*TileArea!=SqArea):
        for j in range (m):
            y = y + a
            county = county + 1
            if( (not y>=m or (m-y>0) ) and count*TileArea!=SqArea) :
                continue
            else:
                break
    print(countx*county)
    '''

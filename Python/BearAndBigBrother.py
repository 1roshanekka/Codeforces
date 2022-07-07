#791A
a,b = map(int, input().split())
#each year a increases weight by 3 
#each year b increases weight by 2
count = 0 
while(a<=b):
    a *= 3
    b *= 2
    count += 1
    # print(f'a = {a} , b = {b}, Count = {count}')
print(count)
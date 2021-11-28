1,1,2,3
x=[20,30,40]
sum=0
for i in x:
    sum=sum+i
print(sum/len(x))
import statistics

mode=statistics.mode(x)
print(mode)

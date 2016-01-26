#!/usr/bin/env python
def fibo(int):
    #Indices 0 & 1 are pre-set; Addition begins at index 2
    fibo_list = [0,1];
    for i in range(2,int):
        #Add previous sum to previous largest integer: (a+b)=sum -> (b+sum)=new_sum -> ... then append to list
        fibo_list.append(fibo_list[i-2]+fibo_list[i-1]);
    return fibo_list;

print(fibo(100)); #Print list 

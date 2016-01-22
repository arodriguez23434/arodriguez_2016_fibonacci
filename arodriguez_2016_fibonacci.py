#Fibonacci Sequence Digits 0-100
def fibo(int):
    a=0;b=0;sum=0;fibo_list=list()
    for i in range(0,int+2): #Indices 0 & 1 are pre-set; Addition begins at index 2
        if i==1:
            sum=1;
        else: #Add previous sum to previous largest integer
            a=b; 
            b=sum;
            sum=a+b; #(a+b)=sum1 -> (b+sum1)=sum2 -> ...
        fibo_list.append(sum)
    return fibo_list

print(fibo(100)) #Print list 

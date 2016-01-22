#Main File; defines function for storing Fibonacci Sequence in a list and printing list
def fibo(int):
    a=0;b=0;sum=0;fibo_list=list()
    for i in range(0,int+2):
        #Indices 0 & 1 are pre-set; Addition begins at index 2
        if i==1: 
            sum=1;
        #Add previous sum to previous largest integer: (a+b)=sum -> (b+sum)=new_sum -> ...
        else:
            a=b; 
            b=sum;
            sum=a+b; 
        fibo_list.append(sum) #List used instead of printing every iteration for modularity
    return fibo_list

print(fibo(100)) #Print list 

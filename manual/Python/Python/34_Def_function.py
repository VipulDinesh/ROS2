def my_func(num): 

    return num*2 

 

seq=[2,3,4,5,6,7] 

map(my_func,seq) # predifined function

a= list(map(my_func,seq)) 

print(a) 
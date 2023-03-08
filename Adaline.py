import numpy as np
import Alphabet36bit as ap

x_vec = ap.x
y_vec = ap.y

def grad_descent(weight_curr, x_vec, y_vec, alpha): 
    weight_grad = [0 for x in range(36)]
    size = len(x_vec[0])
    
    for i in range(len(x_vec)):
        x = x_vec[i]
        y = y_vec[i]
        
        for n in range(size):
            temp = weight_grad[n]
            weight_grad[n] =  temp + -(2/size) * x[n] * (y - get_Vec(weight_curr, x))
            
    newWeight = []
    
    for n in range(len(weight_grad)):
        weight_grad[n] = weight_curr[n] - weight_grad[n] * alpha
        newWeight.append(weight_grad[n])
    
    return newWeight

def get_Vec(weight, x):
    return np.dot(weight, x)

        
def print_Weight(weight):
    x = len(weight)
    
    for i in range(x):
        if i == x-1:
            print(f"Wb: {weight[i]}")
        else:
            print(f"W{i}: {weight[i]}")
    
def alphabet_Print(feed):
    for i in range(len(feed)-1):
        
        print(feed[i] , end= " ")
        
        if (i+1) % 5 == 0:
            print()
            
weight = [0 for x in range(36)]
alpha = 0.05
epochs = 2500

for i in range(epochs): 
    if i % 100:
        print_Weight(weight)
        
        
    weight = grad_descent(weight, x_vec, y_vec, alpha)
   
    
print("Final values:")
print_Weight(weight)

while(True):
    test = input("\nEnter letter: ")
    if test == "0":
        break
    feed = x_vec[ord(test) - ord("A")]
    if(np.dot(weight, feed) > 0.55):
        alphabet_Print(feed)
        print(f"{test} is a vowel letter!\n")
    else:
        alphabet_Print(feed)
        print(f"{test} is a consonant letter!\n")
    
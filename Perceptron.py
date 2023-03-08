import numpy as np
import Alphabet36bit as ap

def get_Vec(weight, xvec):
    vec = 0
    
    for i in range(len(xvec)): 
        vec += xvec[i] * weight[i]
        
        
    vec += weight[-1]
    
    return vec

def train(weight, x_vec, y_vec, alpha):
    
    for x in range(len(x_vec)):
        current_X = x_vec[x]
        
        v = get_Vec(weight, current_X)
        yc = activation_Func(v)
        delta = y_vec[x] - yc
        
        for y in range(len(current_X)):
            weight[y] = weight[y] + alpha * delta * current_X[y]
        
        
        weight[-1] = weight[-1] + alpha * delta
        
    return weight

def activation_Func(vec):
    return 1 if vec > 0 else 0

        
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
            
epochs = 2500
x_vec = ap.x
y_vec = ap.y
weight = [0.5 for x in range(36)]

for _ in range(epochs):
    
    if _ % 50 == 0:
        print_Weight(weight)
        
    weight = train(weight, x_vec, y_vec, alpha = 0.12)

while(True):
    test = input("Enter letter: ")
    
    if test == "0":
        break
    
    feed = x_vec[ord(test) - ord("A")]
    vec = get_Vec(weight, feed)
    
    if(activation_Func(vec)):
        
        alphabet_Print(feed)
        
        print(f"{test} is a vowel letter!\n")
    else:
        
        alphabet_Print(feed)
        print(f"{test} is a consonant letter!\n")
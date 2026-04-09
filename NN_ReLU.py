#A artificial neuron can store and process information
#The store value comes from the weights and features
#THe below code shows how the neuron must be calculating its z value and then applying the ReLU function
import numpy as np
import matplotlib.pyplot as plt



###################################################################################
#Defining features
###################################################################################

X=np.array([2.0,3.0,4.0])


###################################################################################
#Defining weights
###################################################################################

W=np.array([0.5,0.3,0.2])


bias=1.0

def relu(Z):
    a=max(0,Z)
    return a

###################################################################################
#Neuron forward pass- caluclating z and passing the value to the activation function
###################################################################################


def neuronWithReLu(X,W):
    list=[]
    counter=0
    for i in X:
        n=i*W[counter]
        counter=counter+1
        list.append(n)
    print("List: ",list)
    z=0
    for i in list:
        z=z+i
    z=z+bias
    activation=relu(z)

    return z,activation

z,actf=neuronWithReLu(X,W)

print("Features: ",X)
print("Weights: ",W)

print("Weighted sum calculations:",z)
print(f"Activation function ReLu applied on {z} :", actf)




###################################################################################
#Lets plot ReLu 
###################################################################################



def plot_relu():
    #Generate range of values for z
    z_values=np.linspace(-10,10,200)

    #Apply relu on all values
    relu_values=np.maximum(0,z_values)

    #Plotgraph
    plt.figure(figsize=(8,5))
    plt.plot(z_values,relu_values,label="ReLu Function",linewidth=2,color="green")

    #Axes lines
    plt.axhline(y=0,color="black",linewidth=0.5)
    plt.axvline(x=0,color="gray",linestyle="--")

    #Labels and title

    plt.title("ReLu activation function",fontsize=16)
    plt.xlabel("Input (z)",fontsize=14)
    plt.ylabel("Output",fontsize=14)

    #Grid and legend 

    plt.grid(True,linestyle="--",alpha=0.6)
    plt.legend()

    #Show graph
    plt.show()


print("Here is coming the ReLU graph for evenly spaced 200 values between -10 and 10")

plot_relu()
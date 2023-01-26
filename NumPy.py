import numpy as np
#Generate a random vector of size 20 with float numbers between 1 and 20
vector = np.random.uniform(1, 20, 20)
print("\nRandom Vector \n",vector)

#Reshape the array to 4 by 5
reshaped_vector = vector.reshape(4, 5)
print("\nReshaped Array")
print(reshaped_vector)

#Find the index of the maximum value in each row
max_values = np.argmax(reshaped_vector, axis=1)

#Replace the maximum value in each row with 0
reshaped_vector[np.arange(reshaped_vector.shape[0]), max_values] = 0
print("\nReplacing the maximum value with 0 ")
print(reshaped_vector)                                                       
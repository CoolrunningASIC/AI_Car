import random
import math

class Layer:
    def __init__(self, inputs_count, outputs_count):
        # initialize list of outputs
        self.outputs = [0.0 for _ in range(outputs_count)]
        # create list of random numbers for qty of inputs x outputs (5x4=20)
        # I don't understand the use of _i and _o instead of just i and o
        self.weights = [[random.random() * 2 - 1 for _i in range(inputs_count)] for _o in range(outputs_count)]

    def feed_forward(self, inputs):
        # calculate outputs based on inputs and weights
        for output_index, output in enumerate(self.outputs): # for each output
            sum = 0
            for weight_index, input in enumerate(inputs):
                sum += input * self.weights[output_index][weight_index] # multiply input by the weight
            # Activation function - without this, you just have linear calculations
            # addint the tanh function makes the model more powerful
            self.outputs[output_index] = math.tanh(sum)

class Network:
    def __init__(self, dimensions): # dimensions describe qty and count of each layer (5, 4, 2)
        self.dimensions = dimensions
        self.layers = []
        # runs the loop one less time than the number of dimensions
        for i in range(len(dimensions) - 1):
            # because this function is processing two at a time
            # in 5,4,2 example, first processes from 5 to 4, then from 4 to 2
            self.layers.append(Layer(dimensions[i], dimensions[i + 1]))

    def feed_forward(self, inputs): 
        for layer in self.layers:
            layer.feed_forward(inputs) # confusing that both functions are called feed_forward
            inputs = [i for i in layer.outputs]
        return self.layers[-1].outputs # [-1] returns the last item for steer and accelerate
    
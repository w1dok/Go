from __future__ import print_function
import numpy as np

def sigmoid_double(x):
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid(z):
    return np.vectorize(sigmoid_double)(z)

def sigmoid_prime_double(x):
    return np.vectorize(sigmoid_prime_double)(z)

class Layer:
    def __init__(self):
        self.params = []
        
        self.previous = None
        self.next = None
        
        self.input_data = None
        self.output_data = None
        
        self.input_delta = None
        self.output_delta = None
        
        
    def connect(self, layer):
        self.previous = layer
        layer.next = self
        
    def forward(self):
        raise NotImplementedError
    
    def get_forward_input(self):
        if self.previous is not None:
            return self.previous.output_data
        else:
            return self.input_data
        
    def backward(self):
        raise
    
    def get_backward_input(self):
        if self.next is not None:
            return self.next.output_delta
        else:
            return self.input_delta
        
    def clear_deltas(self):
        pass
    
    def update_params(self):
        pass
    
    def describe(self):
        raise NotImplementedError
    
class ActivationLayer(Layer):
    def __init__(self, input_dim):
        super(ActivationLayer, self).__init__()
        
        self.input_dim = input_dim
        self.output_dim = input_dim
        
    def forward(self):
        data = self.get_forward_input()
        self.output_data = sigmoid(data)
        
    def backward(self):
        delta = self.get_backward_input()
        data = self.get_forward_input()
        self.output_data = sigmoid(data)
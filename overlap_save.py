#!python3

import numpy as np

class overlap_save:
    """ Class containing the overlap-save algorithm for long 1D convolution betweem x and h signals """
    
    def __init__(self):
        """ Constructor method """
        self.x = []
        self.h = []
        
        self.block_size = 0                 # Commonly appears as N in the literature
        self.overlap = 0
        
    def set_signals(self, x, h):
        """ """
        
        # Checks for invalid signals
        if len(x) < len(h):
            print("Please enter the long signal as x")
            exit(-1)
        if len(x) == 0 or len(y) == 0:
            print("Please enter valid signals")
            exit(-1)
        
        self.x = x
        self.h = h
        self.overlap = len(h) - 1
        
        
    def reset(self):
        self.x = []
        self.h = []
        
        
    def set_block_size(self, block_size):
        """ Define the block  """
        
        if len(x) == 0 or len(y) == 0:
            print("Please set signals before block size")
            exit(-1)
        
        if block_size <= 0:
            print("Please enter a valid block size")
            exit(-1)
        
        if block_size <= len(h) - 1:
            print("Block size should be greater than length of h - 1")
            exit(-1)
        
        self.block_size = block_size
        
        
    def circular_convolution(self):
        """ Computes circular convolution theoresm using the fft """
        
        x_padded = x
        h_padded = h
        # Define flattening lambda (Alex Martelli)
        flatten = lambda l: [item for sublist in l for item in sublist]
        
        ## Padding
        # Append zeroes in the beginning of x to make x_padded divisible by block_len 
        x_padded.insert(0,[0]*(len(x) % self.block_len))
        # Append zeroes in the begining of h to equal h_padded and block_len sizes
        h_padded.insert(0,[0]*(len(self.block_len)-len(h)))
        print(x_padded)
        print(h_padded)
        
        ## Flatten padding results
        flatten(h_padded)
        flatten(x_padded)
        #h_padded = flatten(h_padded)       # ?
        #x_padded = flatten(x_padded)  
        print(x_padded)
        print(h_padded)
        
        ## By circular convolution theorem, >>><<<
        x_convolved = np.real(np.fft.ifft( np.fft.fft(x_padded) * np.fft.fft(h_padded) ))
        
        return x_convolved
        
        
    def apply_convolution(self):
        """ """
        
        if self.block_size == 0:
            print("Please set block size before applying convolution")
        
        #loop over X, len(h)-1 steps each time, with each subX being the past block_size positions
        
        for 
        
        return
    
    
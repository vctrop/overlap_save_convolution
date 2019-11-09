#!python3

import numpy as np

class overlap_save:
    """ Class containing the overlap-save algorithm for long 1D convolution betweem x and h signals """
    
    def __init__(self):
        """ Constructor method """
        self.x = np.array([])
        self.h = np.array([])
        
        self.block_size = 0
        
        
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
        self.y = y
        
        
    def set_block_size(self, block_size):
        """ """
        
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
        """ """
        return 
        
        
    def apply_convolution(self):
    
    
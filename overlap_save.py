#!python3
# Victor O. Costa (nov, 2019)

import numpy as np

class overlap_save:
    """ Class containing the overlap-save algorithm for long 1D convolution betweem x and h signals """
    
    def __init__(self):
        """ Constructor method """
        self.x = []
        self.h = []
        
        self.block_size = 0                 # Commonly appears as N in the literature
        self.overlap = 0
     
    def reset(self):
        self.x = []
        self.h = []
        self.block_size = 0
     
    def set_signals(self, x, h):
        """ Define long signal x and the corresponding filter impulse response h """
        
        # Checks for invalid signals
        if len(x) < len(h):
            print("Please enter the long signal as x")
            exit(-1)
        if len(x) == 0 or len(h) == 0:
            print("Please enter valid signals")
            exit(-1)
        
        self.x = x
        self.h = h
        self.overlap = len(h) - 1
        
        
    def set_block_size(self, block_size):
        """ Define the size of each data block """
        
        if len(self.x) == 0 or len(self.h) == 0:
            print("Please set signals before block size")
            exit(-1)
        
        if block_size <= 0:
            print("Please enter a valid block size")
            exit(-1)
        
        if block_size <= len(self.h) - 1:
            print("Block size should be greater than length of h - 1")
            exit(-1)
        
        self.block_size = block_size
        
        
    # Irregular list flattening (Josh Lee, https://stackoverflow.com/a/2158522/6129362
    # def _flatten_list(self, x):
        # """ Flattens a list composed of lists and elements """
        # if isinstance(x, collections.Iterable):
            # return [a for i in x for a in self._flatten_list(i)]
        # else:
            # return [x]
        
        
    ## The periodic properties of DFT result in the circular convolution theorem for finite-support sequences,
    #  which says that calculating the inverse DFT of the product of DFTs is equivalent to computing the linear convolution with one of the sequences periodically extended,
    #  that is, the circular convolution of the sequences
    def circular_convolution(self, x_block, h):
        """ Computes circular convolution theorem using the fft """
        ## Padding
        # Appends zeroes in the begining of h to equal h_padded and block_len sizes
        h_padded = list(h)
        h_padded.extend([0] * (len(x_block)-len(h)))
        
        # From circular convolution theorem
        x_convolved = np.real(np.fft.ifft(np.fft.fft(x_block) * np.fft.fft(h_padded)))
        return x_convolved
        
        
    def overlap_save_convolution(self):
        """ Apply the filter defined by impulse response h over the long signal x using the overlap-save method """
        
        if self.block_size == 0:
            print("Please set block size before applying convolution")
        
        # In the beginning there is no past block to overlap from, so the first M-1 positions are set to zero
        x_padded = list(self.x)
        x_padded = [0]*(len(self.h) - 1) + x_padded
        
        # Defines convolution result
        y = []
        
        # loop over x len(h) steps at time, creating a overlap of M-1 positions
        for i in range(0, len(x_padded), len(self.h)):
            ## Define x block
            # Covers the border case of the last block not being N-sized by appending N - (Len(x_padded) - i) zeroes to it
            if len(x_padded) - i < self.block_size:
                x_block = x_padded[i : len(x_padded)]
                x_block.extend([0] * (self.block_size - (len(x_padded) - i)))
                
            # For all other blocks, simply copy x_padded from i to i+N-1
            else:
                x_block = x_padded[i : i + self.block_size]
            
            # The partial result for a given block is the circular convolution between the signal block and filter impulse response 
            y_local = self.circular_convolution(x_block, self.h)
            print("X_block, y_local")
            print(x_block)
            print(y_local)
            
            # Keeps only values unnafected by the filter delay of circular convolution, achieving similar result as the linear convolution
            y.extend(y_local[len(self.h) - 1:])
        
        return y
        
        
# Overlap-save convolution function wrapper to overlap_save class
def os_convolve(x, h, block_size):
    os = overlap_save()
    os.set_signals(x, h)
    os.set_block_size(block_size)
    return os.overlap_save_convolution()
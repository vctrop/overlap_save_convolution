#!python3
# Test script for the overlap_save class

# Define sequence x and filter impulse response h
x = [3,-1,0,1,3,2,0,1,2,1]
h = [1,1,1]

## Overlap-save
# One possibility: instantiate overlap_save class
from overlap_save import overlap_save

# Declare the OS 
os = overlap_save()

# Set overlap-save signal and filter to be applied
os.set_signals(x, h)

# Define overlap-save block size
os.set_block_size(5)

# Compute convolution
conv = os.overlap_save_convolution()
print(conv)

# Other possibility: only call os_convolution method
from overlap_save import os_convolve
conv = os_convolve(x, h, 5);
print(conv)
import ctypes

# Load the shared library
lib = ctypes.CDLL('./libexample.so')  # or 'example.dll' on Windows

# Call the function
lib.my_function()

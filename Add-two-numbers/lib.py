
import ctypes

# Load the shared library
lib = ctypes.CDLL('./libexample.so')  # or 'example.dll' on Windows

# Specify the argument and return types
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int

# Call the function
result = lib.add(5, 7)
print("Result:", result)

// example.cpp
#include <iostream>

extern "C" {
    void my_function() {
        std::cout << "Hello from C++" << std::endl;
    }
}

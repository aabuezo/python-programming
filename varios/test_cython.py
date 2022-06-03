import cython_example
import time


start_vanilla = time.time()
print(cython_example.prime_finder_vanilla(10000))
end_vanilla = time.time()
print(end_vanilla-start_vanilla)


start_c = time.time()
print(cython_example.prime_finder_optimized(10000))
end_c = time.time()
print(end_c-start_c)

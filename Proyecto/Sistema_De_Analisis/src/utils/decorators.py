import time
import logging

logging.basicConfig(level=logging.INFO)

def timeit(func):
    """Decorator to measure the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

def logit(func):
    """Decorator to log the function calls."""
    def wrapper(*args, **kwargs):
        logging.info(f"Executing function '{func.__name__}'")
        result = func(*args, **kwargs)
        logging.info(f"Finished executing function '{func.__name__}'")
        return result
    return wrapper

class Fibonacci:
    def __init__(self):
        
        self.prev = 0
        self.curr = 2  

    def generate_even_fibonacci(self):
        """
        Generator to yield the next even Fibonacci number.
        We start with the first even Fibonacci number, 2.
        """
        while True:
            yield self.curr
            
            self.prev, self.curr = self.curr, 4 * self.curr + self.prev

    def sum_of_even_fibonacci(self, count):
        """
        Calculate the sum of the first 'count' even Fibonacci numbers.
        :param count: The number of even Fibonacci numbers to sum.
        :return: The sum of the first 'count' even Fibonacci numbers.
        """
        total_sum = 0
        even_fib_gen = self.generate_even_fibonacci()
        for _ in range(count):
            total_sum += next(even_fib_gen)
        return total_sum


# Main driver function
if __name__ == "__main__":
    fib = Fibonacci()
    result = fib.sum_of_even_fibonacci(100)  # Sum the first 100 even Fibonacci numbers
    print(f"The sum of the first 100 even Fibonacci numbers is: {result}")

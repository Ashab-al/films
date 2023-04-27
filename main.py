# numbers = [0, 1, 2, 3, 4]

# # for number in numbers:
# #     print(number)

# # def for_loop(iterable, loop_body_function):
# #     iterator = iter(iterable)
# #     next_element_exist = True
# #     while next_element_exist:
# #         try:
# #             element_from_iterator = next(iterator)
# #         except StopIteration:
# #             next_element_exist = False
# #         else:
# #             loop_body_function(element_from_iterator)

# # for_loop(numbers, print)

# iterator = iter(numbers)
# print(dir(iterator))

class IterBoy:
    def __init__(self, count_iters):
        self.count_iters = count_iters
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.count_iters:
            self.counter += 1
            return f"{self.counter} итеррационный boy из {self.count_iters}"
        raise StopIteration
    
new_obj = IterBoy(4)

print(next(new_obj))
print(next(new_obj))

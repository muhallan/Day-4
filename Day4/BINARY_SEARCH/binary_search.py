""" a class that inherits from the list class the init method which creates a list of integers given the length and the step"""
class BinarySearch(list):

    def __init__(self, length, step):
        super(BinarySearch, self).__init__()

        for index in range(1, length + 1):
            self.append(index * step)
        self.length = len(self)

    def search(self, value_to_find):
        """a search method using the binary search algorithm to find a value passed in"""
        first_index = 0
        last_index = len(self) - 1
        value_to_find_index = 0
        is_found = False
        # initialize counter to 0
        counter = 0
        # check if value_to_find is the first or last element. if True, don't carry out the binary search
        if value_to_find == self[first_index]:
            value_to_find_index = first_index
            is_found = True
        elif value_to_find == self[last_index]:
            value_to_find_index = last_index
            is_found = True

        # check if value_to_find is not present in the list. if True, no need to search
        if value_to_find not in self:
            is_found = True
            value_to_find_index = -1

        # carry out the binary search algorithm using a while loop if value is not yet found
        while first_index <= last_index and not is_found:
            counter += 1  # increase counter when an iteration occurs
            middle_point = (first_index + last_index) // 2
            if self[middle_point] == value_to_find:
                is_found = True
                value_to_find_index = middle_point
            else:
                if value_to_find < self[middle_point]:
                    last_index = middle_point - 1
                else:
                    first_index = middle_point + 1
        return {'count': counter, 'index': value_to_find_index}
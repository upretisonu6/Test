class SortedArrayIntersection:
    def __init__(self, array1, array2):
        # Initialize with two sorted arrays
        self.array1 = array1
        self.array2 = array2

    def find_common_elements(self):
        """
        Find the common elements in two sorted arrays without duplicates.
        :return: A sorted list containing the common elements.
        """
        common_elements = []
        i, j = 0, 0  # Pointers for both arrays

        # Traverse both arrays using two pointers
        while i < len(self.array1) and j < len(self.array2):
            if self.array1[i] < self.array2[j]:
                i += 1
            elif self.array1[i] > self.array2[j]:
                j += 1
            else:
                # If elements are the same, add to result (avoid duplicates)
                if not common_elements or common_elements[-1] != self.array1[i]:
                    common_elements.append(self.array1[i])
                i += 1
                j += 1
        
        return common_elements


# Main driver function
if __name__ == "__main__":
    # Test the function
    array1 = [1, 2, 4, 6, 8, 10]
    array2 = [2, 4, 6, 8, 12]

    intersection = SortedArrayIntersection(array1, array2)
    result = intersection.find_common_elements()
    print(f"The common elements are: {result}")

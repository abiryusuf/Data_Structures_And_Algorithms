class Set:
    # Creates an empty set instance
    def __init__(self):
        self.theElement = list()

    # Return the number of items in the set
    def __len__(self):
        return len(self.theElement)

    # Determines if an element is in the set
    def __contains__(self, item):
        return item in self.theElement

    # Add new unique elements to the set
    def add(self, element):
        if element not in self:
            self.theElement.append(element)

    def remove(self, element):
        assert element in self, "The element must be in set"
        self.theElement.remove(element)

    # Determines if two sets are equal
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    # Determines if this set is a subset of setB
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
            return True


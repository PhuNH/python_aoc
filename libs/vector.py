class Vector:
    def __init__(self, *elements):
        self._data = elements
        self.x = elements[0]
        self.y = elements[1]

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._data == other._data

    def __hash__(self):
        return hash(self._data)

import copy


class Vector:
    def __init__(self, *elements):
        self._data = elements
        self.x = elements[0]
        self.y = elements[1]

    @property
    def up(self):
        return Vector(self.x, self.y-1)

    @property
    def down(self):
        return Vector(self.x, self.y+1)

    @property
    def left(self):
        return Vector(self.x-1, self.y)

    @property
    def right(self):
        return Vector(self.x+1, self.y)

    @property
    def adjacents(self):
        return {self.up, self.down, self.left, self.right}

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._data == other._data

    def __hash__(self):
        return hash(self._data)

    def __str__(self):
        return self._data.__str__()


class Area:
    def __init__(self, data: [[]]):
        self._data = data
        self.width = len(data[0])
        self.height = len(data)

    def __getitem__(self, item):
        return self._data.__getitem__(item)

    def adjacents(self, point: Vector) -> set[Vector]:
        result = copy.deepcopy(point.adjacents)
        if point.x == 0:
            result.remove(point.left)
        elif point.x == self.width-1:
            result.remove(point.right)
        if point.y == 0:
            result.remove(point.up)
        elif point.y == self.height-1:
            result.remove(point.down)
        return result

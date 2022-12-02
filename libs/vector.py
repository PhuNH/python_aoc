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

    @property
    def up_right(self):
        return Vector(self.x+1, self.y-1)

    @property
    def down_right(self):
        return Vector(self.x+1, self.y+1)

    @property
    def down_left(self):
        return Vector(self.x-1, self.y+1)

    @property
    def up_left(self):
        return Vector(self.x-1, self.y-1)

    @property
    def diag_adjacents(self):
        return {self.up, self.down, self.left, self.right, self.up_right, self.down_right, self.down_left, self.up_left}

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
        self._adjacents = {}
        self._diag_adjacents = {}

    def __getitem__(self, item):
        return self._data.__getitem__(item)

    def at(self, coord: Vector):
        return self._data[coord.y][coord.x]

    def set_at(self, coord: Vector, value):
        self._data[coord.y][coord.x] = value

    def adjacents(self, point: Vector) -> set[Vector]:
        if point not in self._adjacents:
            result = point.adjacents
            if point.x == 0:
                result.remove(point.left)
            elif point.x == self.width-1:
                result.remove(point.right)
            if point.y == 0:
                result.remove(point.up)
            elif point.y == self.height-1:
                result.remove(point.down)
            self._adjacents[point] = result
        return self._adjacents[point]

    def diag_adjacents(self, point: Vector) -> set[Vector]:
        if point not in self._diag_adjacents:
            result = point.diag_adjacents
            result = set(filter(lambda p: p.x in range(self.width) and p.y in range(self.height), result))
            self._diag_adjacents[point] = result
        return self._diag_adjacents[point]

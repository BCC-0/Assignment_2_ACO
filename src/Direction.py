import enum


# Enum representing the directions an ant can take.
class Direction(enum.Enum):
    east = 0
    north = 1
    west = 2
    south = 3

    """
    Convert direction to an integer representation.
    @param dir: the direction of interest
    @return the corresponding integer from 0 to 3
    """
    @classmethod
    def dir_to_int(cls, dir):
        return dir.value


    @staticmethod
    def from_coords(start, end):
        dx = end.x - start.x
        dy = end.y - start.y
        if dx == 1 and dy == 0:
            return Direction.east
        elif dx == -1 and dy == 0:
            return Direction.west
        elif dx == 0 and dy == 1:
            return Direction.south
        elif dx == 0 and dy == -1:
            return Direction.north
        else:
            raise ValueError(f"Invalid direction coordinates: start={start}, end={end}")

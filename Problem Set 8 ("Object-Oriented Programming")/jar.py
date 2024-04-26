class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size = self.size + n
        return self.size

    def withdraw(self, n):
        self.size = self.size - n
        return self.size

    # Getter
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    # Setters
    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity should be a positive integer")
        self._capacity = capacity

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("There's not enough space in the jar")
        elif size < 0:
            raise ValueError("There aren't so many cookies in the jar")
        self._size = size

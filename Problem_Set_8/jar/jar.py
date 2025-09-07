class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return f"{self._size * '🍪'}"

    def deposit(self, n):
        if n > self._capacity:
           raise ValueError("Not enough space")
        if self._size +n > self._capacity:
            raise ValueError("You're exceeding Limit")
        self._size += n


    def withdraw(self, n):
        if n > self._size:
            raise ValueError("not enough to withdraw")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self,capacity):
        if capacity < 0:
            raise ValueError("Non-neagtive not possible")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

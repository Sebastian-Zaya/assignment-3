import math


class DeletedEntry:
    # Marker to indicate that a slot in the hash table has been deleted.
    pass


class QuadHash:
    # Hash table implementation using 
    # quadratic probing for collision resolution.

    def __init__(self, initial_capacity: int = 11) -> None:
        self.capacity = initial_capacity
        self.size = 0
        self.table = [None] * self.capacity
        self.DELETED = DeletedEntry()
        self.load_factor_limit = 0.5

    def __len__(self) -> int:
        return self.size

    def _hash(self, key: object) -> int:
        return abs(hash(key)) % self.capacity

    def _is_prime(self, num: int) -> bool:
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def _next_prime(self, start: int) -> int:
        candidate = start
        while not self._is_prime(candidate):
            candidate += 1
        return candidate

    def _resize(self) -> None:
        new_capacity = self._next_prime(self.capacity * 2)
        old_table = self.table
        self.capacity = new_capacity
        self.table = [None] * self.capacity
        self.size = 0

        for entry in old_table:
            if entry and entry is not self.DELETED:
                key, value = entry
                self.add(key, value)

    def _probe(self, start_index: int, step: int) -> int:
        return (start_index + step * step) % self.capacity

    def add(self, key: object, value: object) -> None:
        if (self.size + 1) / self.capacity > self.load_factor_limit:
            self._resize()

        index = self._hash(key)
        step = 0
        first_deleted_index = -1

        while step < self.capacity:
            probe_index = self._probe(index, step)
            entry = self.table[probe_index]

            if entry is None:
                if first_deleted_index != -1:
                    probe_index = first_deleted_index
                self.table[probe_index] = (key, value)
                self.size += 1
                return

            elif entry is self.DELETED:
                if first_deleted_index == -1:
                    first_deleted_index = probe_index

            else:
                existing_key, existing_val = entry
                if existing_key == key:
                    self.table[probe_index] = (key, value)
                    return
            step += 1

        raise Exception("Hash table is full, cannot add new key.")

    def get(self, key: object) -> object:
        index = self._hash(key)
        step = 0

        while step < self.capacity:
            probe_index = self._probe(index, step)
            entry = self.table[probe_index]

            if entry is None:
                return None
            elif entry is not self.DELETED:
                existing_key, existing_val = entry
                if existing_key == key:
                    return existing_val
            step += 1

        return None

    def contains_key(self, key: object) -> bool:
        return self.get(key) is not None

    def remove(self, key: object) -> bool:
        index = self._hash(key)
        step = 0

        while step < self.capacity:
            probe_index = self._probe(index, step)
            entry = self.table[probe_index]

            if entry is None:
                return False
            elif entry is not self.DELETED:
                existing_key, existing_val = entry
                if existing_key == key:
                    self.table[probe_index] = self.DELETED
                    self.size -= 1
                    return True
            step += 1

        return False

    def __str__(self) -> str:
        lines = []
        for i, entry in enumerate(self.table):
            if entry is None:
                lines.append(f"{i}: None")
            elif entry is self.DELETED:
                lines.append(f"{i}: DEL")
            else:
                key, value = entry
                lines.append(f"{i}: ({key}, {value})")
        return "\n".join(lines)
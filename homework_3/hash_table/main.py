class HashTable:
    def __init__(self, capacity=8):
        if capacity < 1:
            raise ValueError("capacity must be positive")

        self.capacity = capacity
        self.min_capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def _bucket_index(self, key):
        return hash(key) % self.capacity

    def _find_pair(self, key):
        bucket = self.buckets[self._bucket_index(key)]

        for pair in bucket:
            if pair[0] == key:
                return pair

        return None

    def put(self, key, value):
        pair = self._find_pair(key)

        if pair is not None:
            pair[1] = value
            return

        bucket = self.buckets[self._bucket_index(key)]
        bucket.append([key, value])
        self.size += 1

        if self.size / self.capacity > 0.75:
            self._resize(self.capacity * 2)

    def get(self, key):
        pair = self._find_pair(key)

        if pair is None:
            raise KeyError(key)

        return pair[1]

    def remove(self, key):
        bucket = self.buckets[self._bucket_index(key)]

        for index, pair in enumerate(bucket):
            if pair[0] == key:
                value = pair[1]
                bucket.pop(index)
                self.size -= 1

                if self.capacity > self.min_capacity and self.size / self.capacity < 0.25:
                    self._resize(max(self.min_capacity, self.capacity // 2))

                return value

        raise KeyError(key)

    def _resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [[] for _ in range(new_capacity)]

        for bucket in old_buckets:
            for pair in bucket:
                new_index = self._bucket_index(pair[0])
                self.buckets[new_index].append(pair)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self._find_pair(key) is not None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.remove(key)

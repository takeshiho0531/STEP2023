def calculate_hash(key):
    assert type(key) == str
    hash = 0
    for i in key:
        hash += ord(i)
    return hash


class Item:
    def __init__(self, key, value, next) -> None:
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self):
        self.bucket_size = 97
        self.buckets = [None] * self.bucket_size
        self.item_count = 0

    def put(self, key, value):
        assert type(key) == str
        self.check_size()
        bucket_index = calculate_hash(key) % self.bucket_size
        item = self.buckets[bucket_index]
        while item:
            if item.key == key:
                item.value = value  # keyが同じものあったときvalueを更新
                return False
            item = item.next
        new_item = Item(key, value, self.buckets[bucket_index])
        self.buckets[bucket_index] = new_item
        self.item_count += 1
        return True

    def get(self, key):
        assert type(key) == str
        self.check_size()
        bucket_index = calculate_hash(key) % self.bucket_size
        item = self.buckets[bucket_index]
        while item:
            if item.key == key:
                return (item.value, True)
            item = item.next
        return (None, False)

    def delete(self, key):
        assert (type) == str
        self.check_size()
        bucket_index = calculate_hash(key) % self.bucket_size
        item = self.buckets[bucket_index]

        prev = None
        while item:
            if item.key == key:
                if prev:
                    prev.next = item.next
                else:
                    self.buckets[bucket_index] = item.next
                self.item_count -= 1
                return True
            else:
                item = item.next
                prev = item
        return False

    def rehash(self, expand):
        if expand:
            new_bucket_size = self.next_prime(self.bucket_size * 2)
        else:
            new_bucket_size = self.next_prime(self.bucket_size // 2)
        new_buckets = [None] * new_bucket_size

        for bucket in self.buckets:
            item = bucket
            while item:
                next_item = item.next
                new_bucket_index = calculate_hash(item.key) % new_bucket_size
                # item.next = new_buckets[new_bucket_index] これ何
                new_buckets[new_bucket_index] = item
                item = next_item

        self.buckets = new_buckets
        self.bucket_size = new_bucket_size

class LinkedList:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self._len = 1 if value is not None else 0

    def __getitem__(self, item):
        if 0 <= item < self._len:
            t = self
            for _ in range(item):
                t = t.next
            return t.value
        raise IndexError('LinkedList index out of range')

    def __setitem__(self, key, value):
        if type(key) != int:
            raise TypeError(f'LinkedList indices must be integers, not {type(key)}')
        if 0 <= key < self._len:
            t = self
            for _ in range(key):
                t = t.next
            t.value = value
        else:
            raise IndexError('LinkedList assignment index out of range')

    def __delitem__(self, key):
        if type(key) != int:
            raise TypeError(f'LinkedList indices must be integers, not {type(key)}')
        if 0 <= key < self._len:
            t = self
            for _ in range(key):
                t = t.next
            if t.next is not None:
                t.value = t.next.value
                t.next = t.next.next
            else:
                t.value = None
            self._len -= 1
        else:
            raise IndexError('LinkedList assignment index out of range')

    def __str__(self):
        if self.value is None:
            return '<>'
        t = self
        res = '<'
        while t:
            if type(t.value) == str:
                this = t.value.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n').replace('\t', '\\t')
                part = f"'{this}', "
            else:
                if t.value is self:
                    part = '<...>, '
                else:
                    part = f'{t.value}, '
            res += part
            t = t.next
        res = res[:-2] + '>'
        return res

    def __bool__(self):
        return self.value is not None

    def __len__(self):
        return self._len

    def __eq__(self, other):
        if self is other:
            return True
        if type(other) != LinkedList:
            return False
        if len(self) == len(other):
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True
        return False

    def append(self, obj):
        if obj is not None:
            self._len += 1
        if self.value is None:
            self.value = obj
            return
        t = self
        while t.next:
            t = t.next
        t.next = LinkedList(obj)

    def pop(self):
        if self.value is None:
            raise IndexError('pop from empty LinkedList')
        self._len -= 1
        t = self
        while t.next:
            t = t.next
        res = t.value
        t.value = None
        return res

    def extend(self, iterable):
        iter(iterable)
        if iterable is self:
            iterable = iterable.copy()
        for obj in iterable:
            self.append(obj)

    def clear(self):
        self.value = None
        self.next = None

    def insert(self, index, obj):
        if type(index) != int:
            raise TypeError(f"'{type(index)}' object cannot be interpreted as an integer")
        if index < 0:
            raise ValueError('index can not be negative')
        t = self
        for _ in range(min(index, len(self))):
            t = t.next
        next = t.next
        value = t.value
        t.value = obj
        t.next = LinkedList(value)
        t.next.next = next
        self._len += 1

    def count(self, obj):
        counter = 0
        for x in self:
            if x == obj:
                counter += 1
        return counter

    def copy(self):
        copy_ll = LinkedList()
        for x in self:
            copy_ll.append(x)
        return copy_ll

    def reverse(self):
        for i in range(self._len // 2):
            self[i], self[self._len - i - 1] = self[self._len - i - 1], self[i]


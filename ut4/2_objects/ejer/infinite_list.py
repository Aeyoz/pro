class InfiniteList:
    def __init__(self, *items, fill_value=None):
        self.list = list(items)
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        return self.list[index] if 0 <= index <= len(self.list) - 1 else "IndexError"

    def __setitem__(self, index: int, item):
        for _ in range(len(self.list), index + 1):
            self.list.append(self.fill_value)
        self.list[index] = item

    def __len__(self) -> int:
        return len(self.list)

    def __str__(self) -> str:
        output = ", ".join(str(item) for item in self.list)
        return output


dende = InfiniteList(fill_value="pana")

dende[2] = "hola"
print(len(dende))
print(dende)
print(dende[21])
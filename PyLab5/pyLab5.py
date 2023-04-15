import time

class TribonacciIterableWithGenerator:
    def __init__(self, length):
        self.sequence = [0, 0, 1]
        self.length = length

    def __iter__(self):
        x = 0

        while x <= self.length:
            trib = 0
            if x <= 2:
                trib = 1 if x == 2 else 0
            else:
                trib = self.sequence[2] + self.sequence[1] + self.sequence[0]
                self.sequence[0] = self.sequence[1]
                self.sequence[1] = self.sequence[2]
                self.sequence[2] = trib
            x += 1
            yield str(x) + ": " + str(trib)


if __name__ == '__main__':
    main_iter = TribonacciIterableWithGenerator(34)

    for line in main_iter:
        print(line)
        time.sleep(0.25)

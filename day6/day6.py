# Advent of Code 2022 Day 6

# returns the number of characters that need to be processed before the marker is detected
def chars_processed(datastream):
    def all_unique(chars):
        charset = set()
        for c in chars:
            if c in charset:
                return False
            charset.add(c)
        return True

    chars = list(datastream[:3])
    for i in range(3, len(datastream)):
        chars.append(datastream[i])
        if all_unique(chars):
            return i + 1
        del(chars[0])

def main():
    file = open("input.txt")
    datastream = file.readline().strip()
    file.close()
    print(chars_processed(datastream))

if __name__ == "__main__":
    main()
from functools import reduce

def part_one(start, mapping):
    for m in mapping.split('\n')[1:]:
        destination, source, len = map(int, m.split())
        delta = start - source

        if delta in range(len):
            return destination + delta
        
    else: return start

def part_two(inputs, mapping):
    for start, length in inputs:
        while length > 0:
            for m in mapping.split('\n')[1:]:
                destination, source, len = map(int, m.split())
                delta = start - source

                if delta in range(len):
                    len = min(len - delta, length)
                    yield (destination + delta, len)

                    start += len
                    length -= len
                    break

            else: 
                yield (start, length)
                break

if __name__ == "__main__":
    seeds = open('input.txt').read().split('\n\n')
    
    mappings = seeds[1:]
    seeds = list(map(int, seeds[0].split()[1:]))

    print(min(reduce(part_one, mappings, int(s)) for s in seeds))
    print([min(reduce(part_two, mappings, s))[0] for s in [zip(seeds, [1] * len(seeds)), zip(seeds[0::2], seeds[1::2])]][1])

import sys
import re


def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

lines = [line.rstrip() for line in get_lines_from_file()]

def apply_mask(mask, value):
    #print(mask, value)
    bits = list(format(value, '036b'))
    #print(bits)
    #print(mask[0])
    for idx, m in enumerate(mask):
        #print(idx, m)
        if m == 'X':
            continue
        else:
            bits[idx] = m
    num = "".join(bits)
    return int(num, 2)


def bits_to_addresses(bits, from_idx):
    addresses = []
    split = False

    for idx in range(from_idx, len(bits)):
        if bits[idx] == 'X':
            address1 = bits.copy()
            address2 = bits.copy()
            address1[idx] = '0'
            address2[idx] = '1'
            addresses += bits_to_addresses(address1, idx+1) + bits_to_addresses(address2, idx+1)
            split = True
            break
    if not split:
        addresses.append(bits)
    
    return addresses


def apply_address_mask(mask, address):
    addresses = []
    bits = list(format(int(address), '036b'))

    for idx, m in enumerate(mask):
        if m == '1':
            bits[idx] = '1'
        elif m == 'X':
            bits[idx] = "X"

    for address in bits_to_addresses(bits, 0):
        address_str = "".join(address)
        addresses.append(int(address_str, 2))

    return addresses


mem = {}
mask = ""
part1 = False

for line in lines:
    l1, l2 = line.split("=")
    l1 = l1.strip()

    if l1 == "mask":
        mask = l2.strip()
    else:
        address = re.match(r'mem\[(.+?)]', l1)[1]
        #print(address, l1, l2)
        value = int(l2)
        if part1:
            value = apply_mask(mask, value)
            mem[address] = value
        else:
            addresses = apply_address_mask(mask, address)

            for address in addresses:
                mem[address] = value
        

sum_ = 0
for val in mem.values():
    sum_ += val
print(sum_)

#print(mem)
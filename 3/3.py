def upper_check(chr):
    return ord(chr) > 64 and ord(chr) < 91

def lower_check(chr):
    return ord(chr) > 96 and ord(chr) < 123

def small_cap_bodyg(data, num_bgs):
    for idx in range(len(data)):
        if idx >= num_bgs and idx < len(data) - num_bgs:
            # if ord(data[idx]) > 96 and ord(data[idx]) < 123:
            if lower_check(data[idx]):
                if upper_check(data[idx-num_bgs+2]) and upper_check(data[idx-num_bgs+1]) and upper_check(data[idx-num_bgs]) and upper_check(data[idx+num_bgs-2]) and upper_check(data[idx+num_bgs-1]) and upper_check(data[idx+num_bgs]):
                    # we need exactly 3 capital letters
                    if (idx - (num_bgs + 1) < 0) and not upper_check(data[idx+num_bgs+1]):
                        print(data[idx], end='')
                    elif (idx + num_bgs + 1) > (len(data) - 1) and not upper_check(data[idx-num_bgs-1]):
                        print(data[idx], end='')
                    elif not upper_check(data[idx+num_bgs+1])  and not upper_check(data[idx-num_bgs-1]):
                        print(data[idx], end='')
                    # print(data[idx-3], data[idx-2], data[idx-1], data[idx], data[idx+1], data[idx+2], data[idx+3], sep='')
                    # print(data[idx], end='')

data=None
with open('data.txt') as f:
    data = f.read()
small_cap_bodyg(data, 3)
text = open('input', 'r')


def get_diffs(seq: list, diffs=None) -> list:
    if diffs is None:
        diffs = []
    if len(seq) == 1:
        return diffs
    return get_diffs(seq[1:], diffs + [seq[1] - seq[0]])


def get_extrapolated_list(seq: list) -> list:
    diffs = get_diffs(seq)
    if all(diff == 0 for diff in diffs):
        return seq + [seq[-1] + diffs[-1]]
    return seq + [seq[-1] + get_extrapolated_list(diffs)[-1]]


def get_backwards_extrapolated_list(seq: list) -> list:
    diffs = get_diffs(seq)
    if all(diff == 0 for diff in diffs):
        return [seq[0] - diffs[0]] + seq
    return [seq[0] - get_backwards_extrapolated_list(diffs)[0]] + seq

answer = 0
answer1 = 0
while True:
    line = text.readline()
    if not line:
        break

    sequence = [int(s) for s in line.split(' ')]
    answer += int(get_extrapolated_list(sequence)[-1])
    answer1 += int(get_backwards_extrapolated_list(sequence)[0])

print(answer)
print(answer1)

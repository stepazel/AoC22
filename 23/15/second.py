steps = open('input', 'r').readline().split(',')
steps[-1] = steps[-1].strip()


def get_hash(string: str, value: int = 0, pos: int = 0) -> int:
    if pos == len(string):
        return value
    code = ord(string[pos])
    value += code
    value = value * 17
    value = value % 256
    return get_hash(string, value, pos + 1)

boxes = {}
for i in range(0, 256):
    boxes[i] = {}
for step in steps:
    operation = '-' if '-' in step else '='
    lens_label = step.split(operation)[0]
    box_number = get_hash(lens_label)
    if operation == '=':
        focal_length = step.split(operation)[1]
        boxes[box_number][lens_label] = focal_length
    if operation == '-':
        try:
            del boxes[box_number][lens_label]
        except KeyError:
            pass

answer = 0
for box_number, box in boxes.items():
    slot_number = 1
    for label, focal_length in box.items():
        answer += (box_number + 1) * slot_number * int(focal_length)
        slot_number += 1
print(answer)

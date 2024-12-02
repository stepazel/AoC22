text = open('2/input', 'r')

safe_reports_count = 0
while True:
    line = text.readline()
    if not line:
        break

    report = list(map(int, line.split(" ")))
    diffs = [report[i + 1] - report[i] for i in range(0, len(report) - 1)]

    is_safe = False
    if all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs):
        if all(0 < abs(diff) <= 3 for diff in diffs):
            safe_reports_count += 1
            is_safe = True
    
    if is_safe:
        continue

    for i in range(0, len(report)):
        new_report = report.copy()
        level = new_report[i]
        del new_report[i]
        diffs = [new_report[i + 1] - new_report[i] for i in range(0, len(new_report) - 1)]

        if all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs):
            if all(0 < abs(diff) <= 3 for diff in diffs):
                safe_reports_count += 1
                break

print(safe_reports_count)

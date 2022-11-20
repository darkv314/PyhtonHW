
def extract_section_rows(data, start_section, end_section=None):
    start_end = [index for index, row in enumerate(data) if start_section in row or end_section in row]
    if len(start_end) == 0:
        return
    if len(start_end) == 1:
        start_end.append(len(data))
    return [(index, row) for index, row in enumerate(data) if row != [] and index > start_end[0] and index < start_end[1]]
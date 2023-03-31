# autograde:all-correct a111111 time:2022-10-26T19:14:48+00:00 UTC
def yolo_index(strings):
    """
    here you could see that we are returning -1 if the string is not there
    """
    if 'yolo' in strings:
        return strings.index('yolo')
    return -1

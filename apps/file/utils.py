from typing import Optional, Union


def sizeof_fmt(num: int, suffix: Optional[str] = "B"):
    """
    Return human-readable from file size from byte.
    :param num: integer, the file size
    :param suffix: str, the unit of the generated human-readable file size (default file unit is Byte so suffix="B")
    :return: str, human-readable file size
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0

    return f"{num:.1f}Yi{suffix}"

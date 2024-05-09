"""

        Write a function, which takes a non-negative integer (seconds) as input and 
        returns the time in a human-readable format (HH:MM:SS)

        HH = hours, padded to 2 digits, range: 00 - 99
        MM = minutes, padded to 2 digits, range: 00 - 59
        SS = seconds, padded to 2 digits, range: 00 - 59

    The maximum time never exceeds 359999 (99:59:59)

    You can find some examples in the test fixtures.

"""

from datetime import datetime
import math


def make_readable(seconds):
    """

        readable time readable

    """
    time= seconds % 3600
    if seconds >=3600 :
        hour = seconds / 3600
        min=math.floor((seconds % 3600)/60)
        second = math.floor(seconds % 60)
        formatted= f"{math.floor(hour)}:{min}:{second}".split(":")
        return ":".join(["0"+x if len(x) == 1 else x for x in formatted ])
    elif seconds >=60 and seconds < 3600 :
        minute=math.floor(seconds / 60)
        second=math.floor(seconds % 60)
        formatted= f"00:{minute}:{second}".split(":")
        return ":".join(["0"+x if len(x) == 1 else x for x in formatted ])
    date = datetime(1,1,1,00,00,time)
    return f"{date:%H:%M:%S}"
print(make_readable(0))

from datetime import datetime
import math

def make_readable(seconds):
    time= seconds % 3600
    if seconds >=3600 :
        hour = seconds / 3600
        rem=math.floor((seconds % 3600)/60)
        sec_rem = math.floor(seconds % 60)
        formatted= f"{math.floor(hour)}:{rem}:{sec_rem}".split(":")
        return ":".join(["0"+x if len(x) == 1 else x for x in formatted ])
    elif seconds >=60 and seconds < 3600 :
        minute=math.floor(seconds / 60)
        rem=math.floor(seconds % 60)
        formatted= f"00:{minute}:{rem}".split(":")
        return ":".join(["0"+x if len(x) == 1 else x for x in formatted ])
    date = datetime(1,1,1,00,00,time)
    return f"{date:%H:%M:%S}"
print(make_readable(0))

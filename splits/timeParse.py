from datetime import timedelta
'''
timeParse method used to convert text time into timedelta time
'''
def timeParse(time):
    if time is None:
        return None
    parts = time.split(":")

    if len(parts) != 3:
        raise ValueError(f"Unexpected time format: {time}")

    hours = int(parts[0])
    minutes = int(parts[1])
    secParts = parts[2].split(".")
    seconds = int(secParts[0])
    milliseconds = int(secParts[1][:3]) if len(secParts) > 1 else 0

    return timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)

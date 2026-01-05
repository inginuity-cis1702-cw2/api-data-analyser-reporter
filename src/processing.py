from datetime import datetime, timezone

# -- datetime helper functions --------------------------------------
# https://bobbyhadz.com/blog/python-format-datetime-am-pm
# https://stackoverflow.com/questions/1759455/how-can-i-account-for-period-am-pm-using-strftime#1759485
def get_utc_time() -> str:
    """
    Return time with tzid=UTC.
    """
    verbose = datetime.now(timezone.utc)
    time    = verbose.strftime("%H:%M:%S %p")
    # print(type(verbose))
    return time

def get_today() -> list:
    verbose = datetime.now(timezone.utc)
    today   = verbose.strftime("%Y-%m-%d").split('-')
    # print(today)
    return today

# -- compare time to sun info ---------------------------------------
# https://blog.finxter.com/5-best-ways-to-compare-times-in-python/
# https://dnmtechs.com/comparing-time-differences-in-python-3/
def time_until(target:str) -> str:
    """
    Returns time until target time. If event has passed then a generic
    string is returned. All times in UTC.

    Inputs should follow: "%I:%M:%S %p"
    """

    assert target[-2:] == 'AM' or target[-2:] == 'PM', (
        "Expected '%I:%M:%S %p'"
    )
    assert len(target_slice := target[:-3].split(':')) == 3, (
        "Expected '%I:%M:%S %p'"
    )
    assert int(target_slice[0]) <= 12, (
        "Expected '%I:%M:%S %p'"
    )

    # -- adjusting current time format  -----------------------------
    verbose      = datetime.now(timezone.utc)
    current_time = datetime.strftime(verbose, "%I:%M:%S %p")

    # -- formats now match ------------------------------------------
    current_time = datetime.strptime(current_time, "%I:%M:%S %p")
    target_time  = datetime.strptime(target, "%I:%M:%S %p")

    diff = target_time - current_time
    if str(diff)[0] == '-':
        return "Time has already passed!"

    return str(diff)




def main() -> None:
    print(get_today())
    print(get_utc_time())
    print(time_until('4:13:22 PM'))



if __name__ == "__main__":
    main()

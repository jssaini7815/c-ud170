from datetime import datetime as dt
#Datestring only not acceptable in hour-minutes-second due to strptime mention
# Convert datestring to datetime
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

# Convert string to int
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

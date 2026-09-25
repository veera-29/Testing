import datetime

def get_current_date():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

print(get_current_date())
from datetime import datetime

def greetings():
    present_time = datetime.now().hour

    if (present_time > 0 and present_time < 12):
        G_m = "Good Morning Sir!"
        return G_m
    elif (present_time >= 12 and present_time < 16):
        G_a = "Good Afternoon Sir!"
        return G_a
    elif (present_time >= 16 and present_time < 24):
        G_e = "Good Evening Sir!"
        return G_e

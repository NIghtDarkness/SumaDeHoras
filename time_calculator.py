def add_time(start, duration, day="False"):

    week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    lapse = 0
    period = ""
    show = None

    startSlices = start.split() #divide la hora inicial en 2 partes, la hora (00:00) y el periodo (AM/PM)
    startHour = startSlices[0].split(":") #separa la hora y los minutos ("00:00" -> ["00","00"])

    durationHour = duration.split(":") #separa la hora y los minutos ("00:00" -> ["00","00"])

    #Time start
    h1 = int(startHour[0])
    m1 = int(startHour[1])

    #Time duration
    h2 = int(durationHour[0])
    m2 = int(durationHour[1])

    if startSlices[1] == "PM":
        h1 += 12

    m1 += m2

    if m1 >= 60:
        h1 += int(m1 / 60)
        m1 %= 60

    h1 += h2
    
    if h1 > 24:
        lapse += int(h1 / 24)
        h1 %= 24

    if h1 < 12:
        period = "AM"
        if h1 == 0 or h1 == 24:
            h1 += 12
    else:
        period = "PM"
        if h1 != 12:
            h1 -= 12

    if day != "False":
        for i in week:
            if day.lower() == i.lower():
                show = (week.index(i) + lapse) % 7
                break

    new_time = str(h1) + ":" + str(m1).zfill(2) + " " + period

    if show != None:
        day = week[show]
        new_time += ", " + day
    if lapse == 1:
        new_time += " (next day)"
    elif lapse > 1:
        new_time += " (" + str(lapse) + " days later)"
    
    #print(new_time)
    return new_time
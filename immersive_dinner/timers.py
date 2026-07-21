import time
import winsound


def timer(item, next_course, config):

   
    if config["duration"] == "original":
        durat = item['duration']
    else:
        durat = config["duration"]

    warning_time = config["warning_time"]

    events = {
        durat: lambda: winsound.Beep(800, 200),
        durat // 2: lambda: winsound.Beep(500, 500),
        3: lambda: winsound.Beep(900, 200),
        2: lambda: winsound.Beep(900, 200),
        1: lambda: winsound.Beep(900, 200),
    }

    while durat > 0:

        print(f"\r\t\t\t\t{durat} seconds left",end="")

        if durat in events:
            events[durat]()

        if durat == warning_time:

            winsound.Beep(1000, 500)

            if next_course:
                print(
                    f"\n\t\t\t\tPrepare {next_course['name']} - {next_course['goal']}"
                )
            else:
                print("\t\t\t\tDining experience ending soon")

        time.sleep(1)
        durat -= 1

    winsound.Beep(1000, 3000)
    print()
    print("\t\t\t\tServe Now\n")
    




    

import datetime

def write_log():
    with open("wwww.txt", "w") as file:
        file.write(f"Current Date and Time: {datetime.datetime.now()}\n")
    print("Log file created.")

write_log()

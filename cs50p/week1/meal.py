def main():
    response = input("What time is it? ")

    clock = convert(response)

    if 18.0 <= clock <= 19.0:
        print("dinner time")
    elif 12.0 <= clock <= 13.0:
        print("lunch time")
    elif 7.0 <= clock <= 8.0:
        print("breakfast time")


def convert(time):
    lt = time.replace(":", " ").split()
    hour = float(lt[0])
    minute = float(lt[1])
    if len(lt) == 3:
        period = lt[2]
        if hour == 12.0 and period == "a.m.":
            hour = 0.0
        elif period == "p.m." and hour <= 11.0:
            hour += 12.0

    total = hour + (minute / 60)

    return total



if __name__ == "__main__":
    main()

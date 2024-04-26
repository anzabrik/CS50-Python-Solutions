import re
import sys


def main():
    print(convert(input("Hours: ")))


# Extract the four meaningful parts for each of the two formats, then insert them into the new format
def convert(s):
    t_list = []
    if matches := re.match(r"(\d+)(:\d\d)?( AM| PM) to (\d+)(:\d\d)?( AM| PM)$", s): # Check that minutes are valid:
        f_h, f_m, f_p, s_h, s_m, s_p = matches.groups()
        t_list = is_valid_time(f_h, f_m, f_p, s_h, s_m, s_p)
    else:
        raise ValueError("Wrong format")

    # Add minutes if they're not there
    if len(t_list) == 4:
        t_list.insert(1, 0)
        t_list.insert(-1, 0)
    # Add 12 hours where PM (we add 12, except if 12PM=12)
    if t_list[2] == " PM":
        if t_list[0] != 12:
            t_list[0] += 12
    # If AM, leave as it is, except 12AM = 0, but change last time
    else:
        if t_list[0] == 12: # If 12AM, make it 00 AND change last
            t_list[0] = 0
            if t_list[3] != 12:
                t_list[3] +=12
        else: # change last time
            if t_list[3] != 12:
                t_list[3] +=12

    # Concatenate
    time = f"{t_list[0]:02}:{t_list[1]:02} to {t_list[3]:02}:{t_list[4]:02}"
    return time


def is_valid_time(f_h, f_m, f_p, s_h, s_m, s_p):
    time_list = []
    f_h = int(f_h)
    if f_h >= 0 and f_h <= 12:
        time_list.append(f_h)
    else:
        raise ValueError("Wrong format")

    if f_m != None:
        f_m = f_m.strip(":")
        f_m = int(f_m)
        if f_m >= 0 and f_m <= 59:
            time_list.append(f_m)
        else:
            raise ValueError("Wrong format")

    time_list.append(f_p)
    s_h = int(s_h)
    if s_h >= 0 and s_h <= 12:
        time_list.append(s_h)
    else:
        raise ValueError("Wrong format")

    if s_m != None:
        s_m = s_m.strip(":")
        s_m = int(s_m)
        if s_m >= 0 and s_m <= 59:
            time_list.append(s_m)
        else:
            raise ValueError("Wrong format")

    time_list.append(s_p)
    return time_list

if __name__ == "__main__":
    main()

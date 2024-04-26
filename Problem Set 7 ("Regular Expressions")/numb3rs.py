import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    nums = []
    if matches := re.match(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for match in matches.groups():
            nums.append(match)
    result = check(nums)
    return result


def check(nums):
    if len(nums) != 4:
        return False
    for num in nums:
        num = int(num)
        if num < 0 or num > 255:
            return False
    return True




if __name__ == "__main__":
    main()
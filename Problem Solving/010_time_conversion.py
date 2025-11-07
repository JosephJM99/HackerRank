'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example

s = '12:01:00PM'
Return '12:01:00'.

s = '12:01:00AM'
Return '00:01:00'.
'''

def timeConversion(s):
    nTime = ""
    if(s[-2:] == "PM"):
        if(int(s[0:2]) < 12):
            nTime += str(12 + int(s[0:2])) + s[2:-2]
        else:
            nTime += str(int(s[0:2])) + s[2:-2]
    else:
        if(s[0:2] == '12'):
            nTime += "00" + s[2:-2]
        else:
            nTime += s[:-2]
    return nTime


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)

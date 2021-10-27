import sys
import csv

def main():
    reader = csv.reader(open(sys.argv[1]))
    date = sys.argv[3]
    header = next(reader)
    allcookies = {}
    for row in reader:
        splitrow = row[0].split(',')
        cookieid = splitrow[0]
        dateinfo = splitrow[1].split("T")
        if dateinfo[0] == date:
            if cookieid in allcookies:
                allcookies[cookieid] += 1
            else:
                allcookies[cookieid] = 1
    sort_cookies = sorted(allcookies.items(), key=lambda x: x[1], reverse=True)
    mostactive = sort_cookies[0][1]
    for cookies in sort_cookies:
        if cookies[1] != mostactive:
            break
        print(cookies[0])

if __name__ == '__main__':
    main()

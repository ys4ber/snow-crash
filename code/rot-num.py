import sys

def main():
    if len(sys.argv) != 3:
        print("erooooooooooooooor" )
        return
    s = sys.argv[1]
    n = int(sys.argv[2])
    res = ""
    for i in s:
        if 'a' <= i <= 'z':
            added = chr(((ord(i) - ord('a') + n) % 26) + ord('a'))
            res += added
        else:
            res += s[i]
    print(res)

if __name__ == "__main__":
            main()
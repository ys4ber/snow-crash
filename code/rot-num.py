import sys

def main():
    if len(sys.argv) != 3:
        print("erooooooooooooooor" )
        return
    s = sys.argv[1]
    n = int(sys.argv[2])
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'b':
            s = s[:i] + chr((ord(s[i]) - ord('a') + n) % 26 + ord('a')) + s[i+1:]
    print(s)

if __name__ == "__main__":
            main()
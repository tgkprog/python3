def main():
    print("Hello World!")
    v = userInt("Enter integer :")
    print(f"Gave {v}.")

def userInt(st):
    try:
        f = input(st)
        return int(f)
    except:
        return 0

if __name__ == "__main__":
    main()

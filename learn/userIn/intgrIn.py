def main():
    print("Hello World!")
    try:
        low = input("Enter lower integer :")
        high = input("Enter high integer :")
        low = int(low) 
        high = int(high)
    except:
        low = 0
        high = 10

    print(f"Using high {high} and low {low} inclusive, for my guesses.")


if __name__ == "__main__":
    main()

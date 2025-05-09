import datetime
import time

def sorta_sum(a, b):
    """
    Returns the sum of a and b, unless the sum falls in the forbidden range [10..19],
    in which case it returns 20 instead.
    """
    total = a + b
    if 10 <= total <= 19:
        return 20
    return total

test_case_count = 0
test_case_error_count = 0

def check_sorta_sum(a, b, expected):
    global test_case_count, test_case_error_count
    test_case_count += 1
    actual = sorta_sum(a, b)
    if actual != expected:
        test_case_error_count += 1
        
        print(f"❌ Test case {test_case_count} FAILED: sorta_sum({a}, {b}) = {actual}, expected {expected}")
    #else:
        # see how much faster test cases run without printing every time! IO takes a long time
        #print(f"✅ Test case {test_case_count} passed.")

def test_cases():
    global test_case_count, test_case_error_count
    print("🧪 Starting test cases...")
    print("📅", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    start_time = time.perf_counter_ns()

    check_sorta_sum(3, 4, 7)
    check_sorta_sum(9, 4, 20)
    check_sorta_sum(10, 10, 20)
    check_sorta_sum(5, 5, 20)
    check_sorta_sum(6, 2, 8)
    check_sorta_sum(-3, 3, 0)

    duration_ms = time.perf_counter_ns() - start_time
    print(f"\n✅ Ran {test_case_count} test cases in {duration_ms} ns, errors: {test_case_error_count}")

def main():
    answer = input("Run test cases? (Y/N): ").strip().lower()
    if answer == 'y':
        test_cases()

    while True:
        user_input = input("\nEnter two integers, seperated by space (or 'q' to quit): ").strip()
        if user_input.lower().startswith('q'):
            print("Exiting.")
            break

        try:
            parts = user_input.split()
            if len(parts) != 2:
                print("❗ Please enter exactly two numbers separated by space.")
                continue
            if parts[0].lower().startswith('q') or parts[1].lower().startswith('q'):
                print("Exiting.")
                break
            a, b = int(parts[0]), int(parts[1])
            result = sorta_sum(a, b)
            print(f"✅ Result: {result}")
        except ValueError:
            print("❗ Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()

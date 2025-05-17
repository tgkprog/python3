import datetime
import time

def sorta_sum(a, b):
    """
    Returns the sum of a and b, unless the sum falls in the forbidden range [10..19],
    in which case it returns 20 instead.
    """
    #print("val; is :")  # print ("gl1 val; is :", gl1)
    total = a + b
    if 10 <= total <= 19:
        return 20
    return total

test_case_count = 0
test_case_error_count = 0

def check_sorta_sum(a, b, expected, show_success):
    global test_case_count, test_case_error_count
    test_case_count += 1
    actual = sorta_sum(a, b)
    if actual != expected:
        test_case_error_count += 1
        print(f"❌ Test case {test_case_count} FAILED: sorta_sum({a}, {b}) = {actual}, expected {expected}")
    elif show_success:
        print(f"✅ Test case {test_case_count} passed.")

def test_cases(show_success=False):
    global test_case_count, test_case_error_count
    print("🧪 Starting test cases...")
    print("📅", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    start_time = time.perf_counter_ns()

    check_sorta_sum(3, 4, 7, show_success)
    check_sorta_sum(9, 4, 20, show_success)
    check_sorta_sum(10, 10, 20, show_success)
    check_sorta_sum(5, 5, 20, show_success)
    check_sorta_sum(6, 2, 8, show_success)
    check_sorta_sum(-3, 3, 0, show_success)

    duration_ns = time.perf_counter_ns() - start_time
    print(f"\n✅ Ran {test_case_count} test cases in {duration_ns} ns, errors: {test_case_error_count}")

def main():
    answer = (input("Run test cases? (Y/N): ").lower() + ' ')[0]
    if answer == 'y':
        show_succ = (input("Show success messages (see difference in time to execute with and without, IO takes a lot of time!)? (Y/N): ").lower() + ' ')[0]
        test_cases(show_success=(show_succ == 'y'))

    while True:
        user_input = input("\nEnter two integers, separated by space (or 'q' to quit): ").strip()
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

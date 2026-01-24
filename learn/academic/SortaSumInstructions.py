# =============================================================================
#  sorta_sum20_guide.py
#
#  This file is a SAMPLE GUIDE, similar in spirit to the Java “IcyHot.java”
#  file you provided. This is NOT the interview question. Your real question
#  will be different.
#
#  The goal: show the full structure expected in Python.
#
#  Everything below is pure Python and runnable.
#  All “instructions” are in comments.
#
# =============================================================================


# =============================================================================
#  GENERAL INSTRUCTIONS
#
#  1. Read all instructions. Slowly.
#     Then read them again.
#
#  2. Your actual interview problem will be different. It will have
#     different parameters, different rules, different edge-cases.
#
#  3. The structure you must follow:
#
#       - a target function: your real problem’s function
#       - a test helper: takes the SAME parameters as target + expected
#       - a test cases function: calls helper repeatedly for many cases
#       - a main(): which calls test cases and also optionally lets user
#         run the target function interactively.
#
#  4. You will be judged mainly on:
#       - correct logic in the target function
#       - correctness of expected values in test helper
#       - enough test cases including edge cases
#
#  5. For YOUR real question:
#       - adapt function name
#       - adapt parameters
#       - adapt return type
#       - rewrite all test cases
#
#  6. Keep everything in a single .py file.
#
#  7. No fancy libraries are required. Use only Python’s built-ins.
#
# =============================================================================


import datetime
import time

# =============================================================================
#  SAMPLE TARGET FUNCTION
#
#  This is ONLY a demo. Your real interview question will have different logic.
#
#  SAMPLE QUESTION:
#    "Given two integers a and b, return their sum.
#     BUT if the sum falls in the forbidden range 10..19,
#     return 20 instead."
#
#  Examples:
#      sorta_sum(3,4) -> 7
#      sorta_sum(9,4) -> 20
#      sorta_sum(10,10) -> 20
# =============================================================================

def sorta_sum(a, b):
    total = a + b
    if 10 <= total <= 19:
        return 20
    return total


# global counters for test results
test_case_count = 0
test_case_error_count = 0


# =============================================================================
#  TEST HELPER
#
#  IMPORTANT:
#   * Must receive same parameters as target function + 1 extra expected value.
#   * For your actual interview question, modify parameter list accordingly.
#   * This calls the target function, compares output to expected, prints error.
#
# =============================================================================

def check_sorta_sum(a, b, expected):
    global test_case_count, test_case_error_count
    test_case_count += 1

    try:
        actual = sorta_sum(a, b)
    except Exception as e:
        print(f"❌ ERROR: Exception raised for input ({a}, {b}): {e}")
        test_case_error_count += 1
        return

    if actual != expected:
        print(f"❌ FAILED: sorta_sum({a}, {b}) = {actual}, expected {expected}")
        test_case_error_count += 1


# =============================================================================
#  TEST CASES FUNCTION
#
#  Add MANY test cases.
#  Include valid cases, boundary cases, negative numbers, weird inputs.
#  For your real question: CHANGE ALL THESE.
#
# =============================================================================

def test_cases():
    print("Running sorta_sum test cases at", datetime.datetime.now())
    start = time.perf_counter_ns()

    check_sorta_sum(3, 4, 7)
    check_sorta_sum(9, 4, 20)
    check_sorta_sum(10, 10, 20)
    check_sorta_sum(5, 5, 20)
    check_sorta_sum(6, 2, 8)
    check_sorta_sum(-3, 3, 0)

    end = time.perf_counter_ns()
    print(f"\nTotal cases: {test_case_count}, Errors: {test_case_error_count}")
    print(f"Time: {end - start} ns\n")


# =============================================================================
#  MAIN
#
#  Runs test cases, then lets user manually try inputs.
#  Keep this structure for your real problem.
# =============================================================================

def main():
    test_cases()

    while True:
        raw = input("Enter two integers (or 'q' to quit): ").strip()
        if raw.lower().startswith("q"):
            print("bye.")
            break

        parts = raw.split()
        if len(parts) != 2:
            print("enter exactly two numbers.")
            continue

        try:
            a = int(parts[0])
            b = int(parts[1])
            print("Result:", sorta_sum(a, b))
        except ValueError:
            print("not integers.")


if __name__ == "__main__":
    main()

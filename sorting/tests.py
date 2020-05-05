def test(sort_func):
    cases = [
        [4, 3, 2, 7, 5],
        [5],
        [None],
        [],
        [3, 3, 3, 3],
        [-5, 3, 1, 2, 3]
    ]

    print(f"Testing {sort_func.__name__}:")

    for i, case in enumerate(cases):
        result = sort_func(case.copy())
        sorted_case = sorted(case)
        correct = result == sorted_case
        print(f"Case {i+1} {'passed' if correct else 'failed'}")
        if not correct:
            print("\tInput:", case)
            print("\tExpected result:", sorted_case)
            print("\tActual result:", result)

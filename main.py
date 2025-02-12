import sys

expected_path = sys.argv[1]
user_path = sys.argv[2]

with open(expected_path) as expected_output:
    with open(user_path) as user_output:
        with open("./result/diff.txt", "w") as diff:
            line = 1
            expected_line = expected_output.readline().strip()
            user_line = user_output.readline().strip()

            while expected_line != "":
                if expected_line != user_line:
                    diff.write(f"(saída esperada): {expected_line} (sua saída): {user_line} (linha): {line}\n")
                line += 1
                expected_line = expected_output.readline().strip()
                user_line = user_output.readline().strip()

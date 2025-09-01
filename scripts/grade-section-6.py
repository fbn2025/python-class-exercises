import importlib.util
import pathlib
import argparse
import contextlib
import io

TESTCASES = [
    {"input": [1, 2, 3, 4, 5, 6, 7, 8, 9], "expected_output": (1, 9)},
    {"input": [-8, -6, 9, -90, 344, 3849, 10e2], "expected_output": (-90, 3849)},
    {"input": [57839848, 3839489340, -389248, 3489234892, 338923893], "expected_output": (-389248, 3839489340)},
    {"input": [10e22, -10e10, 38, -40], "expected_output": (-1e11, 1e23)},
    {"input": [-2, -3, -4, -5, -6, -7, -11], "expected_output": (-11, -2)},
]

def safe_import(file: pathlib.Path):
    spec = importlib.util.spec_from_file_location("student", file)
    student = importlib.util.module_from_spec(spec)
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        spec.loader.exec_module(student)
    return student

def grade(file: pathlib.Path) -> tuple[bool, str]:
    directory = file.parent.name
    lines = [f"\n--- Test Report for {directory} - {file._raw_paths[0]} ---"]

    student = safe_import(file)

    all_passed = True
    
    for i, case in enumerate(TESTCASES, 1):
        try:
            result = student.find_min_max(*case["input"])
        except Exception as e:
            all_passed = False
            lines.append(f"Test {i}: ❌ Error while running")
            lines.append(f"   Error: {e}")
            continue
        if result == case["expected_output"]:
            lines.append(f"Test {i}: ✅ Passed")
        else:
            all_passed = False
            lines.append(f"Test {i}: ❌ Failed")
            lines.append(f"   Expected: {case['expected_output']}")
            lines.append(f"   Got     : {result}")
    if all_passed:
        lines.append("🎉 All tests passed!")

    return all_passed, "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--only-show-failing", action="store_true")
    parser.add_argument("--save-output", action="store_true")
    parser.add_argument("--output-file", type=str, default="section-6-assesment-output.txt")

    args = parser.parse_args()

    base = pathlib.Path("day1/section-6")

    reports = []

    if args.only_show_failing:
        reports.append("Results for failing solutions")
    else:
        reports.append("Results for all solutions")

    for file in list(base.glob("*/main.py")):
        all_passed, report = grade(file)
        if args.only_show_failing:
            if not all_passed: 
                print(report)
                reports.append(report)
        else:
            print(report)
            reports.append(report)

    if args.save_output:
        output_file = pathlib.Path(args.output_file)
        output_file.write_text("\n".join(reports))
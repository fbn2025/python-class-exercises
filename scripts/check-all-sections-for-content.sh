#!/bin/bash

toplevel=$(git rev-parse --show-toplevel)
cd "$toplevel" || exit

for section in day1/section-*/; do
    section_name=$(basename "$section")
    echo -e "Checking solutions for $section_name\n"

    student_lines=()

    for file in "$section"*/main.py; do
        if [[ -f "$file" ]]; then
            student_name=$(basename "$(dirname "$file")")
            lines=$(wc -l < "$file")
            student_lines+=("${file}:${lines}")
        fi
    done

    if [ ${#student_lines[@]} -eq 0 ]; then
        echo "No submissions found for $section_name."
        echo -e "\n\n"
        continue
    fi

    ./statistic_grader/statistic_grader "${student_lines[@]}"

    echo -e "\n\n\n"
done

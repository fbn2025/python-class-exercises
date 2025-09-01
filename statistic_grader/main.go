package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
)

type Student struct {
	Name    string
	Lines   int
	Outlier string
}

// Helper to compute median
func median(nums []int) float64 {
	n := len(nums)
	if n == 0 {
		return 0
	}
	sort.Ints(nums)
	if n%2 == 1 {
		return float64(nums[n/2])
	}
	return float64(nums[n/2-1]+nums[n/2]) / 2.0
}

// Compute mean
func mean(nums []int) float64 {
	total := 0
	for _, n := range nums {
		total += n
	}
	if len(nums) == 0 {
		return 0
	}
	return float64(total) / float64(len(nums))
}

// Compute standard deviation
func stddev(nums []int, avg float64) float64 {
	var sum float64
	for _, n := range nums {
		diff := float64(n) - avg
		sum += diff * diff
	}
	if len(nums) <= 1 {
		return 0
	}
	return sqrt(sum / float64(len(nums)))
}

// Simple sqrt using Newton's method
func sqrt(x float64) float64 {
	z := x
	for i := 0; i < 20; i++ {
		z -= (z*z - x) / (2 * z)
	}
	return z
}

// Compute Q1, Q3, IQR
func quartiles(nums []int) (q1, q3 float64) {
	n := len(nums)
	sort.Ints(nums)
	q1Index := n / 4
	q3Index := (3 * n) / 4
	q1 = float64(nums[q1Index])
	q3 = float64(nums[q3Index])
	return
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Usage: go run stats.go <name:lines> ...")
		fmt.Println("Example: go run stats.go alice:123 bob:5 carol:120")
		return
	}

	var students []Student
	var lines []int

	for _, arg := range os.Args[1:] {
		parts := split(arg, ':')
		if len(parts) != 2 {
			fmt.Println("Invalid input:", arg)
			continue
		}
		name := parts[0]
		num, err := strconv.Atoi(parts[1])
		if err != nil {
			fmt.Println("Invalid number for", name, ":", parts[1])
			continue
		}
		students = append(students, Student{Name: name, Lines: num})
		lines = append(lines, num)
	}

	if len(students) == 0 {
		fmt.Println("No valid students.")
		return
	}

	avg := mean(lines)
	med := median(lines)
	sd := stddev(lines, avg)
	q1, q3 := quartiles(lines)
	iqr := q3 - q1

	// Detect outliers (IQR method)
	for i := range students {
		if float64(students[i].Lines) < q1-1.5*iqr {
			students[i].Outlier = "LOW OUTLIER"
		} else if float64(students[i].Lines) > q3+1.5*iqr {
			students[i].Outlier = "HIGH OUTLIER"
		} else {
			students[i].Outlier = ""
		}
	}

	// Sort students by line count descending
	sort.Slice(students, func(i, j int) bool {
		return students[i].Lines > students[j].Lines
	})

	// Print table
	fmt.Println("Student     Lines")
	fmt.Println("----------------")
	for _, s := range students {
		if s.Outlier != "" {
			fmt.Printf("%-10s %-5d <-- %s\n", s.Name, s.Lines, s.Outlier)
		} else {
			fmt.Printf("%-10s %-5d\n", s.Name, s.Lines)
		}
	}

	fmt.Println("\nStatistics:")
	fmt.Printf("Count: %d, Mean: %.2f, Median: %.2f, SD: %.2f, Q1: %.2f, Q3: %.2f, IQR: %.2f\n",
		len(students), avg, med, sd, q1, q3, iqr)
}

// simple split function (like strings.Split)
func split(s string, sep byte) []string {
	var res []string
	last := 0
	for i := 0; i < len(s); i++ {
		if s[i] == sep {
			res = append(res, s[last:i])
			last = i + 1
		}
	}
	res = append(res, s[last:])
	return res
}

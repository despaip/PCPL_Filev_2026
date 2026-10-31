package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
)

func getCoef(index int, prompt string) float64 {
	var coef float64
	var err error

	if len(os.Args) > index {
		coef, err = strconv.ParseFloat(os.Args[index], 64)

		if err == nil {
			return coef
		}

		fmt.Printf("Error: %v. Try again.\n", err)
	}

	for {
		fmt.Print(prompt)
		_, err = fmt.Scan(&coef)

		if err == nil {
			return coef
		}

		fmt.Printf("Error: %v. Try again.\n", err)
	}
}

func getRoots(a, b, c float64) []float64 {
	var roots []float64

	D := b*b - 4*a*c

	if D > 0 {
		root1 := math.Sqrt((-b + math.Sqrt(D)) / (2 * a))
		root2 := math.Sqrt((-b - math.Sqrt(D)) / (2 * a))
		root3 := -root1
		root4 := -root2
		roots = append(roots, root1, root2, root3, root4)
	} else if D == 0 {
		root1 := math.Sqrt(-b / (2 * a))
		root2 := -root1
		roots = append(roots, root1, root2)
	}

	return roots
}

func printRoots(roots []float64) {
	if len(roots) == 4 {
		fmt.Printf("Found 4 roots: %f, %f, %f and %f.\n", roots[0], roots[1], roots[2], roots[3])
	} else if len(roots) == 2 {
		fmt.Printf("Found 2 roots: %f and %f.\n", roots[0], roots[1])
	} else {
		fmt.Println("No roots were found.")
	}
}

func main() {
	a := getCoef(1, "Enter A: ")
	b := getCoef(2, "Enter B: ")
	c := getCoef(3, "Enter C: ")

	roots := getRoots(a, b, c)

	printRoots(roots)
}

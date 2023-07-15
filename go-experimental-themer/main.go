package main

import (
	"fmt"
	"os"
)

func main() {
	theme_file, err := os.Open("example.json")

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("Successfully opened example.json")

	defer theme_file.Close()
}

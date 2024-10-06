package main

import (
	"fmt"
	"time"
)

func main() {
	var age int
	var name, ln string
	name, ln, age = "John", "Doe", 25
	fmt.Println(name, ln, age, time.Now())
}

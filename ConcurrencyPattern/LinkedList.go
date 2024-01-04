package main

import "fmt"

type List *Node

type Node struct {
	next    List
	element int
}

func Append(list *List, element int) {
	if *list == nil {
		*list = &Node{nil, element}
	} else {
		Append(&((*list).next), element)
	}
}

func AppendFirst(list *List, element int) {
	*list = &Node{*list, element}
}

func Print(list List) {
	node := list
	for node != nil {
		fmt.Print(node.element, " ")
		node = node.next
	}
	fmt.Println("")
}

func main() {
	var list List = nil
	for i := 0; i < 10; i++ {
		AppendFirst(&list, i)
		//Append(&list, i)
	}
	Print(list)
}

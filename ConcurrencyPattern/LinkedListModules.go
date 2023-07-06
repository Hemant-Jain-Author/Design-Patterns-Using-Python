package main

import "fmt"

type List struct {
	head *Node
}

type Node struct {
	next    *Node
	element int
}

func (list *List) Append(element int) {
	if list.head == nil {
		list.head = &Node{nil, element}
	} else {
		node := list.head
		for node.next != nil {
			node = node.next
		}
		node.next = &Node{nil, element}
	}
}

func (list *List) AppendFirst(element int) {
	list.head = &Node{list.head, element}
}

func (list *List) Print() {
	node := list.head
	for node != nil {
		fmt.Print(node.element, " ")
		node = node.next
	}
	fmt.Println("")
}

func main() {
	ll := List{}
	for i := 0; i < 10; i++ {
		ll.AppendFirst(i)
		// ll.Append(i)
	}
	ll.Print()
}

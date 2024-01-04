package main

import (
	"fmt"
)

type List struct {
	head  *ListNode
	count int
}

type ListNode struct {
	value int
	next  *ListNode
}

// Sum returns the sum of the list elements using recursion.
func (list *List) Sum() int {
	return list.sumRecursive(list.head)
}

func (list *List) sumRecursive(node *ListNode) int {
	if node == nil {
		return 0
	}
	return node.value + list.sumRecursive(node.next)
}

func (list *List) Size() int {
	return list.count
}

func (list *List) IsEmpty() bool {
	return (list.count == 0)
}

func (list *List) Peek() (int, bool) {
	if list.IsEmpty() {
		fmt.Println("EmptyListException")
		return 0, false
	}
	return list.head.value, true
}

func (list *List) AddHead(value int) {
	list.head = &ListNode{value, list.head}
	list.count++
}

func (list *List) AddTail(value int) {
	list.head = list.addTailRecursive(list.head, value)
	list.count++
}

func (list *List) addTailRecursive(node *ListNode, value int) *ListNode {
	if node == nil {
		return &ListNode{value, nil}
	}
	node.next = list.addTailRecursive(node.next, value)
	return node
}

func (list *List) Print() {
	list.printRecursive(list.head)
	fmt.Println("")
}

func (list *List) printRecursive(node *ListNode) {
	if node == nil {
		return
	}
	fmt.Print(node.value, " ")
	list.printRecursive(node.next)
}

func (list *List) SortedInsert(value int) {
	newNode := &ListNode{value, nil}
	list.head = list.sortedInsertRecursive(list.head, newNode)
	list.count++
}

func (list *List) sortedInsertRecursive(curr *ListNode, newNode *ListNode) *ListNode {
	if curr == nil || curr.value > newNode.value {
		newNode.next = curr
		return newNode
	}
	curr.next = list.sortedInsertRecursive(curr.next, newNode)
	return curr
}

func (list *List) Find(data int) bool {
	return list.findRecursive(list.head, data)
}

func (list *List) findRecursive(node *ListNode, data int) bool {
	if node == nil {
		return false
	}
	if node.value == data {
		return true
	}
	return list.findRecursive(node.next, data)
}

func (list *List) RemoveHead() (int, bool) {
	if list.IsEmpty() {
		fmt.Println("EmptyListException")
		return 0, false
	}
	value := list.head.value
	list.head = list.head.next
	list.count--
	return value, true
}

func (list *List) DeleteNode(delValue int) bool {
	list.head = list.deleteNodeRecursive(list.head, delValue)
	return true
}

func (list *List) deleteNodeRecursive(node *ListNode, delValue int) *ListNode {
	if node == nil {
		return nil
	}
	if node.value == delValue {
		list.count--
		return node.next
	}
	node.next = list.deleteNodeRecursive(node.next, delValue)
	return node
}

func (list *List) DeleteNodes(delValue int) {
	list.head = list.deleteNodesRecursive(list.head, delValue)
}

func (list *List) deleteNodesRecursive(node *ListNode, delValue int) *ListNode {
	if node == nil {
		return nil
	}
	if node.value == delValue {
		list.count--
		return list.deleteNodesRecursive(node.next, delValue)
	}
	node.next = list.deleteNodesRecursive(node.next, delValue)
	return node
}

func (list *List) FreeList() {
	list.head = nil
	list.count = 0
}

func (list *List) Reverse() {
	curr := list.head
	var prev, next *ListNode
	for curr != nil {
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	}
	list.head = prev
}

func (list *List) ReverseRecurse() {
	list.reverseRecurseUtil(list.head, nil)
}

func (list *List) reverseRecurseUtil(currentNode *ListNode, nextNode *ListNode) {
	if currentNode == nil {
		return
	}
	if currentNode.next == nil {
		currentNode.next = nextNode
		list.head = currentNode
		return
	}
	list.reverseRecurseUtil(currentNode.next, currentNode)
	currentNode.next.next = currentNode
	currentNode.next = nextNode
}

func (list *List) RemoveDuplicate() {
	list.head = list.removeDuplicateRecursive(list.head)
}

func (list *List) removeDuplicateRecursive(node *ListNode) *ListNode {
	if node == nil || node.next == nil {
		return node
	}
	if node.value == node.next.value {
		list.count--
		node.next = list.removeDuplicateRecursive(node.next)
		return node.next
	}
	node.next = list.removeDuplicateRecursive(node.next)
	return node
}

func (list *List) CopyListReversed() *List {
	ll2 := new(List)
	ll2.head = list.copyListReversedUtil(list.head)
	ll2.count = list.count
	return ll2
}

func (list *List) copyListReversedUtil(current *ListNode) *ListNode {
	if current == nil {
		return nil
	}

	newNode := &ListNode{value: current.value}
	if current.next != nil {
		newNode.next = list.copyListReversedUtil(current.next)
	}

	return newNode
}

func (list *List) CopyList() *List {
	ll2 := new(List)
	ll2.head = list.copyListUtil(list.head)
	ll2.count = list.count
	return ll2
}

func (list *List) copyListUtil(current *ListNode) *ListNode {
	if current == nil {
		return nil
	}

	newNode := &ListNode{value: current.value}
	newNode.next = list.copyListUtil(current.next)

	return newNode
}

func (list *List) CompareList(ll *List) bool {
	return list.compareListUtil(list.head, ll.head)
}

func (list *List) compareListUtil(head1 *ListNode, head2 *ListNode) bool {
	if head1 == nil && head2 == nil {
		return true
	} else if head1 == nil || head2 == nil || head1.value != head2.value {
		return false
	}

	return list.compareListUtil(head1.next, head2.next)
}

func (list *List) FindLength() int {
	return list.findLengthUtil(list.head)
}

func (list *List) findLengthUtil(current *ListNode) int {
	if current == nil {
		return 0
	}

	return 1 + list.findLengthUtil(current.next)
}

func (list *List) NthNodeFromBegining(index int) (int, bool) {
	if index > list.Size() || index < 1 {
		fmt.Println("TooFewNodes")
		return 0, false
	}

	return list.nthNodeFromBeginingUtil(list.head, index)
}

func (list *List) nthNodeFromBeginingUtil(current *ListNode, index int) (int, bool) {
	if current == nil {
		return 0, false
	}

	if index == 1 {
		return current.value, true
	}

	return list.nthNodeFromBeginingUtil(current.next, index-1)
}

func (list *List) NthNodeFromEnd(index int) (int, bool) {
	size := list.FindLength()
	if size != 0 && size < index {
		fmt.Println("TooFewNodes")
		return 0, false
	}

	startIndex := size - index + 1
	return list.NthNodeFromBegining(startIndex)
}

func (list *List) NthNodeFromEnd2(index int) (int, bool) {
	return list.nthNodeFromEndUtil(list.head, index, 1)
}

func (list *List) nthNodeFromEndUtil(curr *ListNode, index, count int) (int, bool) {
	if curr == nil {
		fmt.Println("TooFewNodes")
		return 0, false
	}

	if count == index {
		return curr.value, true
	}

	return list.nthNodeFromEndUtil(curr.next, index, count+1)
}

func (list *List) MakeLoop() {
	list.makeLoopUtil(list.head, list.head)
}

func (list *List) makeLoopUtil(curr *ListNode, head *ListNode) {
	if curr.next == nil {
		curr.next = head
		return
	}

	list.makeLoopUtil(curr.next, head)
}

func (list *List) LoopDetect() bool {
	return list.loopDetectUtil(list.head, list.head)
}

func (list *List) loopDetectUtil(slowPtr *ListNode, fastPtr *ListNode) bool {
	if fastPtr == nil || fastPtr.next == nil {
		fmt.Println("loop not found")
		return false
	}

	if slowPtr == fastPtr {
		fmt.Println("loop found")
		return true
	}

	return list.loopDetectUtil(slowPtr.next, fastPtr.next.next)
}

func (list *List) ReverseListLoopDetect() bool {
	tempHead := list.head
	list.Reverse()
	defer list.Reverse()

	if tempHead == list.head {
		fmt.Println("loop found")
		return true
	}

	fmt.Println("loop not found")
	return false
}

func (list *List) LoopTypeDetect() int {
	return list.loopTypeDetectUtil(list.head, list.head, list.head)
}

func (list *List) loopTypeDetectUtil(slowPtr *ListNode, fastPtr *ListNode, head *ListNode) int {
	if fastPtr == nil || fastPtr.next == nil {
		fmt.Println("loop not found")
		return 0
	}

	if head == fastPtr.next || head == fastPtr.next.next {
		fmt.Println("circular list loop found")
		return 2
	}

	if slowPtr == fastPtr {
		fmt.Println("loop found")
		return 1
	}

	return list.loopTypeDetectUtil(slowPtr.next, fastPtr.next.next, head)
}

func (list *List) RemoveLoop() {
	loopPoint := list.LoopPointDetect()
	if loopPoint == nil {
		return
	}

	firstPtr := list.head
	if loopPoint == list.head {
		for firstPtr.next != list.head {
			firstPtr = firstPtr.next
		}
		firstPtr.next = nil
		return
	}

	secondPtr := loopPoint
	list.removeLoopUtil(firstPtr, secondPtr)
}

func (list *List) removeLoopUtil(firstPtr *ListNode, secondPtr *ListNode) {
	if firstPtr.next != secondPtr.next {
		list.removeLoopUtil(firstPtr.next, secondPtr.next)
	} else {
		secondPtr.next = nil
	}
}

func (list *List) LoopPointDetect() *ListNode {
	return list.loopPointDetectUtil(list.head, list.head)
}

func (list *List) loopPointDetectUtil(slowPtr *ListNode, fastPtr *ListNode) *ListNode {
	if fastPtr == nil || fastPtr.next == nil {
		return nil
	}

	if slowPtr == fastPtr {
		return slowPtr
	}

	return list.loopPointDetectUtil(slowPtr.next, fastPtr.next.next)
}

func (list *List) FindIntersection(list2 List) *ListNode {
	l1 := list.Size()
	l2 := list2.Size()

	var diff int
	if l1 < l2 {
		list.head, list2.head = list2.head, list.head // Swap the heads
		diff = l2 - l1
	} else {
		diff = l1 - l2
	}

	return list.findIntersectionUtil(list.head, list2.head, diff)
}

func (list *List) findIntersectionUtil(head1 *ListNode, head2 *ListNode, diff int) *ListNode {
	if head1 == nil || head2 == nil {
		return nil
	}

	if diff > 0 {
		return list.findIntersectionUtil(head1.next, head2, diff-1)
	} else if diff < 0 {
		return list.findIntersectionUtil(head1, head2.next, diff+1)
	} else {
		if head1 == head2 {
			return head1
		}
		return list.findIntersectionUtil(head1.next, head2.next, 0)
	}
}

func main1() {
	ll := new(List) // or ll := List{}
	ll.AddHead(1)
	ll.AddHead(2)
	ll.AddHead(3)
	ll.Print()
	fmt.Println("Size :", ll.Size())
	fmt.Println("IsEmpty :", ll.IsEmpty())
	fmt.Println(ll.Peek())
}

/*
3 2 1
Size : 3
IsEmpty : false
3 true
*/

func main2() {
	ll := List{}
	ll.SortedInsert(1)
	ll.SortedInsert(2)
	ll.SortedInsert(3)
	ll.SortedInsert(1)
	ll.SortedInsert(2)
	ll.SortedInsert(3)
	ll.Print()

}

/*
1 1 2 2 3 3
*/

func main3() {
	ll := new(List) // or ll := List{}
	ll.AddHead(1)
	ll.AddHead(2)
	ll.AddHead(1)
	ll.AddHead(2)
	ll.AddHead(1)
	ll.AddHead(3)
	ll.Print()
	ll.DeleteNode(2)
	ll.Print()
	ll.DeleteNodes(1)
	ll.Print()
}

/*
3 1 2 1 2 1
3 1 1 2 1
*/

func main4() {
	ll := new(List) // or ll := List{}
	ll.AddHead(1)
	ll.AddHead(2)
	ll.AddHead(3)
	ll.Print()
	ll.Reverse()
	ll.Print()
}

/*
3 2 1
1 2 3
*/

func main5() {
	ll := List{}
	ll.SortedInsert(1)
	ll.SortedInsert(2)
	ll.SortedInsert(3)
	ll.SortedInsert(1)
	ll.SortedInsert(2)
	ll.SortedInsert(3)
	ll.Print()
	ll.RemoveDuplicate()
	ll.Print()
}

/*
1 1 2 2 3 3
1 2 3
*/

func main6() {
	ll := List{}
	ll.AddHead(1)
	ll.AddHead(2)
	ll.AddHead(3)
	ll.Print()

	ll2 := ll.CopyList()
	ll2.Print()
	fmt.Println(ll.CompareList(ll2))

	ll3 := ll.CopyListReversed()
	ll3.Print()
}

/*
3 2 1
3 2 1
true
1 2 3
*/

func main7() {
	ll := List{}
	ll.AddHead(1)
	ll.AddHead(2)
	ll.AddHead(3)
	ll.Print()
	ll.MakeLoop()
	ll.LoopDetect()
	ll.ReverseListLoopDetect()
	ll.LoopTypeDetect()
	ll.RemoveLoop()
	ll.LoopDetect()
}

/*
3 2 1
loop found
loop found
circular list loop found
loop not found
*/

func main() {
	ll := List{}
	ll.AddHead(1)
	ll.AddHead(2)
	ll2 := List{}
	ll2.AddHead(3)
	ll2.head.next = ll.head
	ll.AddHead(4)
	ll2.AddHead(5)
	ll.Print()
	ll2.Print()
	nd := ll.FindIntersection(ll2)
	fmt.Print("Intersection :: ", nd.value)
}

/*
4 2 1
5 3 2 1
Intersection :: 2
*/

func main9() {
	ll := List{}
	ll.AddHead(1)
	ll.AddHead(2)
	ll.AddHead(3)
	ll.Print()
	fmt.Println(ll.NthNodeFromBegining(2))
	fmt.Println(ll.NthNodeFromEnd(2))
	fmt.Println(ll.NthNodeFromEnd2(2))
}

func main10() {
	ll := List{}
	ll.AddHead(1)
	ll.AddHead(2)
	ll.AddHead(3)
	ll.AddTail(1)
	ll.AddTail(2)
	ll.AddTail(3)
	ll.Print()
	fmt.Println(ll.Size())
	fmt.Println(ll.IsEmpty())
	fmt.Println(ll.Peek())
	ll.DeleteNodes(3)
	ll.Print()
	fmt.Println(ll.Find(3))
	ll.RemoveHead()
	ll.Print()
	ll.FreeList()
	ll.Print()

}

func main99() {
	main1()
	main2()
	main3()
	main4()
	main5()
	main6()
	main7()
	//main8()
	main9()
	main10()
}

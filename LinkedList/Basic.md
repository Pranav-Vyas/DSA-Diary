# Singly LinkedList

### Insert

1. First create a node with a value that is to be inserted at the beginning of LinkedList.

2. Point the next of the newly created Node to the head of the LinkedList.

3. As the node is inserted at the beginning of LinkedList, this is the first Node in LinkedList. So point the head of the LinkedList to the newly created Node.

### Delete

Deletion of Last Node in Singly LinkedList is 2 step process.

1. Find the last Node and second Last Node of the LinkedList. To Find the Nodes, take two ListNode pointers let’s say prev, curr. Initially curr points to the head and prev points to the Null. Move the curr and prev pointers ahead in the LinkedList until the curr reaches the last Node. 

2. We need to remove the Last node, so break the link connecting the LastNode with List. In order to break the link, make prev→next = NULL

# Doubly LinkedList

### Reverse

```
node*temp = NULL;
node*curr = head;

/* swap next and prev for all nodes of
doubly linked list */
while (curr != NULL)
{
    temp = curr->prev;
    curr->prev = curr->next;
    curr->next = temp;          
    curr = curr->prev;
}


//Edge case if our linked list is empty Or list with only one node

if(temp != NULL )
    head = temp->prev;
```
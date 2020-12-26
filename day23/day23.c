#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/** A node (or entry) in a doubly linked list */
typedef struct node {
	unsigned int num;
	struct node * next;
	struct node * prev;
} ll_e;

/** The list */
typedef struct {
	ll_e * head;
	ll_e * tail;
	ll_e ** nodes; //A summary of nodes, indexed by their contained num - to make search O(1)
} dll_t;

/** Create a doubly linked list given a initialisation array */
dll_t * create_list(int* starting_list, int list_size) {
	dll_t * list = malloc(sizeof(dll_t));
	ll_e * nxt = (ll_e*)malloc(sizeof(ll_e));
	list->nodes = malloc(sizeof(ll_e*) * (list_size+1));
	list->head = nxt;
	list->head->prev = NULL;
	for (int i = 0; i < list_size; i++) {
		nxt->num = starting_list[i];
		list->nodes[nxt->num] = nxt;
		if (i < list_size - 1) {
			ll_e * nxt2 = malloc(sizeof(ll_e));
			nxt->next = nxt2;
			nxt2-> prev = nxt;
			nxt = nxt2;
		}
		else {
			nxt->next = NULL;
		}
	}
	list->tail = nxt;
	return list;
}

/** Move a count of items from the start of a dll to the end */
void move_to_end(dll_t* list, int num) {
	ll_e* ptr = list->head;
	ll_e* tail = list->tail;
	for(int i =0; i < num; i++) {
		list->head = ptr->next;
		ptr->next->prev = NULL;
		ptr->next = NULL;
		ptr->prev = list->tail;
		ptr->prev->next = ptr;
		list->tail = ptr;
		ptr = list->head;
	}
}

/** Move 3 nodes from the end of a dll to after a given destination number */
void move_3_nodes(dll_t * list, int dest) {
	ll_e * ptr = list->nodes[dest];
	ll_e * after = ptr->next;
	ll_e * cup1 = list->tail->prev->prev;
	ll_e * cup3 = list->tail;
	ptr->next = cup1;
	list->tail = cup1->prev;
	list->tail->next = NULL;
	cup1->prev = ptr;
	cup3->next = after;
}

/** print a dll */
void print_list(dll_t* list) {
	ll_e * ptr = list->head;
	do {
		printf("%d ", ptr->num);
		ptr = ptr->next;
	} while (ptr != NULL);
	printf("\n");
}

/** Free a dll */
void free_list(dll_t* list) {
	ll_e * ptr = list->head;
	free(list->nodes);
	do {
		ll_e * nxt = ptr->next;
		free(ptr);
		ptr = nxt;
	} while (ptr != NULL);
	free(list);
}

/** Print the results as needed by part 2 */ 
void print_part2_results(dll_t * list) {
	ll_e * ptr = list->nodes[1];
	long int a;
	long int b;
	if (ptr == list->tail) {
		a = list->head->num; b = list->head->next->num;
	}
	else {
		ptr = ptr->next;
		a = ptr->num;
		if (ptr == list->tail) {
			b = list->head->num;
		}
		else {
			b = ptr->next->num;
		}
	}
	printf("%ld %ld %ld\n",a,b,a*b);
}

/** Run the challenge */
int run(int* starting_list, int start_list_size, int steps, int part) {
	dll_t * list = create_list(starting_list, start_list_size);
	move_to_end(list,4);
	for (int i = 0; i < steps; i++) {
		int dest = list->tail->prev->prev->prev->num;
		int allowed;
	        do {
			allowed = 1;
			dest--;
			if (dest <= 0) dest = start_list_size;
			allowed &= dest != list->tail->num;
			allowed &= dest != list->tail->prev->num;
			allowed &= dest != list->tail->prev->prev->num;
		} while (!allowed);
		move_3_nodes(list,dest);
		move_to_end(list,4);
	}
	if (part == 1) print_list(list);
	else if (part == 2) print_part2_results(list);
	free_list(list);
	return 0;

}

int main(int argc, char * argv[]) {
	//Parse input
	const int LENGTH = 9; //expected input array length
	if (argc < 2) {
		printf("Please provide input argument of length %d.\n", LENGTH);
		return -1;
	}
	int * init = malloc(1000000 * sizeof(int));
	for(int i = 0; i < LENGTH; i++) {
		int in = argv[1][i] - 48;
		if (in < 1 || in > 9) {
			printf("Invalid input %c\n", argv[1][i]);
			return -2;
		}
		init[i] = in;
	}
	for(int i = LENGTH; i < 1000000; i++) init[i] = i+1;

	// And run!
	run(init, LENGTH, 100, 1);
	run(init, 1000000, 10000000, 2);
	free(init);
}


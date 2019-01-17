#include <stdlib.h>
#include <stdio.h>
#include "queue.h"


struct queue new_queue() {
	struct queue q;
	q.first_node = 0;
	q.last_node = 0;
	q.number_of_elements = 0;
	return q;
}

void delete_queue(struct queue * queue) {
	struct node * next_node;
	struct node * working_node;
	working_node = (*queue).first_node;
	while (working_node != 0) {
		next_node =  (*working_node).next;
		free(working_node);
		working_node = next_node;
	}
	return;
}

void add_queue_element(void * queue, void * data) {
	struct node tmp_node;
	tmp_node.data = data;
	tmp_node.next = 0;
	struct node * new_node = malloc(sizeof(tmp_node));
	*new_node = tmp_node;
	struct queue * q = (struct queue *) queue;
	if((*q).last_node == 0){
		(*q).first_node = new_node;
	}
	else{
		struct node * last_node;
		last_node = (*q).last_node;
		((*last_node).next) = new_node;
	}
	(*q).number_of_elements++;
	(*q).last_node = new_node;
	return;
}

int get_queue_length(struct queue queue) {
	return queue.number_of_elements;
}

void * pop_first_element_in_queue(void * queue) {
	struct node first_node;
	first_node = *((struct node *)(((* (struct queue *) queue).first_node)));
	(* (struct queue *) queue).first_node = first_node.next;
	(* (struct queue *) queue).number_of_elements--;
	return first_node.data;
}

void * get_first_element_in_queue_data(void * queue) {
	struct node first_node;
	first_node = * ((struct node *) (* (struct queue *) queue).first_node);
	return first_node.data;
}

struct node get_node_by_adress(void * adress){
	struct node n;
	n = (* (struct node *) adress);
	return n;
}



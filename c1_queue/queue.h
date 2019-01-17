/*
 * queue.h
 *
 *  Created on: 17 בינו׳ 2019
 *      Author: Nir
 */

#ifndef QUEUE_H_
#define QUEUE_H_

struct node {
	void* data;
	void* next;
};

struct queue {
	void* first_node;
	void* last_node;
	int number_of_elements;
};

struct queue new_queue();
void delete_queue(struct queue * queue);
void add_queue_element(void * queue, void * data);
void * pop_first_element_in_queue(void * queue);
void * get_first_element_in_queue_data(void * queue);
struct node get_node_by_adress(void * adress);

#endif /* QUEUE_H_ */

/*
 * list.h
 *
 *  Created on: 17 בינו׳ 2019
 *      Author: Nir
 */

#ifndef LIST_H_
#define LIST_H_

struct element {
	void* data;
	void* next;
	void * previous;
};

struct list {
	void* first_element;
	void* last_element;
	int number_of_elements;
};

struct list new_list();
void delete_list(struct list * list);
void add_list_element(void * list, void * data);
int get_list_length(struct list * list);
struct element * get_first_element_in_list(struct list * list);
struct element * get_last_element_in_list(struct list * list);
struct element * get_next_element(struct element * element);
struct element * get_previous_element(struct element * element);
void * get_element_data(struct element * element);
int get_avarage_of_list(struct list * list);

#endif /* LIST_H_ */

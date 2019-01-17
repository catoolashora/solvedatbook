#include "list.h"
#include <stdlib.h>

struct list new_list() {
	struct list q;
	q.first_element = 0;
	q.last_element = 0;
	q.number_of_elements = 0;
	return q;
}

void delete_list(struct list * list) {
	struct element * next_element;
	struct element * working_element;
	working_element = (*list).first_element;
	while (working_element != 0) {
		next_element =  (*working_element).next;
		free(working_element);
		working_element = next_element;
	}
	return;
}

void add_list_element(void * list, void * data) {
	struct element tmp_element;
	tmp_element.data = data;
	tmp_element.next = 0;
	struct element * new_element = malloc(sizeof(tmp_element));
	*new_element = tmp_element;
	struct list * q = (struct list *) list;
	if((*q).last_element == 0){
		(*q).first_element = new_element;
	}
	else{
		struct element * last_element;
		last_element = (*q).last_element;
		((*last_element).next) = new_element;
	}
	(*q).number_of_elements++;
	(*q).last_element = new_element;
	return;
}

int get_list_length(struct list * list) {
	return (*list).number_of_elements;
}

struct element * get_first_element_in_list(struct list * list){
	return (*list).first_element;
}

struct element * get_last_element_in_list(struct list * list){
	return (*list).last_element;
}

struct element * get_next_element(struct element * element){
	return (*element).next;
}

struct element * get_previous_element(struct element * element){
	return (*element).previous;
}

void * get_element_data(struct element * element){
	return (*element).data;
}

int get_avarage_of_list(struct list * list){
	int noe = (*list).number_of_elements;
	struct element * working_element = (*list).first_element;
	struct element * next_element;
	int sum = 0;
	for(int i = 0; i<noe;i++){
		next_element = (*working_element).next;
		sum += *((int *)get_element_data(working_element));
		working_element = next_element;
	}
	return (int) (sum/noe);
}

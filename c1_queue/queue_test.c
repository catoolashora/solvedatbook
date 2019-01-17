/*
 * main.c
 *
 *  Created on: 17 בינו׳ 2019
 *      Author: Nir
 */

#include <stdio.h>
#include "queue.h"

int queue_test(int argc, char **argv) {
	struct queue q = new_queue();
	int a = 78;
	int b = 122;
	int c = 99;
	add_queue_element(&q, &a);
	add_queue_element(&q, &b);
	add_queue_element(&q, &c);
	int x = * (int *) get_first_element_in_queue_data(&q);
	printf("x: %d\n", x);
	return 0;
}


/*
 * main.c
 *
 *  Created on: 17 בינו׳ 2019
 *      Author: Nir
 */

#include <stdio.h>
#include "list.h"

int main(int argc, char **argv) {
	struct list l = new_list();
	int a = 1;
	int b = 2;
	int c = 3;
	add_list_element(&l, &a);
	add_list_element(&l, &b);
	add_list_element(&l, &c);
	int x = get_list_length(&l);
	printf("x: %d\n", x);
	return 0;
}


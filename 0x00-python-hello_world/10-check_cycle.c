#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/*
 * check_cycle - A function that checks if a singly linked list has a cycl
 * @list: pointer to list to check
 * Return: 1 if it is correct, otherwith 0
 */

int check_cycle(listint_t *list)
{
	listint_t *i = list, *j = list;

	while (j && j->next)
	{
		i = i->next;
		j = j->next->next;
		if (i == j)
			return (1);
	}
	return (0);
}

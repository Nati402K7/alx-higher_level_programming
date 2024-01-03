#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - A function that inserts a number into a sorted singly linked
 * @head: address of head pointer
 * @number: number to insert
 * Return: input node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i = *head, *j = malloc(sizeof(listint_t));

	if (!j)
		return (NULL);

	j->n = number;
	j->next = NULL;

	if (!i || j->n < i->n)
	{
		j->next = i;
		return (*head = j);
	}

	while (i)
	{
		if (!i->next || j->n < i->next->n)
		{
			j->next = i->next;
			i->next = j;
			return (i);
		}
		i = i->next;
	}
	return (NULL);
}

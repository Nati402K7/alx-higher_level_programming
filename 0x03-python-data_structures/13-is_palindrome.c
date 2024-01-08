#include "lists.h"
#include <stddef.h>

int checker(listint_t **head, listint_t *i);

/**
 * is_palindrom - A function that checks if a singly linked list is palindrome
 * @head: input list
 * Return: 1 success, othetwise 0
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (checker(head, *head));
}

/**
 * checker - A function that checkes if is palindrome
 * @head: input list
 * @i: input list
 * Return: 1 succeess, otherwith 0
 */

int checker(listint_t **head, listint_t *i)
{
	if (i == NULL)
		return (1);
	if (checker(head, i->next) && (*head)->n == i->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

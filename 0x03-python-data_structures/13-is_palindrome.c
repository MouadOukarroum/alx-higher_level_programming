#include "lists.h"

/**
 * is_palindrome - recursive palind or not
 * @head: head of the list
 * Return: 0 if not a palind, otherwise 1
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - funct to check if a list a plaindrome
 * @head: head list
 * @end: list end
 * Return: 0 if not a plaind, otherwise 1
 */

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

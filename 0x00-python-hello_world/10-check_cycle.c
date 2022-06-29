#include "lists.h"

/**
 * check_cycle - check if a linked list has a loop
 *
 * @list: first node
 *
 * Return: 1: if linked list have a loop
 *         0: if not
 */
int check_cycle(listint_t *list)
{
	listint_t *sHead, *fHead;

	sHead = fHead = list;

	if (list == NULL)
		return (0);

	while (sHead && fHead && fHead->next)
	{
		sHead = sHead->next;
		fHead = fHead->next->next;

		if (sHead == fHead)
		{
			return (1);
		}
	}

	return (0);
}

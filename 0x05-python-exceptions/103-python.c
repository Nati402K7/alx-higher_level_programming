#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

/**
 * print_python_float - A function that prints info about python float
 * @p: input
 */

void print_python_float(pyObject *p)
{
	double i;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_nmae, "float"))
	{
		printf(" [ERROR} Invalid Float Object\n");
		return;
	}
	i = ((PyFloatObject *)p)->ob_fval;
	printf(" value: %s\n",
			PyOS_double_to_string(i, 'r', 0, Py_DTSF_ADD_DOT_0,
				NULL));
}

/**
 * print_python_bytes - A function that prints info about python bytes
 * @p: input
 */

void print_python_bytes(PyObject *p)
{
	size_t i, j, k;
	char *n;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	k = ((PyVarObject *)p)->ob_size;
	n = ((PyBytesObject *)p)->ob_sval;
	j = k + 1 > 10 ? 10 : k + 1;
	printf(" size: %lu\n", k);
	printf(" trying string: %s\n", n);
	printf(" first %lu bytes: ", j);
	for (i = 0; i < j; i++)
		printf("%02hhx%s", n[i], i + 1 < j ? " " : "");
	printf("\n");
}

/**
 * print_python_list - A function that prints info about python lists
 * @p: input
 */

void print_python_list(PyObject *p)
{
	int i;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf(" [ERROR] Invalid list Object\n");
		return;
	}
	printf("[*] Size of the Python List = %lu\n",
			((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		printf("Element %d: %s\n", i, ((PyListObject *)p)->
				ob_item[i]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name,
					"bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
		else if (!strcmp(((PyListObject *)p)->
					ob_item[i]->ob_type->tp_name, "float"))
			print_python_float(((PyListObject *)p)->ob_item[i]);
	}
}

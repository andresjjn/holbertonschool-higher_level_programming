#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Function that prints some basic info about Python lists.
 * @Pyobject: Object to know infi
 * Return: -
 */
void print_python_list_info(PyObject *p)
{
        int j = 0;
        PyObject *ptr;

        printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
        while(j < PyList_Size(p))
	{
		ptr = PyList_GET_ITEM(p, j);
		printf("Element %d: %s\n", j, ptr->ob_type->tp_name);
                j++;
	}
}

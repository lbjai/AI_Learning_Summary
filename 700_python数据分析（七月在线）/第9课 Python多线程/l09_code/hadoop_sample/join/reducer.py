#! /usr/bin/python

import sys

dept = {}
salary = {}
for line in sys.stdin:
    line = line.strip()
    emp_id, emp_name, emp_dept_id, emp_salary, dept_id, dept_name = line.split(',')
    if emp_id == '':
        if dept_id not in dept:
            dept[dept_id] = dept_name
    else:
        if emp_dept_id not in salary:
            salary[emp_dept_id] = 0
        salary[emp_dept_id] += int(emp_salary)
for k, v in salary.items():
    print('Total salary of %s department is %d' % (dept[k], v))

#! /usr/bin/python

import sys

for line in sys.stdin:
    dept_id = ''
    dept_name = ''
    emp_id = ''
    emp_name = ''
    emp_dept_id = ''
    emp_salary = ''
    line = line.strip()
    splits = line.split(',')
    if len(splits) == 4: # salary.csv
        emp_id = splits[0]
        emp_name = splits[1]
        emp_dept_id = splits[2]
        emp_salary = splits[3]
    else: # dept.csv
        dept_id = splits[0]
        dept_name = splits[1]
    print('%s,%s,%s,%s,%s,%s' % (emp_id, emp_name, emp_dept_id, emp_salary, dept_id, dept_name))


#!/user/bin/env python3
# -*- coding: utf-8 -*-


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

company = Company(['tom','non','jane'])
for em in company:
    print(em)
from odoo import api, models, fields
import random

class person_test(models.Model):
    _name = 'school.persontest'
    _description = 'Person test'
    _inherit = ['school.person']
    
    test1 = fields.Char(compute = '_get_test1', store=True)
    @api.depends('name')
    def _get_test1(self):
        self.test1 = f'{random.randint(0,10000)}'


    from odoo.exceptions import ValidationError
    test_constrains = fields.Char()
    @api.constrains('test_constrains')
    def length_large(self):
        if len(self.test_constrains) >=5:
            print('heloo')
            # raise Exception("Test Exception")


    test_sql_constraints1 = fields.Char()
    test_sql_constraints2 = fields.Char()
    _sql_constraints = [
        ('test_check_1', 'CHECK(LENGTH(test_sql_constraints1) <= 5)', 'test_sql_constaints1 phải nhỏ hơn 5 kí tự'),
        ('test_check_2', 'CHECK(LENGTH(test_sql_constraints2) <= 10)', 'test_sql_constraints2 phải nhỏ hơn 10 kí tự')
    ]
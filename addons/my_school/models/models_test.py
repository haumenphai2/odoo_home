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
        if self.test_constrains and len(self.test_constrains) >=5:
            print('heloo')
            # raise Exception("Test Exception")
            

    test_sql_constraints1 = fields.Char()
    test_sql_constraints2 = fields.Char()
    _sql_constraints = [
        ('test_check_1', 'CHECK(LENGTH(test_sql_constraints1) <= 5)', 'test_sql_constaints1 phải nhỏ hơn 5 kí tự'),
        ('test_check_2', 'CHECK(LENGTH(test_sql_constraints2) <= 10)', 'test_sql_constraints2 phải nhỏ hơn 10 kí tự')
    ]
    
    
    
    int_field = fields.Integer()
    @api.onchange('int_field')
    def int_change(self):
        if self.int_field >= 10:
            return {
                'warning': {
                    'title': "return of @api.constraint - Title",
                    'message': "Int field không được lớn hơn 10",
                },
            }
            
    
    
    
    user_id = fields.Many2one('res.users', default=lambda self:self.env.user)
    
    
    
    

class LaoCong(models.Model):
    _name = 'school.laocong'
    _description = 'test thừa kế ủy thác'
    _inherits = {'school.person': 'person_id'}
    
    person_id = fields.Many2one('school.person')          
    

class BuoiHoc(models.Model):
    _name = 'school.test.buoihoc'
    _description = 'test buổi học'
    
    start_date = fields.Datetime(default='2021-01-20 20:20:20')
    end_date = fields.Datetime(default='2021-02-20 20:20:20')
    int_test = fields.Integer()
    name2 = fields.Char(default = 'name2 default')
    html_field = fields.Html()      
            
            
class test_wizards(models.TransientModel):
    _name = 'school.test.wizards'
    _description = "Test wizards"
    buoi_hoc_id = fields.Many2one('school.test.buoihoc')
    laocong_ids = fields.Many2many('school.laocong')       
    
    def subscribe(self):
        for o in self.laocong_ids:
            o.laocong_ids |= self.buoi_hoc_id
        return {}       
            
            
            
            
            
            
            
            
            
            
            
            
            
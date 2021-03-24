from odoo import models, fields, api

from datetime import datetime

class Person(models.Model):
    _name = 'school.person'
    _description = 'person'

    name = fields.Char(required=True, string='Họ tên')
    birth_day = fields.Date(required=True, string="Ngày sinh")
    address = fields.Char(required=True, string="Địa chỉ")
    gioi_tinh = fields.Selection([
        ('Nam_', 'Nam'),
        ('Nu_', 'Nữ')
    ],required=True, string='Giới tính', default='Nam_')
    
    age = fields.Integer(readonly=True, string='Tuổi', compute='_compute_age')
    
    @api.depends('birth_day')
    def _compute_age(self):
        print(self)
        now_year = datetime.now().year
        for o in self:
            o.age = now_year - o.birth_day.year
from odoo import models, fields, api


class Person(models.Model):
    _name = 'school.person'
    _description = 'person'

    name = fields.Char(required=True, string='Họ tên')
    age = fields.Integer(required=True, string='Tuổi')
    birth_day = fields.Date(required=True, string="Ngày sinh")
    address = fields.Char(required=True, string="Địa chỉ")
    gioi_tinh = fields.Selection([
        ('Nam_', 'Nam'),
        ('Nữ_', 'Nữ')
    ],required=True, string='Giới tính', default='Nam_')
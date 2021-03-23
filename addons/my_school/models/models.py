# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GiaoVien(models.Model):
    _name = 'school.giaovien'
    _description = 'giáo viên'
    _inherit = 'school.person'

    luong = fields.Float(string='Lương')
    chu_nhiem_lop = fields.Many2one('school.class', string='Chủ nhiệm lớp')


class Student(models.Model):
    _name = 'school.student'
    _description = 'Học sinh'
    _inherit = 'school.person'

    hoc_sinh_lop = fields.Many2one('school.class')


class Class(models.Model):
    _name = 'school.class'
    _description = 'quản lý trường học'

    name = fields.Char(required=True, string='Tên lớp')
    phong_hoc = fields.Char(string="Số phòng")
    hoc_sinh_trong_lop = fields.One2many('school.student', 'hoc_sinh_lop', string='Học sinh của lớp')






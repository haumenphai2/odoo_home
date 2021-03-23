# -*- coding: utf-8 -*-
# from odoo import http


# class MySchool(http.Controller):
#     @http.route('/my_school/my_school/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_school/my_school/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_school.listing', {
#             'root': '/my_school/my_school',
#             'objects': http.request.env['my_school.my_school'].search([]),
#         })

#     @http.route('/my_school/my_school/objects/<model("my_school.my_school"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_school.object', {
#             'object': obj
#         })

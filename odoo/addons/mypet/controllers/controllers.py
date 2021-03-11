# -*- coding: utf-8 -*-
# from odoo import http


# class Mypet(http.Controller):
#     @http.route('/mypet/mypet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mypet/mypet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mypet.listing', {
#             'root': '/mypet/mypet',
#             'objects': http.request.env['mypet.mypet'].search([]),
#         })

#     @http.route('/mypet/mypet/objects/<model("mypet.mypet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mypet.object', {
#             'object': obj
#         })

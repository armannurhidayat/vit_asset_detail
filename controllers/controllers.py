# -*- coding: utf-8 -*-
from odoo import http

# class VitAssetDetail(http.Controller):
#     @http.route('/vit_asset_detail/vit_asset_detail/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_asset_detail/vit_asset_detail/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_asset_detail.listing', {
#             'root': '/vit_asset_detail/vit_asset_detail',
#             'objects': http.request.env['vit_asset_detail.vit_asset_detail'].search([]),
#         })

#     @http.route('/vit_asset_detail/vit_asset_detail/objects/<model("vit_asset_detail.vit_asset_detail"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_asset_detail.object', {
#             'object': obj
#         })
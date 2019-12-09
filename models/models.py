# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
import logging
_logger = logging.getLogger(__name__)
# from datetime import datetime
import datetime

class Asset(models.Model):
	_name = 'account.asset.asset'
	_inherit = ['account.asset.asset','mail.thread']

	pengadaan = fields.Selection(
		selection=[
			('PO', 'PO'),
			('Pembelian Langsung', 'Pembelian Langsung'),
		],
		string='Metode Pengadaan',
	)
	sertifikat = fields.Selection(
		selection=[
			('SHM', 'SHM'),
			('HGB', 'HGB'),
		],
		string='Jenis Sertifikat',
	)
	processor = fields.Char(
		string='Processor',
		size=64,
		required=False,
	)
	harddisk = fields.Char(
		string='Harddisk',
	)
	memory = fields.Char(
		string='Memory',
	)
	budget = fields.Char(
		string='Budget',
	)
	kd_wilayah = fields.Char(
		string='Kode Wilayah',
	)
	no_polisi = fields.Char(
		string='No. Polisi',
	)
	tgl_pajak = fields.Date(
		string='Tanggal Pajak dan STNK',
		default=lambda self:time.strftime("%Y-%m-%d"),
	)
	tgl_asuransi = fields.Date(
		string='Tanggal Asuransi',
	)
	tanah = fields.Integer(
		string='Luas Tanah',
	)
	bangunan = fields.Integer(
		string='Luas Bangunan',
	)
	no_sertifikat = fields.Char(
		string='Nomor Sertifikat',
	)
	tgl_sertifikat = fields.Date(
		string='Tanggal Sertifikat',
		default=lambda self:time.strftime("%Y-%m-%d"),
	)
	alamat = fields.Text(
		string='Alamat',
	)
	tgl_jp_pajak = fields.Date(
		string='Tanggal Jatuh Tempo Pajak',
		default=lambda self:time.strftime("%Y-%m-%d"),
	)
	tgl_jp_asuransi = fields.Date(
		string='Tanggal Jatuh Tempo Asuransi',
		default=lambda self:time.strftime("%Y-%m-%d"),
	)


	@api.model
	def create(self, vals):
		# supaya auto subscribe channel asset
		res = super(Asset, self).create(vals)

		cids = self.env['mail.channel'].search([('name','ilike','assets')])
		res.message_subscribe(
			channel_ids = cids.ids
		)
		return res


	def cek_jatuh_tempo(self):
		# date_jt = hari ini + 10 hari
		date_jt	= datetime.datetime.now() + datetime.timedelta(days=10)
		pajak	= self.env['account.asset.asset'].search([('tgl_jp_pajak', '<=', date_jt)])
		asuransi= self.env['account.asset.asset'].search([('tgl_jp_asuransi', '<=', date_jt)])
		
		for pj in pajak:
			days_pajak = pj.tgl_jp_pajak - datetime.date.today()
			pj.message_post(body="Asset Jatuh Tempo Pajak "+ str(days_pajak)[0:8],
							  message_type='comment', subtype='mail.mt_comment')

		for asu in asuransi:
			days_asuransi = asu.tgl_jp_asuransi - datetime.date.today()
			asu.message_post(body="Asset Jatuh Tempo Asuransi "+ str(days_asuransi)[0:8],
							  message_type='comment', subtype='mail.mt_comment')

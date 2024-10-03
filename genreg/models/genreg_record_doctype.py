from odoo import models, fields

class GenRegRecordDocType(models.Model):
    _name = 'genreg.record.doctype'
    _description = 'DocType Configuration'

    name = fields.Char(string='Document Type', required=True)
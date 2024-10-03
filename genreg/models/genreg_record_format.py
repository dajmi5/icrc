from odoo import models, fields

#Type in Notes
class GenRegRecordFormat(models.Model):
    _name = 'genreg.record.format'
    _description = 'Format Configuration'

    name = fields.Char(string='Format', required=True)
    code = fields.Char(string='Code', required=True)
from odoo import models, fields

class GenRegConfidentiality(models.Model):
    _name = 'genreg.confidentiality'
    _description = 'Confidentiality Level'

    name = fields.Char(string='Confidentiality Level', required=True)
    code = fields.Char(string='Code', required=True)
    default = fields.Boolean(string='Is Default')

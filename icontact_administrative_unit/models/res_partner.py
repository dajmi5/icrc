from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    administrative_unit_id = fields.Many2one(
        comodel_name='administrative.unit',
        string="Administrative unit"
    )
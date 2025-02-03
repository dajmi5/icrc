from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    military_rank_id = fields.Many2one(
        comodel_name='military.rank',
        string="Military rank"
    )
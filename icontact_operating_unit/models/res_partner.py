# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _default_operating_unit_ids(self):
        if self.parent_id and self.parent_id.operating_unit_ids:
            return [(6, 0, self.parent_id.operating_unit_ids.ids)]
        default_ou = self.env.user.default_operating_unit_id
        if default_ou:
            return [
                (6,0,default_ou.ids)
            ]


    operating_unit_ids = fields.Many2many(
        "operating.unit",
        "res_partner_operating_unit_rel",
        string="Operating Units",
        default=_default_operating_unit_ids,
    )
from odoo import _, api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_icontact_military_rank = fields.Boolean(string="Military ranking management")
    module_icontact_administrative_unit = fields.Boolean(string="Administrative units management")
    module_icontact_adminlevel = fields.Boolean(string="Administrative levels")
    module_icontact_operating_unit = fields.Boolean(string="Operating units on partner")
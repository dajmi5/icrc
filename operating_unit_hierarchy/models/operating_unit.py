# Copyright 2015-TODAY ForgeFlow
# - Jordi Ballester Alomar
# Copyright 2015-TODAY Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models


class OperatingUnit(models.Model):
    _inherit = "operating.unit"
    # _parent_name = 'parent_id'
    # _parent_store = True

    parent_id = fields.Many2one("operating.unit", "Parent")
    child_ids =fields.One2many("operating.unit","parent_id","Childs")
    color = fields.Integer(string='Color',default=6)

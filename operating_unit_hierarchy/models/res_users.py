# Copyright 2015-TODAY ForgeFlow
# - Jordi Ballester Alomar
# Copyright 2015-TODAY Serpent Consulting Services Pvt. Ltd. - Sudhir Arya
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResUsers(models.Model):

    _inherit = "res.users"

    #@api.constrains('operating_unit_ids')
    def _check_operating_hierarchical_unit(self):
        for user in self:
            # Collect all the business units assigned to the user
            operating_units = user.operating_unit_ids

            if not operating_units:
                continue

            # Search for any business units in the hierarchy of the assigned ones
            overlapping_units = self.env['operating.unit'].search([
                '|',  # Match either parent or child relationships
                ('id', 'child_of', operating_units),  # Business units in the subtree of assigned units
                ('id', 'parent_of', operating_units)  # Business units that are parents of assigned units
            ])

            # Check if there is any overlap
            if len(overlapping_units) > len(user.operating_unit_ids):
                raise ValidationError(
                    "You cannot assign operating Units that are in the same hierarchical line (parent/child). "
                    "Please review the selected Business Units."
                )


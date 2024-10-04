import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class GenRegRegister(models.Model):
    _name = 'genreg.register'
    _description = 'General Register'

    name = fields.Char(string='Name')
    sequence = fields.Many2one('ir.sequence', string='Sequence', required=True)

    # access rights
    sec_editor_group_ids = fields.Many2many(
        'res.groups',
        'genreg_register_editor_groups_rel',  # Relation table
        'register_id',  # Column for register id
        'group_id',  # Column for group id
        string="Editor Groups"
    )

    sec_manager_group_ids = fields.Many2many(
        'res.groups',
        'genreg_register_manager_groups_rel',  # Relation table
        'register_id',  # Column for register id
        'group_id',  # Column for group id
        string="Manager Groups"
    )

    # to show records on the form
    record_ids = fields.One2many('genreg.record', 'doc_register_id', string='Records')

    can_edit = fields.Boolean(
        string="Can Edit",
        compute="_compute_can_edit",
        store=False
    )

    @api.depends('sec_manager_group_ids')
    def _compute_can_edit(self):
        for record in self:
            # Check if user belongs to manager group(s)
            is_manager = self.env.user.has_group('genreg.group_genreg_user_manager') or \
                         any(group.id in self.env.user.groups_id.ids for group in record.sec_manager_group_ids)
            record.can_edit = is_manager

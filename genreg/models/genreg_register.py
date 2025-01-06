import ast
import logging
from odoo import models, fields, api, _

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
    @api.model
    def get_action(self,action_name):
        _logger.info(f'Action called: {action_name}')
        return False

    @api.model
    def _get_view(self, view_id=None, view_type='form', **options):
        _logger.info(f'Action called _get_view: {view_id}')
        arch, view = super()._get_view(view_id, view_type, **options)
        # if view_type == 'form':
            # arch = self._view_get_address(arch)
        return arch, view

    def get_last_update_or_default(self):
        self.ensure_one()
        return {
            'status': "ok",
            'name': self.name,
        }

    def action_view_records(self):
        action = self.env['ir.actions.act_window'].with_context({'active_id': self.id})._for_xml_id(
            'genreg.action_genreg_register_records')
        action['display_name'] = _("%(name)s", name=self.name)
        context = action['context'].replace('active_id', str(self.id))
        context = ast.literal_eval(context)
        action['context'] = context
        return action

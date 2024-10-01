from odoo import api, fields, models


class HelpdeskCategory(models.Model):
    _inherit = "helpdesk.ticket.category"

    team_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.team',
        string='Teams',
        relation='helpdesk_ticket_team_category_rel',
        column1='categ_id', column2='team_id'
    )
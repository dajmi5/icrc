from odoo import api, fields, models

class HelpdeskTeam(models.Model):
    _inherit = "helpdesk.ticket.team"

    category_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.category',
        string='Categories',
        relation='helpdesk_ticket_team_category_rel',
        column1='team_id', column2='categ_id'
    )
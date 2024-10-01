from odoo import api, fields, models

class HelpdeskTicket(models.Model):

    _inherit = "helpdesk.ticket"

    team_categ_ids = fields.Many2many(related='team_id.category_ids')


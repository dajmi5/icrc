from odoo import api, fields, models

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    state = fields.Selection(
        related='stage_id.state',
        store=True, readonly=True
    )
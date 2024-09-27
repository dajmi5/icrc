from odoo import api, fields, models


class HelpdeskTicketStage(models.Model):
    _inherit = "helpdesk.ticket.stage"

    @api.model
    def _get_stage_states(self):
        return [
            ('draft', 'Draft'),
            ("open", "In Progress"),
            #("pending", "Pending Approval"),
            ("done", "Done"),
            ("cancel", "Cancelled"),
        ]

    state = fields.Selection(
        selection="_get_stage_states"
    )
from odoo import api, fields, models


class HelpdeskTicketTSageTransition(models.Model):
    _name = 'helpdesk.ticket.stage.transition'

    stage_from_id = fields.Many2one(
        comodel_name='helpdesk.ticket.stage',
        string="Stage from", required=1
    )
    stage_to_id = fields.Many2one(
        comodel_name='helpdesk.ticket.stage',
        string="Stage to", required=1
    )


class HelpdeskTicketStage(models.Model):
    _inherit = "helpdesk.ticket.stage"

    @api.model
    def _get_stage_states(self):
        return [
            ('draft', 'Draft'),
            ("open", "In Progress"),
            ("pending", "Pending Approval"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ]

    state = fields.Selection(
        selection="_get_stage_states"
    )
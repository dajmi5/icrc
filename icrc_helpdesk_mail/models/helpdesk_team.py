from odoo import api, fields, models
from odoo.tools.safe_eval import safe_eval


class HelpdeskTeam(models.Model):
    _inherit = "helpdesk.ticket.team"

    default_mail_channel_id = fields.Many2one(
        comodel_name='mail.channel',
        string="Default mail channel",
        help="general discussion and all unclassified emails"
    )
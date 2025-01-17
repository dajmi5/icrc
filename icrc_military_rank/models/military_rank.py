from odoo import models, fields, api


class MilitaryRank(models.Model):
    _name = "military.rank"
    _description = "Military Ranks"
    _order = "sequence asc"
    _avoid_quick_create = True

    active = fields.Boolean("Active", default=True)
    sequence = fields.Integer(string="Sequence", required=True)
    name = fields.Char(string="Name",required=True)

    code = fields.Char(string="Code")
    description = fields.Text("Description")
    parent_id = fields.Many2one(
        "military.rank",
        string="Parent Rank",
    )


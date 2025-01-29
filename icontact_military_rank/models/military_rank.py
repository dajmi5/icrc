from odoo import models, fields, api


class MilitaryRank(models.Model):
    _name = "military.rank"
    _description = "Military Ranks"
    #_order = "sequence asc"
    _avoid_quick_create = True
    #_parent_name = "parent_id"
    #_parent_store = True
    # _rec_names_search = ['complete_name', 'barcode']

    active = fields.Boolean("Active", default=True)
    sequence = fields.Integer(string="Sequence", required=True, default=16)
    rank_type = fields.Selection(
        selection=[
            ('general', 'General/Flag/Air Officer'),
            ('senior', 'Senior officer'),
            ('junior', 'Junior officer'),
            ('nco', 'Non-Commisioned officers'),
            ('enlisted', 'Enlisted ranks')
        ], string="Rank seniority"
    )
    forces_type = fields.Selection(
        selection=[
            ('army', 'Army'),
            ('navy', 'Navy / Coast Guard'),
            ('airforce', 'Air forces'),
            ('other', 'Other'),
        ], string="Army forces type"
    )
    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country'
    )
    country_group_id = fields.Many2one(
        comodel_name='res.country.group',
        string="Country group",
        help="For example: NATO"
    )
    name = fields.Char(string="Name",required=True)
    code = fields.Char(string="Code")  # might be a selection!! nato codes OF/OR 1-10
    description = fields.Text("Description")
    parent_id = fields.Many2one(
        comodel_name="military.rank",
        string="Parent Rank",
    )
    child_ids = fields.One2many(
        comodel_name='military.rank',
        inverse_name='parent_id',
        string="Subordinate"
    )
    partner_ids = fields.One2many(
        comodel_name="res.partner",
        inverse_name='military_rank_id',
        string="Staff"
    )


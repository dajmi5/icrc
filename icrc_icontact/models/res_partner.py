from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _get_rating_sel(self):
        return [
            ("0", "0"),
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("10", "10"),
        ]

    # override original string in selection?
    company_type = fields.Selection(
        selection=[
            ('person', 'Individual'),
            ('company', 'Stakeholder'),
        ],
    )
    power_influence = fields.Selection(
        selection=_get_rating_sel,
        string='Power & Influence',
        help='Level of power and influence (1-10)'
    )
    attitude_icrc = fields.Selection(
        selection=_get_rating_sel,
        string='Attitude towards the ICRC',
        help='Attitude towards the ICRC (1-10)'
    )
    level_of_interest = fields.Selection(
        selection=[
            ('positive', 'Positive'),
            ('medium', 'Medium'),
            ('negative', 'Negative')
        ],
        string='Level of Interest',
        help='Level of interest in the organization',
        default='medium'
    )
    contact_type = fields.Selection(
        selection=[
            ('armed', 'Armed and Security Forces'),
            ('civil', 'Civil society'),
            ('diplomatic', 'Diplomatic corps/Donors'),
            ('ngo', 'IO/NGO'),
        ],
        string='Stakeholder Type'
    )
    icrc_focal_point = fields.Char(
        string='ICRC Focal Point/Department',
        help="The ICRC focal point or department"
    )
    land_line = fields.Char(
        string='Land Line',
        help="Landline contact number")
    bio_url = fields.Char(
        string='Bio',
        help="Link to the person's bio"
    )
    social_media_1 = fields.Char(string='Social Media 1', help="Link to the first social media profile")
    social_media_2 = fields.Char(string='Social Media 2', help="Link to the second social media profile")
    social_media_3 = fields.Char(string='Social Media 3', help="Link to the third social media profile")
    email_private = fields.Char(string='Email private',)

    report_to_id = fields.Many2one(
        comodel_name="res.partner",
        string="Report to"
    )
    report_to_child_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='report_to_id',
        string="Reporting to"
    )

    level_prot_dialog = fields.Selection(
        selection=[
            ('none', 'No protection discussion started'),
            ('basic', 'Basic PROT dissemination conducted'),
            ('depth', 'In depth PROT discussion conducted'),
            ('signed', 'PROT representation conducted (written or oral)')
        ],
        string="Level of Prot Dialogue"
    )
    recorded_prot6 = fields.Char("Recorded in Prot6", help="Link to the Prot6")

    #Moved to military_rank module
    # military_rank = fields.Many2one("military.rank","Rank")
    #
    def button_reporting_hierarchy_view(self):
        view = self.env.ref('icrc_icontact.view_stakeholder_hierarchy')
        return {
            'type': 'ir.actions.act_window',
            'name': 'Hierarchy',
            'view_mode': 'hierarchy',
            'view_id': view.id,
            'res_model': 'res.partner',
            'domain': [("id","=",self.id)],
            'context': dict(self.env.context),
            'target': 'current',
        }

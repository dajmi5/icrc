from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _get_rating_sel(self):
        return [
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5"),
            (6, "6"),
            (7, "7"),
            (8, "8"),
            (9, "9"),
            (10, "10"),
        ]
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

    icrc_focal_point = fields.Char(string='ICRC Focal Point/Department', help="The ICRC focal point or department")
    land_line = fields.Char(string='Land Line', help="Landline contact number")
    bio_url = fields.Char(string='Bio', help="Link to the person's bio")
    social_media_1 = fields.Char(string='Social Media 1', help="Link to the first social media profile")
    social_media_2 = fields.Char(string='Social Media 2', help="Link to the second social media profile")
    social_media_3 = fields.Char(string='Social Media 3', help="Link to the third social media profile")
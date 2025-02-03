from odoo import fields, models, api


class AdminLevel(models.AbstractModel):
    _name = 'admin.level'

    code = fields.Char("Code")
    name = fields.Char(required=True)
    country_id = fields.Many2one(
        comodel_name='res.country'
    )
    latitude = fields.Char(string="Latitude")
    longitude = fields.Char(string="Longitude")


class Adminlevel01(models.Model):
    _inherit = 'admin.level'
    _name = 'admin.level.01'

    country_id = fields.Many2one(required=True)
    child_2_ids = fields.One2many(
        comodel_name='admin.level.02',
        inverse_name='lvl_1_id'
    )
    child_3_ids = fields.One2many(
        comodel_name='admin.level.03',
        inverse_name='lvl_1_id'
    )
    locality_ids = fields.One2many(
        comodel_name='admin.locality',
        inverse_name='lvl_1_id'
    )


class Adminlevel02(models.Model):
    _inherit = 'admin.level'
    _name = 'admin.level.02'

    country_id = fields.Many2one(
        related="lvl_1_id.country_id",
        readonly=1
    )
    lvl_1_id = fields.Many2one(
        comodel_name="admin.level.01",
        string="Lvl 1",
        required=True
    )
    child_3_ids = fields.One2many(
        comodel_name='admin.level.03',
        inverse_name='lvl_2_id'
    )
    locality_ids = fields.One2many(
        comodel_name='admin.locality',
        inverse_name='lvl_2_id'
    )


class Adminlevel03(models.Model):
    _inherit = 'admin.level'
    _name = 'admin.level.03'

    lvl_2_id = fields.Many2one(
        comodel_name="admin.level.02",
        string="Lvl 2",
        required=True
    )
    lvl_1_id = fields.Many2one(
        comodel_name="admin.level.01",
        related='lvl_2_id.lvl_1_id',
        string="Lvl 1",
        readonly=1
    )
    country_id = fields.Many2one(
        related="lvl_2_id.lvl_1_id.country_id",
        readonly=1
    )
    locality_ids = fields.One2many(
        comodel_name='admin.locality',
        inverse_name='lvl_3_id'
    )


class AdminLocality(models.Model):
    _inherit = 'admin.level'
    _name = 'admin.locality'

    local_name = fields.Char("Local name")
    lvl_1_id = fields.Many2one(
        comodel_name="admin.level.01",
        string="Lvl 1",
        #required=True
    )
    lvl_2_id = fields.Many2one(
        comodel_name="admin.level.02",
        string="Lvl 2",
        #required=True
    )
    lvl_3_id = fields.Many2one(
        comodel_name="admin.level.03",
        string="Lvl 3",
        #required=True
    )
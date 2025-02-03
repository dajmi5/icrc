from odoo import fields, models, api

class AdministrativeUnit(models.Model):
    _name = "administrative.unit"
    _description = "ICRC Administrative units"
    #_parent_store = True
    #_parent_name = "parent_id"

    name = fields.Char(
        string="Name", required=True
    )
    code = fields.Char(
        string="Code", required=True
    )

    country_group_id = fields.Many2one(
        comodel_name="res.country.group"
    )
    country_id = fields.Many2one(
        comodel_name="res.country"
    )
    country_state_id = fields.Many2one(
        comodel_name="res.country.state"
    )

    latitude = fields.Char(string="Latitude")
    longitude = fields.Char(string="Longitude")

    parent_id = fields.Many2one(
        comodel_name='administrative.unit',
        string="Parent unit"
    )
    child_ids = fields.One2many(
        comodel_name="administrative.unit",
        inverse_name="parent_id",
        string="Direct suborditnates",
    )
    level = fields.Integer(
        string="Administrative level",
        compute="_compute_admin_level",
        store=True, recursive=True
    )
    level_code = fields.Char(
        string="Full code",
        compute="_compute_admin_level",
        store=True
    )
    partner_ids = fields.One2many(
        comodel_name="res.partner",
        inverse_name='administrative_unit_id',
        string="Contacts"
    )

    @api.depends('parent_id', 'parent_id.level')
    def _compute_admin_level(self):
        for unit in self:
            if not unit.parent_id:
                unit.level = 0
                unit.level_code = unit.code
            else:
                unit.level = unit.parent_id.level + 1
                unit.level_code = '-'.join((unit.parent_id.level_code, unit.code))
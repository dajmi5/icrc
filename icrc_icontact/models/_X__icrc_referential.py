from odoo import fields, models, api


class Adminlevel01(models.Model):
    _name = 'icrc.adminlevel01'

    name = fields.Char()
    country_id = fields.Many2one("res.country")
    latitude = fields.Char(string="Latitude")
    longitude = fields.Char(string="Latitude")
    code = fields.Char("AL1 code")

class Adminlevel02(models.Model):
    _name = 'icrc.adminlevel02'

    name = fields.Char()
    latitude = fields.Char(string="Latitude")
    longitude = fields.Char(string="Latitude")
    code = fields.Char("AL2 code")
    adminlevel1_id = fields.Many2one("icrc.adminlevel01", "Admin level 01")

class Adminlevel03(models.Model):
    _name = 'icrc.adminlevel03'

    name = fields.Char()
    latitude = fields.Char(string="Latitude")
    longitude = fields.Char(string="Latitude")
    code = fields.Char("AL3 code")
    adminlevel2_id = fields.Many2one("icrc.adminlevel02", "Admin level 02")

class Locality(models.Model):
    _name = 'icrc.locality'

    name = fields.Char()
    local_name = fields.Char("Local name")
    latitude = fields.Char(string="Latitude")
    longitude = fields.Char(string="Latitude")
    code = fields.Char("AL4 code")
    adminlevel2_id = fields.Many2one("icrc.adminlevel02", "Admin level 02")
    adminlevel3_id = fields.Many2one("icrc.adminlevel03", "Admin level 03")
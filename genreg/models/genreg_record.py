import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class GenRegRecord(models.Model):
    _name = 'genreg.record'
    _description = 'Register Record'
    _rec_name = 'doc_ref'
    _order = 'create_date desc'

    doc_register_id = fields.Many2one('genreg.register', string="Register", required=True)
    doc_ref = fields.Char(string="Doc Ref", readonly=True)
    doc_date = fields.Date(string="Date", default=fields.Date.today, required=True)
    format_id = fields.Many2one('genreg.record.format', string="Format", required=True)
    format_code = fields.Char(string="F", related="format_id.code", store=True)

    doctype_id = fields.Many2one('genreg.record.doctype', string="Doctype")

    # For Action / To: Define a custom intermediary table
    for_action_ids = fields.Many2many(
        "res.partner",
        "genreg_record_for_action_partners_rel",  # Custom relation table name
        "record_id",  # Column for register id
        "partner_id",  # Column for user id
        string="For Action / To:"
    )

    # For Info / Cc: Define a different custom intermediary table
    for_info_ids = fields.Many2many(
        "res.partner",
        "genreg_record_for_info_partners_rel",  # Another custom relation table name
        "record_id",  # Column for register id
        "partner_id",  # Column for user id
        string="For Info / Cc:"
    )

    confidentiality_id = fields.Many2one("genreg.confidentiality",
                                         string="Confidentiality Level", required=True,
                                         default=lambda self: self._get_default_confidentiality())
    confidentiality_code = fields.Char(string="Level",related="confidentiality_id.code", store=True)

    doc_initiator = fields.Many2one('res.users', string="Initiator", default=lambda self: self.env.user, required=True)
    doc_sender = fields.Many2one('res.users', string="Sender", required=True)
    doc_subject = fields.Char(string="Subject", required=True)

    filing = fields.Char(string="Filing")

    remarks = fields.Text(string="Remarks")
    status = fields.Selection([('active', 'Active'), ('cancelled', 'Cancelled')], string="Status", default='active')

    @api.model
    def create(self, vals):

        _logger.info('Create method called for Register model')  # Log that the method was called
        # Ensure doc_ref is generated before the record is created
        if 'doc_ref' not in vals or not vals['doc_ref']:
            _logger.info('Generating doc_ref sequence...')  # Log sequence generation

            # Retrieve the doc_register ID from vals
            if 'doc_register_id' in vals:
                register = self.env['genreg.register'].browse(vals['doc_register_id'])
                if register and register.sequence:
                    seq_code = register.sequence.code
                    _logger.info(f'Sequence code: {seq_code}')
                    vals['doc_ref'] = self.env['ir.sequence'].next_by_code(seq_code) or '/'
                    _logger.info(f'Doc Ref generated: {vals["doc_ref"]}')
                else:
                    _logger.warning('No sequence found for the selected register.')
            else:
                _logger.warning('No doc_register_id provided in vals.')
        return super(GenRegRecord, self).create(vals)

    @api.model
    def _get_default_confidentiality(self):
        # Fetch the confidentiality level where 'default' field is True
        default_confidentiality = self.env['genreg.confidentiality'].search([('default', '=', True)], limit=1)
        return default_confidentiality.id if default_confidentiality else False

    cancelled_display = fields.Char(string="C", compute='_compute_cancelled_display')

    @api.depends('status')
    def _compute_cancelled_display(self):
        for record in self:
            if record.status == 'cancelled':
                record.cancelled_display = 'C'
            else:
                record.cancelled_display = ''

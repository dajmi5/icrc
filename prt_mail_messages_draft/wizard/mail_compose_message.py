###################################################################################
#
#    Copyright (C) 2020 Cetmix OÜ
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU LESSER GENERAL PUBLIC LICENSE as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

from odoo import _, fields, models

from ..models.tools import _select_draft


class MailComposer(models.TransientModel):
    _name = "mail.compose.message"
    _inherit = "mail.compose.message"

    current_draft_id = fields.Many2one("prt.mail.message.draft", string="Draft")

    def _prepare_draft_value(self, action):
        """
        Prepare value for message draft
        :param str action: 'link' - Command.link, 'set' - Command.set
        :return dict: prepared value for draft record
        """
        values = {
            "res_id": self.res_id,
            "model": self.model,
            "parent_id": self.parent_id.id,
            "author_id": self.author_id.id,
            "subject": self.subject,
            "signature_location": self.signature_location,
            "wizard_mode": self.wizard_mode,
            "subtype_id": self.subtype_id.id,
            "body": self.body,
        }
        if action == "link":
            values.update(
                {
                    "partner_ids": [
                        (4, partner_id) for partner_id in self.partner_ids.ids
                    ],
                    "attachment_ids": [
                        (4, attachment_id) for attachment_id in self.attachment_ids.ids
                    ],
                }
            )
        elif action == "set":
            values.update(
                {
                    "partner_ids": [(6, False, self.partner_ids.ids)],
                    "attachment_ids": [(6, False, self.attachment_ids.ids)],
                }
            )
        else:
            raise models.ValidationError(_("Unknown method"))
        return values

    def _update_existing_draft(self, draft):
        """
        Update existing draft
        :param draft: prt.mail.message.draft record
        :return: updated prt.mail.message.draft record
        """
        vals = self._prepare_draft_value("set")
        return draft.write(vals)

    def _create_new_draft(self):
        """Create new draft"""
        vals = self._prepare_draft_value("link")
        return self.env["prt.mail.message.draft"].create(vals)

    def _save_draft(self, draft):
        """
        Save draft wrapper
        :param draft: prt.mail.message.draft record
        :return: updated/new prt.mail.message.draft record
        """
        self.ensure_one()
        if draft:
            return self._update_existing_draft(draft)
        return self._create_new_draft()

    def save_draft(self):
        """Save draft button"""
        result = self._save_draft(self.current_draft_id)
        if self._context.get("save_mode") == "save":
            return _select_draft(self.current_draft_id or result)
        if self.wizard_mode == "compose":
            return self.env["ir.actions.act_window"]._for_xml_id(
                "prt_mail_messages_draft.action_prt_mail_messages_draft"
            )

    def _action_send_mail(self, auto_commit=False):
        result = super()._action_send_mail(auto_commit=auto_commit)
        self.env["prt.mail.message.draft"].sudo().search(
            [
                ("model", "=", self.model),
                ("res_id", "=", self.res_id),
                ("write_uid", "=", self.create_uid.id),
            ]
        ).sudo().unlink()
        if not self._context.get("wizard_mode") == "compose":
            return result
        return self.env["ir.actions.act_window"]._for_xml_id(
            "prt_mail_messages.action_prt_mail_messages"
        )

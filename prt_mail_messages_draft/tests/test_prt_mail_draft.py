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

from odoo.tests import Form, TransactionCase


class TestPrtMailDraft(TransactionCase):
    def setUp(self):
        super().setUp()
        self.res_partner_test_1 = self.env.ref("prt_mail_messages.res_partner_test_1")
        self.prt_mail_message_draft_test_1 = self.env["prt.mail.message.draft"].create(
            {
                "subject": "Test Subject #1",
                "body": "Test text body",
            }
        )

    def test_create_draft(self):
        subject = "Test Wizard!"
        body = "Test Body text!"
        prt_mail_messages_draft_obj = self.env["prt.mail.message.draft"]

        form = Form(self.env["mail.compose.message"])
        form.partner_ids.add(self.res_partner_test_1)
        form.subject = subject
        form.body = body
        wizard = form.save()
        action = wizard.with_context(save_mode="save").save_draft()
        self.assertEqual(
            action.get("name"),
            "New message",
            msg="Action name must be equal to 'New message'",
        )
        self.assertEqual(
            action.get("res_model"),
            "mail.compose.message",
            msg="res_model value must be equal to 'mail.compose.message'",
        )
        self.assertEqual(
            action.get("type"),
            "ir.actions.act_window",
            msg="Action type must be equal to 'ir.actions.act_window'",
        )
        self.assertEqual(
            type(action["context"]["default_current_draft_id"]),
            int,
            msg="Value type must be equal to int",
        )
        draft_id = action["context"]["default_current_draft_id"]
        draft_obj_id = prt_mail_messages_draft_obj.browse(draft_id)
        self.assertEqual(
            draft_obj_id.subject, subject, msg="Subjects value must be the same"
        )
        self.assertIn(body, draft_obj_id.body, msg="Bodies value must be the same")
        self.assertFalse(draft_obj_id.model, msg="Model not set")
        self.assertFalse(draft_obj_id.res_id, msg="Record ID not set")
        self.assertEqual(
            draft_obj_id.partner_ids,
            self.res_partner_test_1,
            msg="Partners must be the same",
        )

        new_subject = "Test Wizard Change #1"
        wizard.subject = new_subject
        action = wizard.with_context(save_mode="save").save_draft()
        self.assertEqual(
            type(action["context"]["default_current_draft_id"]),
            int,
            msg="Value type must be equal to int",
        )
        updated_draft_id = action["context"]["default_current_draft_id"]
        updated_draft_obj_id = prt_mail_messages_draft_obj.browse(updated_draft_id)
        self.assertEqual(
            updated_draft_obj_id.subject,
            new_subject,
            msg="Subjects value must be the same",
        )
        self.assertIn(
            body, updated_draft_obj_id.body, msg="Bodies value must be the same"
        )

    def test_create_draft_result_none(self):
        subject = "Test Wizard!"
        body = "Test Body text!"

        form = Form(self.env["mail.compose.message"])
        form.partner_ids.add(self.res_partner_test_1)
        form.subject = subject
        form.body = body
        test_wizard = form.save()
        action = test_wizard.save_draft()
        self.assertIsNone(action, msg="Action must be empty")

    def test_prepare_model_dict(self):
        valid_variant_dict = {"res.partner": ["Contact", 1]}
        res_partner_model_id = self.env["ir.model"]._get("res.partner")
        result = self.env["prt.mail.message.draft"]._prepare_model_dict(
            res_partner_model_id
        )
        self.assertEqual(valid_variant_dict, result, msg="Values must be the same")

    def test_prepare_subject_display(self):
        default_subject_display = "=== No Reference ==="
        empty_model_dict = {}
        subject = self.prt_mail_message_draft_test_1._prepare_subject_display(
            empty_model_dict
        )[1]
        self.assertEqual(
            subject,
            default_subject_display,
            msg="Subject must be equal to '=== No Reference ==='",
        )
        self.prt_mail_message_draft_test_1.write(
            {
                "model": self.res_partner_test_1._name,
                "res_id": self.res_partner_test_1.id,
            }
        )
        subject = self.prt_mail_message_draft_test_1._prepare_subject_display(
            empty_model_dict
        )[1]
        self.assertEqual(
            subject,
            default_subject_display,
            msg="Subject must be equal to '=== No Reference ==='",
        )

        valid_result = "Contact: Test Partner #1"
        valid_variant_dict = {"res.partner": ["Contact", 1]}
        subject = self.prt_mail_message_draft_test_1._prepare_subject_display(
            valid_variant_dict
        )[1]
        self.assertEqual(
            subject,
            valid_result,
            msg="Subject must be equal to 'Contact: Test Partner #1'",
        )

        valid_result = "Contact => Test Subject #1"
        invalid_variant_dict = {"res.partner": ["Contact", 0]}
        subject = self.prt_mail_message_draft_test_1._prepare_subject_display(
            invalid_variant_dict
        )[1]
        self.assertEqual(
            subject,
            valid_result,
            msg="Subject must be equal to 'Contact => Test Subject #1'",
        )
        self.prt_mail_message_draft_test_1.subject = ""
        subject = self.prt_mail_message_draft_test_1._prepare_subject_display(
            invalid_variant_dict
        )[1]
        self.assertEqual(
            subject,
            default_subject_display,
            msg="Subject must be equal to '=== No Reference ==='",
        )

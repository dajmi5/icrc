from odoo import api, models


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _inherit = ['helpdesk.ticket', "tier.validation"]

    _tier_validation_buttons_xpath = "/form/header/field[@name='stage_id']"
    _state_from = ["draft", "cancel"]
    _state_to = ["confirmed"]
    _cancel_state = ["inactive"]
    _tier_validation_manual_config = False

    @api.model
    def _ticket_tier_revalidation_fields(self, vals):
        """
        Changing some Partner fields forces Tier Validation to be reevaluated.
        Out of the box these are is_company and parent_id.
        Other can be added extending this method.
        """
        # IDEA: make it a System Parameter?
        return [
            "partner_id",
            "project_id",
            "state_id",
            "category_id",
        ]

    def write(self, vals):
        # Changing certain fields requires a new validation process
        revalidate_fields = self._ticket_tier_revalidation_fields(vals)
        if any(x in revalidate_fields for x in vals.keys()):
            vals["stage_id"] = self._get_default_stage_id().id
        # Tier Validation does not work with Stages, only States :-(
        # Workaround is to signal state transition adding it to the write values
        if "stage_id" in vals:
            stage_id = vals.get("stage_id")
            stage = self.env["helpdesk.ticket.stage"].browse(stage_id)
            vals["state"] = stage.state
        res = super().write(vals)
        if "stage_id" in vals and vals.get("stage_id") in self._state_from:
            self.restart_validation()
        return res
/** @odoo-module **/

import { ControlPanel } from "@web/search/control_panel/control_panel";
import { useService } from "@web/core/utils/hooks";

const { onWillStart } = owl;

export class GenRegControlPanel extends ControlPanel {
    setup() {
        super.setup();
        this.orm = useService("orm");
        this.user = useService("user");
        const { active_id, show_project_update } = this.env.searchModel.globalContext;
        this.showProjectUpdate = this.env.config.viewType === "form" || show_project_update;
        this.genRegId = this.showProjectUpdate ? active_id : false;

        onWillStart(async () => {
            if (this.showProjectUpdate) {
                await this.loadData();
            }
        });
    }

    async loadData() {
        const [data, isProjectUser] = await Promise.all([
            this.orm.call("genreg.register", "get_last_update_or_default", [this.genRegId]),
            this.user.hasGroup("project.group_project_user"),
        ]);
        this.data = data;
        this.isProjectUser = isProjectUser;
        console.log(data)
    }

    async onStatusClick(ev) {
        ev.preventDefault();
        this.actionService.doAction("project.project_update_all_action", {
            additionalContext: {
                default_project_id: this.projectId,
                active_id: this.projectId,
            },
        });
    }
}

GenRegControlPanel.template = "genreg.GenRegControlPanel";

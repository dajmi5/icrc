/** @odoo-module */

import { registry } from "@web/core/registry";
import { listView } from '@web/views/list/list_view';
import { GenRegControlPanel } from "../../components/genreg_control_panel/genreg_control_panel";

export const genregRecordListView = {
    ...listView,
    ControlPanel: GenRegControlPanel,
};

registry.category("views").add("genreg_record_list", genregRecordListView);
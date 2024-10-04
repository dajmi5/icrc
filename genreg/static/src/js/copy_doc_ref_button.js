/** @odoo-module **/

import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

// Define the OWL component
export class CopyDocRefButton extends Component {
    setup() {
        this.dialogService = useService("dialog");  // Using OWL's dialog service
    }

    // Method to copy the doc_ref field to the clipboard
    async copyToClipboard() {
        const docRef = this.props.record.data.doc_ref;  // Get the doc_ref from the current record

        if (docRef) {
            try {
                await navigator.clipboard.writeText(docRef);
                this.dialogService.add(AlertDialog, {
                    title: "Copied to clipboard",
                    body: "Copied " + docRef,
                })
            } catch (error) {
                console.error(error);
            }
        }
    }

}

CopyDocRefButton.template = "genreg.CopyDocRefButton";
// Register the component with Odoo's widget registry
registry.category("fields").add("CopyDocRefButton", CopyDocRefButton);

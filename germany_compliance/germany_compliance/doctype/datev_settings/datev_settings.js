// Copyright (c) 2022, Frappe Technologies Private Limited[C and contributors
// For license information, please see license.txt

frappe.ui.form.on('DATEV Settings', {
	refresh: function(frm) {
		frm.add_custom_button('Show Report', () => frappe.set_route('query-report', 'DATEV'), "fa fa-table");
	}
});

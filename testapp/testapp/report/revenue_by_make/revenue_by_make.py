# Copyright (c) 2024, AL and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = frappe.get_all("Ride Booking",  fields=["SUM(amount) AS total_revenue", "vehicle.make"],filters={"docstatus": 1},  group_by = "make")
	chart = {
		"data":{
			"labels": [x.make for x in data],
			"datasets": [{"values": [x.total_revenue for x in data]}],
		},
		"type": "pie",
	}

	return columns, data, "This is a report", chart


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Make"),
			"fieldname": "make",
			"fieldtype": "Data",
		},
		{
			"label": _("Revenue"),
			"fieldname": "total_revenue",
			"fieldtype": "currency",
			"options": "PHP"
		},
	]


# def get_data() -> list[list]:
# 	"""Return data for the report.

# 	The report data is a list of rows, with each row being a list of cell values.
# 	"""
	# data = frappe.get_all(
	# 		"Ride Booking",
	# 		fields=["SUM(amount) AS total_revenue", "vehicle.make"],
	# 		filters={"docstatus": 1},
	# 		group_by="make"
	# 	)

	# report_data = []
	# for row in data:
	# 	report_data.append(row['vehicle.make'], row['total_revenue'])

	# return report_data
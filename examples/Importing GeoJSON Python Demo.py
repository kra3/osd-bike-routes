# TITLE: Importing GeoJSON Example in Python
# AUTHOR: Tom Schenk Jr., City of Chicago
# CREATED: 2013-01-23
# UPDATED: 2013-02-03
# NOTES: Quick example to import GeoJSON data in Python.
# MODULES: json

import json
bikeroutes_json = open('PATH/TO/FILE/data/Bikeroutes.json', 'r')
# FIXME: Is json_data == bikeroutes_json ? if not from where it's added to the scope!
# So if it indeed a mistake then uncomment next line, or rename json_data to bikeroutes_json
# bikeroutes_json = json_data
bike_routes = json.load(json_data)
json_data.close()

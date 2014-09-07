import json

settings_json = json.dumps([
    {'type': 'options',
     'title': 'Select unit',
     'desc': 'Change unit type',
     'section': 'preferences',
     'key': 'unit',
     'options': ['m/s', 'km/h', 'mi/h']}
])

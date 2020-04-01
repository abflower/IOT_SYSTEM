#Automation list 
automations_list = [{'id': '1', 'name': 'get weather in Palermo', 'status': 0}, {'id': '2', 'name': 'get weather in Bristol', 'status': 0}, {'id': '3', 'name': 'test automation', 'status': 0}, {'id': '4', 'name': 'stove Bristol', 'status': 0}]

# Automation page
info = {'status': 0, 'id': '1', 'name': 'get weather in Palermo', 'service': 'open_weather', 'params': {'city': 'Palermo,IT', 'api_key': '', 'api_url': 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='}, 'condition_type': 'time_day_only', 'conditions': {'days': [0], 'time_on': '00:00', 'time_off': '13:59'}, 'function': 'get_weather', 'extra_params': [{'name': 'city', 'type': 'string', 'required': True}]}
service_data = [{'name': 'city', 'value': 'Palermo,IT'}]
conditions_list = [{'name': 'days', 'value': [0]}, {'name': 'time_on', 'value': '00:00'}, {'name': 'time_off', 'value': '13:59'}]
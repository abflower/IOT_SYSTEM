
from flask import request
from wtforms import Form, StringField

def create_automation_form(data):
    automation_data = data

    class AutomationForm(Form):
        name=StringField(
            label='Automation\'s name', default=automation_data['name']
        )
        #for param in automation_data['extra_params']:

    form = AutomationForm(request.form)
    return form
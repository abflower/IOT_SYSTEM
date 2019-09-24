from flask import Flask, make_response, render_template, request

# this files contains some parts of the baisc flask app

automations = []

##### FLASK ######
app = Flask(__name__)

@app.route('/')
def index():
    return '''HOME</br>
    <a href="/autom_list">List of automations</a>'''

@app.route('/autom_list')
def autom_list():
    automations_list = []
    for automation in automations:
        field = {}
        field['id'] = automation.id
        field['name'] = automation.name
        field['status'] = automation.status
        automations_list.append(field)
    response = make_response(render_template("automations_list.html", automations_list=automations_list))
    return response

@app.route('/autom_page')
def autom_page():
    id = request.args.get('id')
    response=''
    for automation in automations:
        if automation.id == id:
            info = automation.return_all_attrs()
            service_fields = []
            for param in automation.extra_params:
                field = {}
                field['name'] = param['name']
                field['value'] = automation.params[param['name']]
                service_fields.append(field)
            conditions_list = []
            for key in automation.conditions.keys():
                field = {}
                field['name'] = key
                field['value'] = automation.conditions[key]
                conditions_list.append(field)

            response = make_response(render_template("single_automation.html", info=info, service_fields=service_fields, conditions_list=conditions_list))
    return response

if __name__ == '__main__':
    app.run(debug=True)
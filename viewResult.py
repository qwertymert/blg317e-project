from flask import Blueprint, render_template, current_app, request
from MySqlRepository import MySQLRepository

viewResult = Blueprint('viewResult', __name__)

@viewResult.route("/results", methods=["GET", "POST"])
def results_page():
    repo = MySQLRepository()  
    columns = repo.get_columns('results')
    if request.method == 'POST':
        # If the "Show All" button is clicked, fetch all drivers
        result_data = repo.read('results')
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('results.html', result_data=result_data, columns=columns, table_names=table_names,bool=True)
    else:
        # Otherwise, fetch a limited number of drivers (adjust the limit as needed)
        table_names = repo.get_table_names()
        table_names = [name[0] for name in table_names]
        return render_template('results.html', columns=columns, table_names=table_names,bool=False)
    
@viewResult.route("/results/filter_data", methods=["POST"])
def filter_data():
    repo = MySQLRepository()

    # Handle filtering based on the submitted form data
    filter = (request.form.get('filter_input'))
    column = request.form.get('column_input')


    result_data = repo.read('results',filter, column)
    columns = repo.get_columns('results')
    table_names = repo.get_table_names()
    table_names = [name[0] for name in table_names]
    return render_template('results.html', result_data=result_data, columns=columns, table_names=table_names,bool=True)
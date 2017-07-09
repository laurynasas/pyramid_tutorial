from pyramid.view import view_config


# First view, available at http://localhost:6543/
@view_config(route_name='home', renderer='home.jinja2')
def home(request):
    return {'name': 'Home View'}


# /howdy
@view_config(route_name='hello', renderer='home.jinja2')
def hello(request):
    return {'name': 'Hello View'}
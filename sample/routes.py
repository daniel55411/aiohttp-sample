import views


def setup_routes(app):
    app.router.add_get('/user/{name}/add', views.add)
    app.router.add_get('/user/{name}/results', views.results)
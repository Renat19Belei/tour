from .settings import main
import home_app
import tour_app
import user_app
import personalization_app

main.add_url_rule(rule= '/', view_func= home_app.render_home, methods = ["GET","POST"])
main.add_url_rule(rule= '/login/', view_func= user_app.render_login, methods = ["GET","POST"])
main.add_url_rule(rule= '/logout/', view_func= user_app.render_logout)
main.add_url_rule(rule= '/registration/', view_func= user_app.render_registration, methods = ["GET","POST"])
main.add_url_rule(rule= '/tour/', view_func= tour_app.render_tour, methods = ["GET","POST"])
main.add_url_rule(rule= '/personal/', view_func= personalization_app.render_personalization, methods= ["GET","POST"])

main.register_blueprint(home_app.home)
main.register_blueprint(user_app.user)
main.register_blueprint(tour_app.tour)
main.register_blueprint(personalization_app.personalization)
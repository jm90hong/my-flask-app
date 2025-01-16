from .view_route import view_route
from .user_route import user_route
from .ai_route import ai_route




blueprints = [
   (view_route,"/"),
   (user_route,"/api/user"),
   (ai_route,"/api/ai")
]


def register_blueprints(app):
    for blueprint,prefix in blueprints:
        app.register_blueprint(blueprint,url_prefix=prefix)


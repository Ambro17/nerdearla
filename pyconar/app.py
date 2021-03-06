from flask import Flask
from graphql import get_introspection_query
import json

from pyconar.views.voyager_view import APIExplorer
from pyconar.views.flask_view import GraphQLAPI
from pyconar.schema import schema
from pyconar.db.database import db


def create_app():
    app = Flask(__name__, static_folder='static')

    # Serve Graphiql IDE at /
    graphiql = GraphQLAPI.as_view("graphiql", schema=schema, use_playground=False)
    app.add_url_rule("/", view_func=graphiql)


    # Serve Graphiql IDE at /dark
    graphiql = GraphQLAPI.as_view("playground", schema=schema, use_playground=True)
    app.add_url_rule("/dark", view_func=graphiql)


    # Serve Explorer at /explorer
    introspection = schema.execute_sync(get_introspection_query())
    explorer = APIExplorer.as_view("voyager",
                                introspection=json.dumps({'data': introspection.data}))
    app.add_url_rule("/explorer", view_func=explorer)

    # Handle database connections per request
    @app.before_request
    def before_request():
        db.connect()

    @app.after_request
    def after_request(response):
        db.close()
        return response


    return app


if __name__ == "__main__":
    create_app().run()

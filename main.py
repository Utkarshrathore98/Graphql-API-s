from flask import Flask, request, send_file, jsonify
from ariadne import graphql_sync, make_executable_schema, gql, load_schema_from_path
from resolver.query_resolver import query

type_defs = gql(load_schema_from_path("./schema"))
schema = make_executable_schema(type_defs, query)

app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return send_file("playground.html")

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request)
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


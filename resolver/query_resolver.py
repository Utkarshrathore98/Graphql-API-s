from ariadne import QueryType
from services.services import getPrintStatement

query = QueryType()

@query.field("getPrintStatement")
def resolve_getPrintStatement(obj, info, filter):
    try:
        return getPrintStatement(filter)
    except Exception as e:
        raise Exception(f"Exception: Error in printing statements! {str(e)}")

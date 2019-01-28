from ..exceptions import InvalidAPIRequest, InvalidContentType


class RequireJSON(object):

    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise InvalidContentType(
                description='This API only supports responses encoded as JSON.'
            )

        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise InvalidAPIRequest(
                    description='This API only supports'
                                'requests encoded as JSON.'
                )

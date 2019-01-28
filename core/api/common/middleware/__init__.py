from . import response
from .context import ContextMiddleware
from .request import RequireJSON


class AfterRequestMiddleware:

    def process_response(self, req, resp, resource):
        response.commit_session(resp)
        response.shutdown_session()
        return


__all__ = ['ContextMiddleware', 'RequireJSON', 'AfterRequestMiddleware']

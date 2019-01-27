import falcon


class FalconException(falcon.HTTPError):
    """Custom Excepetion based from falcon
    """
    status = falcon.HTTP_500
    title = None
    description = ''
    href = None

    def __init__(self,
                 title=None,
                 description=None,
                 status=None,
                 href=None
                 ):
        if status is not None:
            self.status = status
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if href is not None:
            self.href = href

        super().__init__(
            status=self.status,
            title=self.title,
            description=self.description,
            href=self.href
        )


class InvalidContentType(FalconException):
    """
    Raised when an invalid Content-Type is provided.
    """
    status = falcon.HTTP_406
    href = 'https://banaspati.fromindonesia.com/api/json'


class InvalidPermissions(FalconException):
    status = falcon.HTTP_401


class InvalidAPIRequest(FalconException):
    """
    Raised when an invalid request has been made.
    (e.g. accessed unexisting url, the schema validation did
    not pass)
    """
    status = falcon.HTTP_UNSUPPORTED_MEDIA_TYPE
    href = 'https://banaspati.fromindonesia.com/api/json'


class DatabaseError(FalconException):
    """
    Generic database interaction error.
    Inherit this error for all subsequent
    errors that are related to database.
    """
    pass


class RecordNotFound(DatabaseError):
    """
    Raised when the record was not found in the database.
    """
    status = falcon.HTTP_404


class RecordAlreadyExists(DatabaseError):
    """
    Raised in the case of violation of a unique constraint.
    """
    status = falcon.HTTP_409

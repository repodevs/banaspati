def get_status_code(status):
    """Get status code by HTTP status line

    :param status: HTTP status line (e.g., '200 OK').
    :return: HTTP status code
    :rtype: int
    """
    code = int(status.split(' ')[0])
    return code

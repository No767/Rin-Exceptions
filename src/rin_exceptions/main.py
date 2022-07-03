class Error(Exception):
    """The base class for all exceptions. This should not be explicitly raised or called.

    Args:
        Exception (Exception): Base exception for this class
    """
    pass


class UnknownPlayer(Error):
    """Raised when there is no player found within the Hypixel Cog.

    Args:
        Error (_type_): Base Error
    """
    pass


class NotFoundHTTPException(Error):
    """Raised when there is usually an HTTP 404 error within the API

    Args:
        Error (_type_): Base Error
    """
    pass


class NoItemsError(Error):
    """Raised when there are no items found. This should be raised instead of NotFoundHTTPException when the HTTP status is still 2xx-3xx.

    Args:
        Error (_type_): Base Error
    """
    pass


class ThereIsaRSlashInSubreddit(Error):
    """Raised when there is an r/ within the subreddit name. This should be only raised in the Reddit Cog. 

    Args:
        Error (_type_): Base Error
    """
    pass


class HTTPException(Error):
    """Raised when the HTTP status of the request is 5xx

    Args:
        Error (_type_): Base Error
    """
    pass


class InvalidToken(Error):
    """Raised when the token being used for authentication is invalid.

    Args:
        Error (_type_): Base Error
    """
    pass

class ItemNotFound(Error):
    """Rasied when the item within the Marketplace is not found. This is used in Kumiko's Economy system. This should only be raised when the item within the database is not found.

    Args:
        Error (_type_): Base Error
    """
    pass


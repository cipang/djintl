from functools import wraps


def page_info(page_id: str = None, page_title: str = None):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            request.page_info = {
                "page_id": page_id,
                "page_title": page_title
            }
            return view(request, *args, **kwargs)
        return _wrapped_view
    return decorator

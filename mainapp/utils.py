from functools import wraps


def page_info(page_id: str = None, page_title: str = None):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(*args, **kwargs):
            response = view(*args, **kwargs)
            if hasattr(response, "context_data"):
                response.context_data["page_id"] = page_id
                response.context_data["page_title"] = page_title
            else:
                raise RuntimeError(f"TemplateResponse expected, but got {type(response).__name__}.")
            return response
        return _wrapped_view
    return decorator

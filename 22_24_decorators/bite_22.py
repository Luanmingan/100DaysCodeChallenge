from functools import wraps


def make_html(element):
    def decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            return '<{}>{}</{}>'.format(element, func(*args, **kwargs), element)
        return wrap
    return decorator


@make_html('p')
@make_html('strong')
def get_text(text='I Code with PyBites'):
    return text


html_tag = get_text()
print(html_tag)

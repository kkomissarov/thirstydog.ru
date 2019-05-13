from django import template
register = template.Library()

#Приводит int к str формата "20 000 руб."
@register.filter
def price_format(value):

    result = []
    x = 0
    for l in reversed(str(value)):
        if x < 3:
            result.append(l)
            x += 1
        else:
            result.append(l+' ')
            x = 0

    return '{} руб'.format(''.join(reversed(result)))


from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent').prefetch_related('children')

    current_url = request.path
    active_item = None
    for item in menu_items:
        if item.get_url() == current_url:
            active_item = item
            break

    return {
        'menu_items': menu_items,
        'active_item': active_item,
    }


from django import template
from menu.models import Items
from django.utils.datastructures import MultiValueDictKeyError


register = template.Library()

@register.inclusion_tag("menu_tag.html", takes_context=True)
def show_menu(context, menu_name):
    menu = Items.objects.filter(menu__title=menu_name)
    items_values = menu.values("title", "menu_id", "parent_id", "id")
    items = [item for item in items_values.filter(parent=None)]
    try:
        aktiv_items_id = int(context["request"].GET[menu_name])
        aktiv_item = menu.get(id=aktiv_items_id)
        items_id_list = get_items_id_list(aktiv_item)
        for item in items:
            if item["id"] in items_id_list:
                item["child_items"] = get_chield(item["id"], items_values, items_id_list)
        return {"menu": menu_name, "items": items}
    except MultiValueDictKeyError:
        return {"menu": menu_name, "items": items}
    
def get_chield(item_id, items_values, items_id_list):
    items = [item for item in items_values.filter(parent_id=item_id)]
    for item in items:
        if item["id"] in items_id_list:
            item["child_items"] = get_chield(item["id"], items_values, items_id_list)
    return items

def get_items_id_list(aktiv_item):
    items_id_list = []
    items_id_list.append(aktiv_item.id)
    parent = aktiv_item.parent
    while parent:
        items_id_list.append(parent.id)
        parent = parent.parent
    if not items_id_list:
        items_id_list.append(aktiv_item.id)
    return items_id_list
        


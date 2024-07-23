
def get_ordered_queryset(queryset, query_params, type=""):
    order = query_params.get("orderBy")
    if order:
        if order == "orderByNameAsc":
            return queryset.order_by("name")
        elif order == "orderByNameDesc":
            return queryset.order_by("-name")
        elif order == "orderByIdAsc":
            return queryset.order_by("id")
        elif order == "orderByIdDesc":
            return queryset.order_by("-id")
        elif order == "orderByDateAsc":
            return queryset.order_by("created_at")
        elif order == "orderByDateDesc":
            return queryset.order_by("-created_at")
        elif order == "default":
            if type == "user":
                return queryset.order_by("id")
            else:
                return queryset.order_by('name')
    elif type == "muscle":
        return queryset.order_by('name')
    elif type == "injury":
        return queryset.order_by('-date')
    elif type == "user":
        return queryset.order_by('id')
    else:
        return queryset.order_by("name")

def get_ordered_queryset(queryset, query_params):
    order = query_params.get("orderBy")
    if order:
        if order == "orderByNameAsc":
            return queryset.order_by("name")
        elif order == "orderByNameDesc":
            return queryset.order_by("-name")
        elif order == "orderByIdAsc" or order == "default":
            return queryset.order_by("id")
        elif order == "orderByIdDesc":
            return queryset.order_by("-id")
        elif order == "orderByDateAsc":
            return queryset.order_by("created_at")
        elif order == "orderByDateDesc":
            return queryset.order_by("-created_at")
    return queryset.order_by("id")
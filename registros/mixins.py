from rest_framework.response import Response

class LimitPaginationMixin:
    def list(self, request, *args, **kwargs):
        # Obtén el queryset filtrado y ordenado
        queryset = self.filter_queryset(self.get_queryset())

        # Extrae el parámetro "limit" y aplica slicing si está presente
        limit = request.query_params.get('limit')
        if limit:
            try:
                limit = int(limit)
                queryset = queryset[:limit]
            except ValueError:
                pass

        # Aplica la paginación
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # Si no hay paginación, serializa todo el queryset
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination, pagination.LimitOffsetPagination):
    page_size = 1
    page_size_query_description = 'page_size'
    max_page_size = 50
    page_query_param = 'page'
    
    def __init__(self, request):
        self.page_size = int(request.query_params.get('limit', 1))
        
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'current_page': int(self.request.query_params.get('page', 1)),
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'total': self.page.paginator.count,
            'per_page': self.page_size,
            'total_pages': int(round(self.page.paginator.count/self.page_size, 1)),
            'data': data,
        })




def list(self, request):
        admin = Admin.objects.all()
        obj = CustomPagination(self.request)
        page = obj.paginate_queryset(admin, request)
        
        if page is not None:
            serializer = AdminSerializer(page, many=True)
            return obj.get_paginated_response(serializer.data)

from rest_framework.pagination import PageNumberPagination

class TinnyResultsSetPagination(PageNumberPagination):
    page_size = 5
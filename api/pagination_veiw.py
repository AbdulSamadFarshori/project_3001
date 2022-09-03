from rest_framework.pagination import LimitOffsetPagination

class Pagination(LimitOffsetPagination):
	defualt_limit = 1
	
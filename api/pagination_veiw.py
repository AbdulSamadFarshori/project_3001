from rest_framework.pagination import LimitOffsetPagination

class MyPagination(LimitOffsetPagination):
	defualt_limit = 1

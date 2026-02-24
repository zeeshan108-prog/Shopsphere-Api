from rest_framework.permissions import BasePermission

class IsAdminUserCustom(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ADMIN'


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'CUSTOMER'
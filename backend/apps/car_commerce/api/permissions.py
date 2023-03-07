from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        """admin_permission, verifica si en la request hay un user y si ese usuario,
        es un usuario adminstrador.

        Luego retorna un True si la solicitud es del tipo GET o si admin_permission==True
        de esta manera solo los administradores podran acceder al CRUD de los modelos
        """
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission

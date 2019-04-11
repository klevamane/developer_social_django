from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
       Object-level permission to only allow owners of an object to edit it.
       Assumes the model instance has an `owner` attribute.
    """
    # message = 'You must be the owner of this owner in order to make changes to the {}' \
    #     .format (obj.__class__.__name__)
    message = 'You must be the owner in order to view or make changes'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS and obj.developer.id == request.user.id:
            return True
        # Instance must have an attribute named `owner`. but ours is developer
        return obj.developer == request.user


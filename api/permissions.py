from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "You must be owner of this post to edit."

    # my_safe_method = ['PUT', 'POST', 'DELETE', 'GET']
    #
    def has_permission(self, request, view):
        if 'pk' in view.kwargs and view.kwargs['pk']:
            # obj = Api.objects.get(pk=view.kwargs['pk'])
            obj = view.get_queryset().values()[0]
            if obj['user_id'] == request.user.id:
                return True
            return False
        else:
            return False
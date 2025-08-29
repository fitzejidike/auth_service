from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from ratelimit.decorators import ratelimit
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import User
from .serializers import RegisterSerializer
import uuid

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    @ratelimit(key='ip', rate='5/m', block=True)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @ratelimit(key='ip', rate='3/m', block=True)
    def post(self, request):
        email = request.data.get("email")
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        token = str(uuid.uuid4())
        cache.set(token, email, timeout=600)
        return Response({"reset_token": token})

    @ratelimit(key='ip', rate='3/m', block=True)
    def post(self, request):
        token = request.data.get("token")
        new_password = request.data.get("password")
        email = cache.get(token)

        if not email:
            return Response({"error": "Invalid or expired token"}, status=400)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        user.set_password(new_password)
        user.save()
        cache.delete(token)

        return Response({"message": "Password reset successful"})
        user.set_password(new_password)
        user.save()
        cache.delete(token)

        return Response({"message": "Password reset successful"})

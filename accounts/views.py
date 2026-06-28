from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now, timedelta
import random
from .models import User, OTPCode
from .serializers import UserSerializer

class RequestOTPView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        mobile = request.data.get('mobile')
        if not mobile:
            return Response({'error': 'شماره موبایل الزامی است'}, status=400)
        code = str(random.randint(100000, 999999))
        OTPCode.objects.filter(mobile=mobile, is_used=False).update(is_used=True)
        OTPCode.objects.create(
            mobile=mobile,
            code=code,
            expires_at=now()+timedelta(minutes=2),
            purpose='REGISTER'
        )
        # در نسخه واقعی، کد را به پیامک وصل کنید
        return Response({'message': 'کد ارسال شد', 'code': code})

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        mobile = request.data.get('mobile')
        code = request.data.get('code')
        try:
            otp = OTPCode.objects.get(mobile=mobile, code=code, is_used=False, expires_at__gt=now())
        except OTPCode.DoesNotExist:
            return Response({'error': 'کد نامعتبر یا منقضی'}, status=400)
        otp.is_used = True
        otp.save()
        user, created = User.objects.get_or_create(mobile=mobile)
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': UserSerializer(user).data
        })

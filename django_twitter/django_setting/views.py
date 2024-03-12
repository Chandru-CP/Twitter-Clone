from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ChangeUsernameForm, ChangeEmailForm, ChangeMobileNumberForm
from rest_framework import generics, status, response
from django_accounts.models import CustomUser as User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from . import serializers


@login_required()
def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Username changed successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = ChangeUsernameForm(instance=request.user)

    return render(request, 'django_setting/change_username.html', {'form': form})

@login_required()
def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Email changed successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ChangeEmailForm(instance=request.user)
    return render(request, 'django_setting/change_email.html', {'form': form})

@login_required()
def change_mobile_number(request):
    if request.method == 'POST':
        form = ChangeMobileNumberForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mobile number changed successfully.')
            print('Mobile number changed successfully.')
            return redirect('profile')
        else:
            print(form.errors)
            print('Mobile number failed to update')
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ChangeMobileNumberForm(instance=request.user)
    return render(request, 'django_setting/change_mobile_number.html', {'form': form})


class PasswordReset(generics.GenericAPIView):
    serializer_class = serializers.EmailSerializer

    def post(self, request):
        """
        Create token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"127.0.0.1:8000{reset_url}"

            # send the rest_link as mail to the user.

            return response.Response(
                {
                    "message":
                    f"Your password rest link: {reset_link}"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return response.Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ResetPasswordAPI(generics.GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class = serializers.ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        """
        Verify token & encoded_pk and then reset the password.
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )

@login_required()
def setting(request):
    return render(request, 'django_setting/setting.html')

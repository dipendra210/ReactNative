from django.shortcuts import render
from django.http import HttpResponse
from authy.api import AuthyApiClient

def register(request):
    if request.method == 'POST':

        authy_user = authy_api.users.create(
        form.cleaned_data['email'],
        form.cleaned_data['phone_number'],
        form.cleaned_data['country_code'],
        )
        if authy_user.ok():
            twofa_user = TwoFAUser.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            authy_user.id,
            form.cleaned_data['password']
        )
            login(request, twofa_user)
            return redirect('2fa')
        else:
            for key, value in authy_user.errors():
                form.add_error(None, '{key}: {value}'.format(key=key, value=value)        )
    else:
        return render("OK")

def verify(request):
    authy_api = AuthyApiClient('kGMhLpEz8fxhoryGsqCoLQ8VBpVpHquk')
    verification = authy_api.tokens.verify('116415031', '4076094')
    if verification.ok():
        return HttpResponse("OK")
    else:
        return HttpResponse("Wrong")
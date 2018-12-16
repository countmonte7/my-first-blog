from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model


User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text',]

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='이메일 주소')
    email2 = forms.EmailField(label='이메일 주소 확인')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("이메일은 일치해야 합니다.")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "이 이메일은 이미 사용중입니다."
            )
        return super(UserRegisterForm, self).clean(*args, **kwargs)
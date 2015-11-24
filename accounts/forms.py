from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class QuizAuthenticationForm(AuthenticationForm):
    quiz = forms.CharField(help_text='3+3=?')

    def clean_quiz(self):
        quiz = self.cleaned_data.get('quiz', '')
        if quiz:
            if quiz != '6':
                raise forms.ValidationError('퀴즈를 맞춰보시오!!!')
        return quiz


class UserEmailCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        fields = ('email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserEmailCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

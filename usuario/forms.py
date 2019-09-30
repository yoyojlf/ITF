from django import forms
from usuario.models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['is_staff', 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions', 'created_at', 'modified_at', ]
        labels = {'username': 'username', 'password': 'password', 'first_name': 'First Name',
                  'last_name': 'Last Name', }
        help_texts = {'password': ' ', 'username': ' ', 'is_active': ''}

        widgets = {
            'password': forms.PasswordInput(),
            'presentacion': forms.Textarea,
        }

    def save(self, commit=True):  # Save the provided password in hashed format #
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    usr = forms.CharField(label='Nombre de usuario')
    pwd = forms.CharField(label='Contraseña', widget=forms.PasswordInput())

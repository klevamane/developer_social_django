from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Developer

from django import forms
# Register your models here.


class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required fields, and a repeated password
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Developer
        fields = ('firstname', 'lastname', 'email', 'password', 'date_of_birth')

    def clean_password2(self):
        # check that the password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(" Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hash format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on the user, but replaces the password field
    with admin's password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Developer
        fields = ('email', 'password', 'date_of_birth', 'firstname', 'lastname', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value
        # This is done here rather than on the field because the field does not
        # has access to the initial value
        return self.initial["password"]


class DeveloperAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','firstname', 'lastname', 'email', 'created_at', 'updated_at')
    list_display_links = ('id', 'email', 'created_at', 'updated_at')
    list_filter = ('created_at', 'email', 'is_admin')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'firstname', 'lastname')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
         ),
    )
    search_fields = ('firstname', 'lastname', 'email')
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Developer, DeveloperAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
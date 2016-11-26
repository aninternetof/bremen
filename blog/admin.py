from django.contrib import admin
from .models import Post
from .models import Tagline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Contributor

class ContributorInline(admin.StackedInline):
    model = Contributor
    can_delete = False
    verbose_name_plural = 'contributor'

class UserAdmin(BaseUserAdmin):
    inlines = (ContributorInline, )

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tagline)

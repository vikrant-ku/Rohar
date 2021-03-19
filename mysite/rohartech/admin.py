from django.contrib import admin
from .models import Contact, Web_Mobile_Budget, Website_Budget, Mobile_Budget, Photography


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'subject' ]

class BudgetAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact']

class Photography_Admin(admin.ModelAdmin):
    list_display = ['title', 'category', 'show']
    list_filter = ('category', 'show',)
    # search_fields = ('name', 'category__name', 'subcategory__name', 'sr_no', 'subcat_type', 'type', 'lable')
    list_editable = ('show',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Website_Budget, BudgetAdmin)
admin.site.register(Mobile_Budget, BudgetAdmin)
admin.site.register(Web_Mobile_Budget, BudgetAdmin)
admin.site.register(Photography, Photography_Admin)

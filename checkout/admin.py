from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import Payment
from .models import ShippingAddress


@admin.action(description='Mark selected orders as approved')
def make_approved(modeladmin, request, queryset):
    updated = queryset.update(approval=True)
    modeladmin.message_user(request, ngettext(
        '%d Payment has been marked as approved successfully.',
        '%d Payments have been marked as approved successfully.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'stripe_id', 'amount', 'issued_data', 'approval')
    search_fields = ('user__email', 'stripe_id', 'user__username')
    search_help_text = "Search by user email, user username or stripe id"
    list_filter = ('approval',)
    actions = [make_approved]


admin.site.register(ShippingAddress)

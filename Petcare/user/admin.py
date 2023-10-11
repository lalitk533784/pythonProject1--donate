from django.contrib import admin
from .models import QuickEnquiry, Newsletter, Contacts, DogAdopt,Donation


class QuickEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'location', 'message', 'service')


admin.site.register(QuickEnquiry, QuickEnquiryAdmin)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(Newsletter, NewsletterAdmin)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subjects', 'messages')


admin.site.register(Contacts, ContactsAdmin)


class DogAdoptAdmin(admin.ModelAdmin):
    list_display = (
    'fullname', 'contact', 'email', 'address', 'dogname', )


admin.site.register(DogAdopt, DogAdoptAdmin)


class DonationAdmin(admin.ModelAdmin):
    list_display =(
        'full_name','email','donation_amount','payment_method'
    )

admin.site.register(Donation, DonationAdmin)
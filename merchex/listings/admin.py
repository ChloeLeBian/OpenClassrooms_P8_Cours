from django.contrib import admin
from listings.models import Review, Ticket, UserFollows, User


class TicketAdmin(admin.ModelAdmin): 
    list_display = ('title', 'time_created', 'user') 
    # liste les champs que nous voulons sur l'affichage de la liste

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'headline', 'rating', 'user', 'time_created' )
    list_display_links = ('ticket', 'headline')
    search_fields = ['headline']
    list_filter = ['time_created']


admin.site.register(User)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(UserFollows)




# Register your models here.

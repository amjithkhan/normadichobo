from django.contrib.syndication.views import  Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from product.models import Destinations



class latestfeed(Feed):
    title="NORMADICHOBO"
    link="/drcomments/"
    description="NORMADICHOBO IS A TRAVEL WEBSITE , YOU CAN BOOK TOURS AND TRAVEL PACKAGES"



    def items(self):
        return Destinations.objects.order_by("date")[:3]

    def item_title(self, place):
        return place.name

    def item_description(self, place):
        return truncatewords (place.desc,10)
    def item_link(self,place):
        return reverse("Homepage")


from rest_framework import serializers
from .models import Event, Venue

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue_name = serializers.HyperlinkedRelatedField(
        view_name='venue_list',
        many=True,
        read_only=True
    )
    class Meta:
        model = Event
        fields = ('event_name', 'venue_name', 'event_type', 'event_description', 'event_date', 'event_time', 'ticket_price', 'ticket_quantity')

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    event_name = EventSerializer(
        many = True,
        read_only = True
    )

    class Meta:
        model = Venue
        fields = ('venue_name', 'event_name', 'address', 'description', 'url')
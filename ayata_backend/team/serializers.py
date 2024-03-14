from rest_framework import serializers
from team.models import *

class SocialLinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SocialLink
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    social_link = serializers.SerializerMethodField()

    def get_social_link(self, obj):
        social_links = SocialLink.objects.filter(user = obj)
        return SocialLinkSerializer(social_links, many =True).data
    
    class Meta:
        model = User
        fields = "__all__"
    
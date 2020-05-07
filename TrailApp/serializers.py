from rest_framework import serializers
import TrailApp.models as md

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = md.members
        fields = ('Id','real_name','tz','phone_number','starttime','endtime')
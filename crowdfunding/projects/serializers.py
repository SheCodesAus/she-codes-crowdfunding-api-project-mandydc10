from rest_framework import serializers
from .models import Project, Pledge
from users.serializers import CustomUserSerialiser

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.SerializerMethodField()
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']

    def get_supporter(self, obj):
    # do your conditional logic here
        if obj.anonymous:
            return None
        else:
            return obj.supporter.username
    def create(self,validated_data):
            return Pledge.objects.create(**validated_data)
class ProjectSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner_id')
    total = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Project.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class ProjectDetailSerializer(ProjectSerializers):
    pledges = PledgeSerializer(many=True, read_only=True)
    followed_by = CustomUserSerialiser(many=True, read_only=True)




from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from jobs.models import Job



class JobSerializer(serializers.ModelSerializer):
  
  # time_since_publication = serializers.SerializerMethodField()
  # author = JournalistSerializer(read_only=True)
  # author = serializers.StringRelatedField()  
  
  class Meta:
    model = Job
    # exclude = ("id",)
    fields = "__all__" # we want all the fields of our model
    # fields = ("title", "description", "body")
  
  def get_time_since_publication(self, object):
    publication_date = object.publication_date
    now = datetime.now()
    time_delta = timesince(publication_date, now)
    return time_delta

  def validate(self, data):
    """ check the description and title are different """
    if data["title"] == data["description"]:
      raise serializers.ValidationError("Title and Description must be different from one another")
    return data

  def validate_title(self, value):
    if len(value) < 30:
      raise serializers.ValidationError("The Title has to be at least 60 characters long")
    return value


# class JobSerializer(serializers.Serializer):
#   id                = serializers.IntegerField(read_only=True)
#   author            = serializers.CharField()
#   title             = serializers.CharField()
#   description       = serializers.CharField()
#   body              = serializers.CharField()
#   location          = serializers.CharField()
#   publication_date  = serializers.DateField()
#   active            = serializers.BooleanField()
#   created_at        = serializers.DateTimeField(read_only=True)
#   updated_at        = serializers.DateTimeField(read_only=True)

#   def create(self, validated_data):
#     print(validated_data)
#     return Article.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#     instance.autor            = validated_data.get('author', instance.author)
#     instance.title            = validated_data.get('title', instance.title)
#     instance.description      = validated_data.get('description', instance.description)
#     instance.description      = validated_data.get('description', instance.description)
#     instance.body             = validated_data.get('body', instance.body)
#     instance.location         = validated_data.get('location', instance.location)
#     instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#     instance.active           = validated_data.get('active', instance.active)
#     instance.save()
#     return instance

#   def validate(self, data):
#     """ check the description and title are different """
#     if data["title"] == data["description"]:
#       raise serializers.ValidationError("Title and Description must be different from one another")
#     return data

#   def validate_title(self, value):
#     if len(value) < 60:
#       raise serializers.ValidationError("The Title has to be at least 60 characters long")
#     return value
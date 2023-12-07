from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from jobs.models import Job



class JobSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Job
    # exclude = ("id",)
    fields = "__all__" # we want all the fields of our model
    # fields = ("company_name", "job_title", "job_description")
  
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

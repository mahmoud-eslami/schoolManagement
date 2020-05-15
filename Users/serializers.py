from rest_framework import serializers

class FindIdSerilizer(serializers.Serializer):
    user_id = serializers.CharField(max_length=5)

class User(serializers.Serializer):
    id = serializers.CharField(max_length=5)
    username = serializers.CharField(max_length=5)
    first_name = serializers.CharField(max_length=5)
    last_name = serializers.CharField(max_length=5)
    email = serializers.CharField(max_length=5)
    date_joined = serializers.DateTimeField()

class UserProfile(serializers.Serializer):
    user_id = serializers.CharField()
    role = serializers.CharField()
    uuid = serializers.CharField()

class UserDoc(serializers.Serializer):
    userPhoto = serializers.ImageField()
    nationalCardPhoto = serializers.ImageField()
    user_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    home_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    address = serializers.CharField(max_length=250,allow_null=True,allow_blank=False)
    zipCode = serializers.CharField(max_length=20,allow_blank=False,allow_null=True)
    personalCode = serializers.CharField(max_length=20,allow_null=True,allow_blank=True)
    nationalCode = serializers.CharField(max_length=20,allow_blank=False,allow_null=True)
    father_nationalCode = serializers.CharField(max_length=20,allow_blank=False,allow_null=True)
    father_name = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    father_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    father_jobName = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    father_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=False)
    father_job_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    mother_nationalCode = serializers.CharField(max_length=20,allow_blank=False,allow_null=True)
    mother_name = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    mother_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    mother_jobName = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    mother_jobAddress = serializers.CharField(max_length=250,allow_null=True,allow_blank=False)
    mother_job_pNum = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    citizen_Num = serializers.CharField(max_length=40,allow_blank=True,allow_null=True)
    date_of_birth = serializers.DateTimeField()
    place_of_birth = serializers.CharField(max_length=40,allow_blank=False,allow_null=True)
    citizen = serializers.CharField(max_length=1)
    gender = serializers.CharField(max_length=1)
    section = serializers.CharField(max_length=1)

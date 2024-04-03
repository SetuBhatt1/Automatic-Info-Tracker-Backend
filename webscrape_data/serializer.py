from rest_framework import serializers
from .models import Vendor, GirlsHostel, BoysHostel, GirlsPg, BoysPg, Tiffin, Student, Review


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class GirlsHostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GirlsHostel
        fields = '__all__'


class BoysHostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoysHostel
        fields = '__all__'


class GirlsPgSerializer(serializers.ModelSerializer):
    class Meta:
        model = GirlsPg
        fields = '__all__'


class BoysPgSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoysPg
        fields = '__all__'


class TiffinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tiffin
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id', 'experience', 'rating', 'type', 'service_name'

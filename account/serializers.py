from rest_framework import serializers

from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=4, required=True)

    class Meta: 
        model = User
        fields = ('email', 'password', 'password_confirm', 'first_name', 'last_name', 'phone')
    
    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password_confirm')
        if p1 != p2:
            raise serializers.ValidationError("Passwords not match")
        return attrs
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with email already exists")
        return email

    def validate_phone(self, phone):
        if len(phone) > 13:
            raise serializers.ValidationError("The number should be max 13 digits")
        return phone
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
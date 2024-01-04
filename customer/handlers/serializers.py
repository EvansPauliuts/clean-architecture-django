from rest_framework import serializers
from customer.models import Customer


class CustomerBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
        )


class CustomerCreateSerializer(CustomerBaseSerializer):
    ...


class CustomerPutOrPatchSerializer(CustomerBaseSerializer):
    ...


class CustomerDetailSerializer(CustomerBaseSerializer):
    ...


class CustomerListSerializer(CustomerBaseSerializer):
    class Meta:
        model = Customer
        fields = CustomerBaseSerializer.Meta.fields + ('id',)

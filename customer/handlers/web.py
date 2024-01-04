from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CustomerCreateSerializer
from customer.domain.entities import Customer as CustomerEntity
from customer.repository.customer import CustomerRepository
from customer.use_cases.customer import CustomerUseCase


class CustomerAPIView(APIView):
    def post(self, request):
        customer_serializer = CustomerCreateSerializer(data=request.data)

        if not customer_serializer.is_valid():
            return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        customer_entity = CustomerEntity(**customer_serializer.validated_data)
        customer_repo = CustomerRepository()
        customer = CustomerUseCase(customer_repo).insert(customer_entity)

        return Response(customer.dict(), status=status.HTTP_201_CREATED)

    def put(self, request, customer_id):
        customer_repo = CustomerRepository()
        customer = CustomerUseCase(customer_repo).get_by_id(customer_id)

        if not customer:
            return Response(
                {'message': 'Customer with that Id Doesnot exist'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            customer_serializer = CustomerCreateSerializer(data=request.data)

            if not customer_serializer.is_valid():
                return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            customer_entity = CustomerEntity(**customer_serializer.validated_data)
            customer_entity.id = customer.id
            customer_repo = CustomerRepository()
            customer = CustomerUseCase(customer_repo).update(customer_entity)

            return Response(customer.dict(), status=status.HTTP_200_OK)

    def get(self, request, customer_id=None):
        customer_repo = CustomerRepository()

        if not customer_id:
            if customers := CustomerUseCase(customer_repo).list():
                customers_dict = [customer.__dict__ for customer in customers]
            else:
                customers_dict = {}
            return Response(
                {
                    'message': customers_dict,
                },
                status=status.HTTP_200_OK,
            )
        else:
            if customer := CustomerUseCase(customer_repo).get_by_id(customer_id):
                return Response(customer.dict(), status=status.HTTP_200_OK)
            else:
                return Response(
                    {'message': 'Customer with that Id DoesNot exist'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

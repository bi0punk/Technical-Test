


#from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Merchant, Keyword, Transaction
from .serializers import CategorySerializer, MerchantSerializer, KeywordSerializer, TransactionSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.shortcuts import render



@extend_schema_view(
    list=extend_schema(
        description='Retrieve a list of all categories.'
    ),
    retrieve=extend_schema(
        description='Retrieve a specific category by its ID.'
    ),
    create=extend_schema(
        description='Create a new category.'
    ),
    update=extend_schema(
        description='Update an existing category.'
    ),
    partial_update=extend_schema(
        description='Partially update an existing category.'
    ),
    destroy=extend_schema(
        description='Delete an existing category.'
    )
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['post'])
    def enrich(self, request):
        transactions = request.data.get('transactions', [])
        enriched_transactions = []
        for tx in transactions:
            tx_description = tx.get('description', '').lower()
            tx_category = None
            tx_merchant = None

            keywords = Keyword.objects.filter(keyword__icontains=tx_description)
            if keywords.exists():
                keyword = keywords.first()
                tx_merchant = keyword.merchant
                tx_category = tx_merchant.category

            if tx_category is None:
                tx_category = Category.objects.filter(type='income' if float(tx['amount']) > 0 else 'expense').first()

            enriched_transactions.append({
                'id': tx['id'],
                'description': tx['description'],
                'amount': tx['amount'],
                'date': tx['date'],
                'category': CategorySerializer(tx_category).data if tx_category else None,
                'merchant': MerchantSerializer(tx_merchant).data if tx_merchant else None,
            })

        return Response({
            'total_transactions': len(transactions),
            'enriched_transactions': enriched_transactions,
            'categorization_rate': sum(1 for tx in enriched_transactions if tx['category']) / len(enriched_transactions) * 100,
            'merchant_identification_rate': sum(1 for tx in enriched_transactions if tx['merchant']) / len(enriched_transactions) * 100,
        }, status=status.HTTP_200_OK)




def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

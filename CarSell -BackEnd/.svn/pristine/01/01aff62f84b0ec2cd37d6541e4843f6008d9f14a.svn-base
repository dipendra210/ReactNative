import graphene
from graphene_django.types import DjangoObjectType

from .models import Category, SellingBrandsCategory


# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category


# class SellingBrandsCategoryType(DjangoObjectType):
#     class Meta:
#         model = SellingBrandsCategory



# class Query(object):
#     all_categories = graphene.List(CategoryType)
#     all_brands = graphene.List(SellingBrandsCategoryType)

#     def resolve_all_categories(self, info, **kwargs):
#         return Category.objects.all()

#     def resolve_all_brands(self, info, **kwargs):
#         # We can easily optimize query count in the resolve method
#         return SellingBrandsCategory.objects.select_related('brands').all()



# from graphene import relay, ObjectType
# from graphene_django import DjangoObjectType
# from graphene_django.filter import DjangoFilterConnectionField

# from .models import Category, SellingBrandsCategory


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
# class CategoryNode(DjangoObjectType):
#     class Meta:
#         model = Category
#         filter_fields = {
#             'name': ['exact', 'icontains', 'istartswith'],
#         }
#         interfaces = (relay.Node, )


# class SellingBrandsNode(DjangoObjectType):
#     class Meta:
#         model = SellingBrandsCategory
        # Allow for some more advanced filtering here
#         filter_fields = {
#             'name': ['exact', 'icontains', 'istartswith'],
            
#             'category': ['exact'],
#             'category__name': ['exact'],
#         }
#         interfaces = (relay.Node, )


# class Query(object):
#     category = relay.Node.Field(CategoryNode)
#     all_categories = DjangoFilterConnectionField(CategoryNode)

#     brand = relay.Node.Field(SellingBrandsNode)
#     all_brands = DjangoFilterConnectionField(SellingBrandsNode)
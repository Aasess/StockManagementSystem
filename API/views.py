from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Vendor,Item,Stock,Sale,Category
from .serializers import VendorSerializer,ItemSerializer,StockSerializer,SaleSerializer,CategorySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class VendorViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self,request):
        vendors = Vendor.objects.all()
        #serialize them to json
        serializer = VendorSerializer(vendors,many = True, context = {"request":request})
        #return json response
        response_dict = {
            "error": False,
            "message": "All vendor list data",
            "data": serializer.data
        }
        return Response(response_dict)


    def create(self,request):
        try:
            serializer = VendorSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                response_dict = {
                    "error": False,
                    "message": "new vendor added sucessfully!!!"
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! New vendor cannot be added."
            }
        
        return Response(response_dict)


    def update(self,request,pk):
        try:
            vendor = Vendor.objects.get(id=pk)
            serializer = VendorSerializer(vendor,data = request.data)
            if serializer.is_valid():
                serializer.save()
                response_dict = {
                    "error": False,
                    "message": "vendor updated sucessfully!!!"
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! Vendor cannot be updated."
            }
        
        return Response(response_dict)

    def delete(self,request,pk):
        try:
            vendor = Vendor.objects.get(id=pk)
            vendor.delete()
            response_dict = {
                    "error": False,
                    "message": "vendor deleted sucessfully!!!"
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! Vendor cannot be deleted."
            }
        
        return Response(response_dict)


# vendor_list = VendorViewSet.as_view({"get":"list"})
# vendor_create = VendorViewSet.as_view({"post":"create"})
# vendor_update = VendorViewSet.as_view({"put":"update"})
# vendor_delete = VendorViewSet.as_view({"delete":"delete"})

class CategoryViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self,request):
        categories = Category.objects.all()
        #serialize them to json
        serializer = CategorySerializer(categories,many = True, context = {"request":request})
        #return json response
        response_dict = {
            "error": False,
            "message": "All item list data",
            "data": serializer.data
        }
        return Response(response_dict)

class ItemViewSet(viewsets.ViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self,request):
        items = Item.objects.all()
        #serialize them to json
        serializer = ItemSerializer(items,many = True, context = {"request":request})
        #return json response
        response_dict = {
            "error": False,
            "message": "All item list data",
            "data": serializer.data
        }
        return Response(response_dict)


    def retrieve(self,request,pk):
        try:
            item = Item.objects.get(id=pk)
            #serialize them to json
            serializer = ItemSerializer(item,context = {"request":request})
            response_dict = {
                    "error": False,
                    "message": "item found sucessfully!!!",
                    "data": serializer.data
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! item not found."
            }
        
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = ItemSerializer(data = request.data)
            print(serializer)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {
                    "error": False,
                    "message": "item added sucessfully!!!"
            }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! item cannot be added."
            }
        return Response(response_dict)

    def update(self,request,pk):
        try:
            item = Item.objects.get(id=pk)
            serializer = ItemSerializer(item,data = request.data)
            if serializer.is_valid():
                serializer.save()
                response_dict = {
                    "error": False,
                    "message": "item updated sucessfully!!!"
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! Item cannot be updated."
            }
        
        return Response(response_dict)

    def delete(self,request,pk):
        try:
            item = Item.objects.get(id=pk)
            item.delete()
            response_dict = {
                    "error": False,
                    "message": "item deleted sucessfully!!!"
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! Item cannot be deleted."
            }
        
        return Response(response_dict)




class StockViewSet(viewsets.ViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self,request):
        stocks = Stock.objects.all()
        #serialize them to json
        serializer = StockSerializer(stocks,many = True, context = {"request":request})
        #return json response
        response_dict = {
            "error": False,
            "message": "All stocks list data",
            "data": serializer.data
        }
        return Response(response_dict)

    def retrieve(self,request,pk):
        try:
            stock = Stock.objects.get(id=pk)
            #serialize them to json
            serializer = StockSerializer(stock,context = {"request":request})
            response_dict = {
                    "error": False,
                    "message": "stock item found sucessfully!!!",
                    "data": serializer.data
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! stock item not found."
            }
        
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = StockSerializer(data = request.data)
            print(serializer)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {
                    "error": False,
                    "message": "stock item added sucessfully!!!"
            }
        except:
            response_dict = {
                "error": True,
                "message": "Error!!stock item cannot be added."
            }
        return Response(response_dict)

    def update(self,request,pk):
        try:
            stock = Stock.objects.get(id=pk)
            serializer = StockSerializer(stock,data = request.data)
            if serializer.is_valid():
                serializer.save()
                response_dict = {
                    "error": False,
                    "message": "stock item updated sucessfully!!!"
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! stock item cannot be updated."
            }
        
        return Response(response_dict)

    def delete(self,request,pk):
        try:
            stock = Stock.objects.get(id=pk)
            stock.delete()
            response_dict = {
                    "error": False,
                    "message": "stock item deleted sucessfully!!!"
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!!stock item cannot be deleted."
            }
        
        return Response(response_dict)




class SaleViewSet(viewsets.ViewSet): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self,request):
        sales = Sale.objects.all()
        #serialize them to json
        serializer = SaleSerializer(sales,many = True, context = {"request":request})
        #return json response
        response_dict = {
            "error": False,
            "message": "All sales list data",
            "data": serializer.data
        }
        return Response(response_dict)

    def retrieve(self,request,pk):
        try:
            sale = Sale.objects.get(id=pk)
            #serialize them to json
            serializer = SaleSerializer(sale,context = {"request":request})
            response_dict = {
                    "error": False,
                    "message": "sold item found sucessfully!!!",
                    "data": serializer.data
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! sold item not found."
            }
        
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = SaleSerializer(data = request.data)
            print(serializer)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {
                    "error": False,
                    "message": "sold item added sucessfully!!!"
            }
        except:
            response_dict = {
                "error": True,
                "message": "Error!!sold item cannot be added."
            }
        return Response(response_dict)

    def update(self,request,pk):
        try:
            sale = Sale.objects.get(id=pk)
            serializer = SaleSerializer(sale,data = request.data)
            if serializer.is_valid():
                serializer.save()
                response_dict = {
                    "error": False,
                    "message": "sold item updated sucessfully!!!"
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!! sold item cannot be updated."
            }
        
        return Response(response_dict)

    def delete(self,request,pk):
        try:
            sale = Sale.objects.get(id=pk)
            sale.delete()
            response_dict = {
                    "error": False,
                    "message": "sold item deleted sucessfully!!!"
                }
        except:
            response_dict = {
                "error": True,
                "message": "Error!!sold item cannot be deleted."
            }
        
        return Response(response_dict)




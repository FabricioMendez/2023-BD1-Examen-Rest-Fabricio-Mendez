from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Customers, Suppliers, Categories, Products, Orders, Orderdetails, Employees

class SerializadorPadre(ModelSerializer):
    class Meta:
        fields = '__all__'

class CustomerSerializer(SerializadorPadre):
    class Meta:
        model = Customers
        fields = '__all__'

class SupplierSerializer(SerializadorPadre):
    class Meta:
        model = Suppliers
        fields = '__all__'

class CategorieSerializer (SerializadorPadre):
   class Meta:
      model = Categories
      fields = '__all__'

class ProductSerializer (SerializadorPadre):
   supplierid = SupplierSerializer(many=False,required=False)
   categoryid = CategorieSerializer(many=False, required=False)

   class Meta:
      model = Products
      fields = '__all__'

class OrderdetailSerializer (SerializadorPadre):
   class Meta:
      model = Orderdetails
      fields = '__all__'

class OrderSerializer(SerializadorPadre):
   class Meta:
      model = Orders
      fields = '__all__'

class EmployeeSerializer (SerializadorPadre):
   class Meta:
      model = Employees
      fields = '__all__'

class Punto1Serializer(serializers.Serializer):
   id = serializers.IntegerField()
   apellido = serializers.CharField()
   nombre = serializers.CharField()
   birthdate = serializers.DateTimeField()


#class Punto1Serializer(serializers.Serializer):
#    id = serializers.IntegerField()
#    apellido = serializers.CharField(max_length=50)
#    descripcion = CondicionIvaSerializer(many=False)
#    telefono = serializers.IntegerField()
#    nuevoTelefono = serializers.IntegerField()
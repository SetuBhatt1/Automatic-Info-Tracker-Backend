from .models import Vendor, GirlsHostel, BoysHostel, GirlsPg, BoysPg, Tiffin, Student, Review
from .serializer import VendorSerializer, GirlsHostelSerializer, BoysHostelSerializer, GirlsPgSerializer, \
    StudentSerializer, \
    BoysPgSerializer, TiffinSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework.test import APIClient

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def apply_permissions(view_func):
    return permission_classes([IsAuthenticatedOrReadOnly])(view_func)


class BaseAPIView(APIView):
    model = None
    serializer_class = None

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None

    @apply_permissions
    @api_view(['GET'])
    def get(self, request, pk=None):
        if request.method != 'GET':
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if pk:
            instance = self.get_object(pk)
            if not instance:
                return Response({'error': f'{self.model.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(instance)
            return Response(serializer.data)
        else:
            queryset = self.model.objects.all()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)

    @apply_permissions
    @api_view(['POST'])
    def post(self, request):
        if request.method != 'POST':
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @apply_permissions
    @api_view(['PUT'])
    def put(self, request, pk):
        if request.method != 'PUT':
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        instance = self.get_object(pk)
        if not instance:
            return Response({'error': f'{self.model.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @apply_permissions
    @api_view(['DELETE'])
    def delete(self, request, pk):
        if request.method != 'DELETE':
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        instance = self.get_object(pk)
        if not instance:
            return Response({'error': f'{self.model.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({'message': f'{self.model.__name__} deleted successfully'})


class VendorListCreateAPIView(APIView):
    # def get(self, request):
    #     vendors = Vendor.objects.all()
    #     serializer = VendorSerializer(vendors, many=True)
    #     return Response(serializer.data)
    @staticmethod
    def post(request):
        print('hi')
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            print('saving vendor')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_object(pk):
        try:
            return Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return None

    def get(self, request, pk):
        vendor = self.get_object(pk)
        if vendor:
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        vendor = self.get_object(pk)
        if vendor:
            serializer = VendorSerializer(vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        vendor = self.get_object(pk)
        if vendor:
            vendor.delete()
            return Response({'message': 'Vendor deleted successfully'})
        return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)


class GirlsHostelListCreateAPIView(APIView):
    @staticmethod
    def get(request):
        hostels = GirlsHostel.objects.all()
        serializer = GirlsHostelSerializer(hostels, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = GirlsHostelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GirlsHostelRetrieveUpdateDestroyAPIView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return GirlsHostel.objects.get(pk=pk)
        except GirlsHostel.DoesNotExist:
            return None

    def get(self, request, pk):
        hostel = self.get_object(pk)
        if hostel:
            serializer = GirlsHostelSerializer(hostel)
            return Response(serializer.data)
        return Response({'error': 'Girls hostel not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        hostel = self.get_object(pk)
        if hostel:
            serializer = GirlsHostelSerializer(hostel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Girls hostel not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        hostel = self.get_object(pk)
        if hostel:
            hostel.delete()
            return Response({'message': 'Girls hostel deleted successfully'})
        return Response({'error': 'Girls hostel not found'}, status=status.HTTP_404_NOT_FOUND)


class BoysHostelListCreateAPIView(APIView):
    @staticmethod
    def get(request):
        hostels = BoysHostel.objects.all()
        serializer = BoysHostelSerializer(hostels, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = BoysHostelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoysHostelRetrieveUpdateDestroyAPIView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return BoysHostel.objects.get(pk=pk)
        except BoysHostel.DoesNotExist:
            return None

    def get(self, request, pk):
        hostel = self.get_object(pk)
        if hostel:
            serializer = BoysHostelSerializer(hostel)
            return Response(serializer.data)
        return Response({'error': 'Boys hostel not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        hostel = self.get_object(pk)
        if hostel:
            serializer = BoysHostelSerializer(hostel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Boys hostel not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        hostel = self.get_object(pk)
        if hostel:
            hostel.delete()
            return Response({'message': 'Boys hostel deleted successfully'})
        return Response({'error': 'Boys hostel not found'}, status=status.HTTP_404_NOT_FOUND)


class GirlsPgListCreateAPIView(APIView):
    @staticmethod
    def get(request):
        pgs = GirlsPg.objects.all()
        serializer = GirlsPgSerializer(pgs, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = GirlsPgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GirlsPgRetrieveUpdateDestroyAPIView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return GirlsPg.objects.get(pk=pk)
        except GirlsPg.DoesNotExist:
            return None

    def get(self, request, pk):
        pg = self.get_object(pk)
        if pg:
            serializer = GirlsPgSerializer(pg)
            return Response(serializer.data)
        return Response({'error': 'Girls PG not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        pg = self.get_object(pk)
        if pg:
            serializer = GirlsPgSerializer(pg, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Girls PG not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        pg = self.get_object(pk)
        if pg:
            pg.delete()
            return Response({'message': 'Girls PG deleted successfully'})
        return Response({'error': 'Girls PG not found'}, status=status.HTTP_404_NOT_FOUND)


class BoysPgListCreateAPIView(APIView):
    @staticmethod
    def get(request):
        pgs = BoysPg.objects.all()
        serializer = BoysPgSerializer(pgs, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = BoysPgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoysPgRetrieveUpdateDestroyAPIView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return BoysPg.objects.get(pk=pk)
        except BoysPg.DoesNotExist:
            return None

    def get(self, request, pk):
        pg = self.get_object(pk)
        if pg:
            serializer = BoysPgSerializer(pg)
            return Response(serializer.data)
        return Response({'error': 'Boys PG not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        pg = self.get_object(pk)
        if pg:
            serializer = BoysPgSerializer(pg, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Boys PG not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        pg = self.get_object(pk)
        if pg:
            pg.delete()
            return Response({'message': 'Boys PG deleted successfully'})
        return Response({'error': 'Boys PG not found'}, status=status.HTTP_404_NOT_FOUND)


class TiffinListCreateAPIView(APIView):
    @staticmethod
    def get(request):
        tiffins = Tiffin.objects.all()
        serializer = TiffinSerializer(tiffins, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = TiffinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TiffinRetrieveUpdateDestroyAPIView(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Tiffin.objects.get(pk=pk)
        except Tiffin.DoesNotExist:
            return None

    def get(self, request, pk):
        tiffin = self.get_object(pk)
        if tiffin:
            serializer = TiffinSerializer(tiffin)
            return Response(serializer.data)
        return Response({'error': 'Tiffin not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        tiffin = self.get_object(pk)
        if tiffin:
            serializer = TiffinSerializer(tiffin, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Tiffin not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        tiffin = self.get_object(pk)
        if tiffin:
            tiffin.delete()
            return Response({'message': 'Tiffin deleted successfully'})
        return Response({'error': 'Tiffin not found'}, status=status.HTTP_404_NOT_FOUND)




# Register Business View
class RegisterBusinessView(APIView):
    @staticmethod
    def post(request):
        registration_form_data = request.data
        vendor_serializer = VendorSerializer(data=registration_form_data)
        if vendor_serializer.is_valid():
            vendor = vendor_serializer.save()

            business_type = registration_form_data.get('type_of_business')
            if business_type == 'H':
                gender_type = registration_form_data.get('gender_type')
                if gender_type == 'G':
                    GirlsHostelSerializer(data=registration_form_data).save(vid=vendor)
                elif gender_type == 'B':
                    BoysHostelSerializer(data=registration_form_data).save(vid=vendor)
            elif business_type == 'Pg':
                pass
            elif business_type == 'T':
                TiffinSerializer(data=registration_form_data).save(vid=vendor)

            return Response({'message': 'Business registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(vendor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Business Details View
class BusinessDetailsView(APIView):
    @staticmethod
    def get(request, vendor_id):
        # Logic to fetch and return business details
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def put(request, vendor_id):
        # Logic to update business details
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            serializer = VendorSerializer(vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)


class ReviewListCreateAPIView(BaseAPIView):
    model = Review
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyAPIView(BaseAPIView):
    model = Review
    serializer_class = ReviewSerializer

    def get(self, request, pk=None):  # Add `pk` parameter here
        review = self.get_object(pk)
        if review:
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)


class RatingAndReviewsView(APIView):
    @staticmethod
    def get(request, vendor_id):
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            rating = vendor.rating
            reviews = Review.objects.filter(vendor=vendor)
            serializer = ReviewSerializer(reviews, many=True)
            return Response({'rating': rating, 'reviews': serializer.data}, status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)


class StudentListCreateAPIView(BaseAPIView):
    model = Student
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyAPIView(BaseAPIView):
    model = Student
    serializer_class = StudentSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/dashboard/',
        '/api/register/',
        '/api/business/<int:vendor_id>/',
        '/api/business/<int:vendor_id>/rating-reviews/',
    ]
    return Response({'routes': routes}, status=status.HTTP_200_OK)


client = APIClient()


@api_view(['GET'])
def test_dashboard_endpoint(request):
    # Test endpoint for dashboard view
    if request.method == 'GET':
        # Perform GET request to dashboard view
        response = client.get('/dashboard/')
        return JsonResponse({'response': response.data})


@api_view(['POST'])
def test_register_business_endpoint(request):
    # Test endpoint for register business view
    if request.method == 'POST':
        # Perform POST request to register business view with form data
        response = client.post('/register/', {'data': 'form_data'})
        return JsonResponse({'response': response.data})


@api_view(['GET'])
def test_business_details_endpoint(request, vendor_id):
    # Test endpoint for business details view
    if request.method == 'GET':
        # Perform GET request to business details view for a specific vendor
        response = client.get(f'/business/{vendor_id}/')
        return JsonResponse({'response': response.data})


@api_view(['PUT'])
def test_update_business_details_endpoint(request, vendor_id):
    # Test endpoint for updating business details
    if request.method == 'PUT':
        # Perform PUT request to update business details for a specific vendor
        response = client.put(f'/business/{vendor_id}/')
        return JsonResponse({'response': response.data})


@api_view(['GET'])
def test_rating_and_reviews_endpoint(request, vendor_id):
    # Test endpoint for rating and reviews view
    if request.method == 'GET':
        # Perform GET request to rating and reviews view for a specific vendor
        response = client.get(f'/business/{vendor_id}/rating-reviews/')
        return JsonResponse({'response': response.data})

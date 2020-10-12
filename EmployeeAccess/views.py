from .models import Employee                                     # import Employee table from models.py file(database)
from .serializers import EmployeeSerializer, AccessSerializer    # import serialize class
from rest_framework.response import Response
from rest_framework import status
from .classifier import Classifier                                # import Classifier class which predict access
from rest_framework.views import APIView


# predict access status with serializer using class based API views
class EmployeeAPIView(APIView):

    def post(self, request):  # define post method
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():                    # check serialized data is valid or not
            predict = Classifier(request.data)         # Create object for class classifier
            predict = predict.classify()                # return  access status (approved or denied)
            serializer_access = AccessSerializer(data=predict)  # serializing predicated output
            if serializer_access.is_valid():                    # check serializer is valid or not
                return Response(serializer_access.data)
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)  # 400 bad request response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auction_api.models import Bid
from auction_api.serializers.bid import BidSerializer
from auction_api.services.email import send_new_bid_notification


class BidAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BidSerializer
    queryset = Bid.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        bid_instance = serializer.save()
        send_new_bid_notification(bid_instance=bid_instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name="all", in_="query", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter(
                name="only_active", in_="query", type=openapi.TYPE_BOOLEAN
            ),
            openapi.Parameter(
                name="only_closed", in_="query", type=openapi.TYPE_BOOLEAN
            ),
        ]
    )
    def get(self, request):
        if len(request.query_params) > 1:
            return Response(
                "Using more than one parameter is not allowed",
                status=status.HTTP_400_BAD_REQUEST,
            )

        if request.query_params.get("only_active") == "true":
            self.queryset = self.get_queryset().is_active()
        elif request.query_params.get("only_closed") == "true":
            self.queryset = self.get_queryset().is_closed()

        return Response(
            self.serializer_class(instance=self.get_queryset(), many=True).data
        )
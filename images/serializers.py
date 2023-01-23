from rest_framework import serializers

from images.models import Images
from images.models import Stock6Sign202212


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        # fields = '__all__'
        fields = ('id', 'Url', 'CreateDate')
        
class Stock6Sign202212Serializer(serializers.ModelSerializer):
    class Meta:

        model = Stock6Sign202212
        # fields = '__all__'
        fields = ('id', 'cStockID', 'cStockName', 'cNewestSeason', 'cNewestRev', 'cSign1' ,'cSign2' ,'cSign3' ,'cSign4' ,'cSign5' ,'cSign6' ,'cAverageScore' ,'cLossGain' ,'CreateDate')


    
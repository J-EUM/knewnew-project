from rest_framework import serializers

from app.user.models import User
from app.review.models import Review, ReviewImage


class UserSimpleSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "profile_image", "nickname", "tags"]

    def get_tags(self, obj):
        return obj.tag.name


class ImageSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ["order", "url"]


class ReviewDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    retailer = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    # reviewimage_set = ImageSimpleSerializer(many=True)
    user = UserSimpleSerializer()

    # user 정보를 dict 형태로 가져올 때,
    # 1. nested serializer
    # 2. serializerMethodField사용 def 정의 할 때 또 다른 serializer로 정의
    # 3. dict 만들어서 보내주기

    class Meta:
        model = Review
        fields = [
            "user",
            "images",
            "id",
            "created_at",
            "product_name",
            "description",
            "retailer",
            "quotation_count",
            "like_count",
            "bookmark_count",
            "share_count",
            "comment_count",
            "is_updated",
            "is_active",
        ]

    def get_product_name(self, obj):
        if obj.product is not None:
            return obj.product.name
        return "None"

    def get_retailer(self, obj):
        return obj.retailer.name

    def get_images(self, obj):
        images = obj.reviewimage_set.all()
        return ImageSimpleSerializer(instance=images, many=True).data

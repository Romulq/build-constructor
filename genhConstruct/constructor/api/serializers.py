from rest_framework import serializers

from ..models import (TypeArtifact, Artifact, ArtifactBuild,
                      TypeWeapon, Weapon, WeaponBuild,
                      Character, CharacterBuild,
                      Build
                      )


class TypeArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeArtifact
        fields = '__all__'


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = '__all__'


class ArtifactBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactBuild
        fields = '__all__'


class TypeWeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeWeapon
        fields = '__all__'


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class WeaponBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponBuild
        fields = ('username',)


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class CharacterBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterBuild
        fields = '__all__'


class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = '__all__'


# class CommentListRetrieveSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#
#     class Meta:
#         model = Comment
#         fields = '__all__'


# class RecipeListRetrieveSerializer(serializers.ModelSerializer):
#     kitchen = KitchenSerializer()
#     category = CategorySerializer()
#
#     stages = StageSerializer(many=True)
#     ingredients = IngredientSerializer(many=True)
#     comments = CommentListRetrieveSerializer(many=True)
#
#     class Meta:
#         model = Recipe
#         fields = '__all__'

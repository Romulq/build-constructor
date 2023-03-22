from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import (TypeArtifactSerializer, ArtifactSerializer, ArtifactBuildSerializer,
                          TypeWeaponSerializer, WeaponSerializer, WeaponBuildSerializer,
                          CharacterSerializer, CharacterBuildSerializer,
                          BuildSerializer, ElementSerializer)

from ..models import (TypeArtifact, Artifact, ArtifactBuild,
                      TypeWeapon, Weapon, WeaponBuild,
                      Character, CharacterBuild,
                      Build, Element)


class ElementViewSet(viewsets.ModelViewSet):

    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class TypeArtifactViewSet(viewsets.ModelViewSet):

    queryset = TypeArtifact.objects.all()
    serializer_class = TypeArtifactSerializer


class ArtifactViewSet(viewsets.ModelViewSet):

    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer


class ArtifactBuildViewSet(viewsets.ModelViewSet):

    queryset = ArtifactBuild.objects.all()
    serializer_class = ArtifactBuildSerializer


class TypeWeaponViewSet(viewsets.ModelViewSet):

    queryset = TypeWeapon.objects.all()
    serializer_class = TypeWeaponSerializer


class WeaponViewSet(viewsets.ModelViewSet):

    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer


class WeaponBuildViewSet(viewsets.ModelViewSet):

    queryset = WeaponBuild.objects.all()
    serializer_class = WeaponBuildSerializer


@action(detail=True, methods=['get'])
@permission_classes([AllowAny])
class CharacterViewSet(viewsets.ModelViewSet):

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterBuildViewSet(viewsets.ModelViewSet):

    queryset = CharacterBuild.objects.all()
    serializer_class = CharacterBuildSerializer


class BuildViewSet(viewsets.ModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer


# class RecipeViewSet(viewsets.ModelViewSet):
#
#     queryset = Weapon.objects.all()
#     serializer_class = WeaponSerializer
#
#     action_to = {
#         "list": RecipeListRetrieveSerializer,
#         "retrieve": RecipeListRetrieveSerializer
#     }
#
#     def get_serializer_class(self):
#         return self.action_to.get(self.action, self.serializer_class)
#
#
# class CommentViewSet(viewsets.ModelViewSet):
#
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#     action_to = {
#         "list": CommentListRetrieveSerializer,
#         "retrieve": CommentListRetrieveSerializer
#     }
#
#     def get_serializer_class(self):
#         return self.action_to.get(self.action, self.serializer_class)

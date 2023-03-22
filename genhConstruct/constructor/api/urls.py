from rest_framework import routers

from .views import (TypeArtifactViewSet, ArtifactViewSet, ArtifactBuildViewSet,
                    TypeWeaponViewSet, WeaponViewSet, WeaponBuildViewSet,
                    CharacterViewSet, CharacterBuildViewSet,
                    BuildViewSet, ElementViewSet)

router = routers.SimpleRouter()
router.register('typeArtifact', TypeArtifactViewSet, basename='typeArtifact')
router.register('artifact', ArtifactViewSet, basename='artifact')
router.register('artifactBuild', ArtifactBuildViewSet, basename='artifactBuild')

router.register('typeWeapon', TypeWeaponViewSet, basename='typeWeapon')
router.register('weapon', WeaponViewSet, basename='weapon')
router.register('weaponBuild', WeaponBuildViewSet, basename='weaponBuild')

router.register('character', CharacterViewSet, basename='character')
router.register('characterBuild', CharacterBuildViewSet, basename='characterBuild')

router.register('build', BuildViewSet, basename='build')
router.register('element', ElementViewSet, basename='element')

urlpatterns = []
urlpatterns += router.urls

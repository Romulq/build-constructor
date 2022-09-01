from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import (TypeArtifact, Artifact, ArtifactBuild,
                     TypeWeapon, Weapon, WeaponBuild,
                     Character, CharacterBuild,
                     Build, Element
                     )


@admin.register(TypeArtifact)
class TypeArtifactAdmin(admin.ModelAdmin):
    pass


@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    pass


@admin.register(ArtifactBuild)
class ArtifactBuildAdmin(admin.ModelAdmin):
    pass


@admin.register(TypeWeapon)
class TypeWeaponAdmin(admin.ModelAdmin):
    pass


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    pass


@admin.register(WeaponBuild)
class WeaponBuildAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(CharacterBuild)
class CharacterBuildAdmin(admin.ModelAdmin):
    pass


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    pass


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(User)
admin.site.unregister(Group)

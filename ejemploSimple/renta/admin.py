# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Actor, Address, Category, City, Country, Customer, Film, FilmActor, FilmCategory, FilmText, Inventory, Language, Payment, Rental, Staff, Store


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('actor_id', 'first_name', 'last_name', 'last_update')
    list_filter = ('last_update',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'address_id',
        'address',
        'address2',
        'district',
        'city',
        'postal_code',
        'phone',
        'last_update',
    )
    list_filter = ('city', 'last_update')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', 'last_update')
    list_filter = ('last_update',)
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'city', 'country', 'last_update')
    list_filter = ('country', 'last_update')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country', 'last_update')
    list_filter = ('last_update',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'customer_id',
        'store',
        'first_name',
        'last_name',
        'email',
        'address',
        'active',
        'create_date',
        'last_update',
    )
    list_filter = ('store', 'address', 'create_date', 'last_update')


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = (
        'film_id',
        'title',
        'description',
        'release_year',
        'language',
        'original_language',
        'rental_duration',
        'rental_rate',
        'length',
        'replacement_cost',
        'rating',
        'special_features',
        'last_update',
    )
    list_filter = ('language', 'original_language', 'last_update')


@admin.register(FilmActor)
class FilmActorAdmin(admin.ModelAdmin):
    list_display = ('actor', 'film', 'last_update')
    list_filter = ('actor', 'film', 'last_update')


@admin.register(FilmCategory)
class FilmCategoryAdmin(admin.ModelAdmin):
    list_display = ('film', 'category', 'last_update')
    list_filter = ('film', 'category', 'last_update')


@admin.register(FilmText)
class FilmTextAdmin(admin.ModelAdmin):
    list_display = ('film_id', 'title', 'description')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', 'film', 'store', 'last_update')
    list_filter = ('film', 'store', 'last_update')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language_id', 'name', 'last_update')
    list_filter = ('last_update',)
    search_fields = ('name',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'payment_id',
        'customer',
        'staff',
        'rental',
        'amount',
        'payment_date',
        'last_update',
    )
    list_filter = (
        'customer',
        'staff',
        'rental',
        'payment_date',
        'last_update',
    )


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = (
        'rental_id',
        'rental_date',
        'inventory',
        'customer',
        'return_date',
        'staff',
        'last_update',
    )
    list_filter = (
        'rental_date',
        'inventory',
        'customer',
        'return_date',
        'staff',
        'last_update',
    )


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'staff_id',
        'first_name',
        'last_name',
        'address',
        'picture',
        'email',
        'store',
        'active',
        'username',
        'password',
        'last_update',
    )
    list_filter = ('address', 'store', 'last_update')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'manager_staff', 'address', 'last_update')
    list_filter = ('manager_staff', 'address', 'last_update')
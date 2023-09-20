from django.db import models


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True,db_index=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        db_table = 'actor'


class Address(models.Model):
    address_id = models.AutoField(primary_key=True,db_index=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(blank=True, null=True,max_length=50)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City', on_delete=models.RESTRICT)
    postal_code = models.CharField(blank=True, null=True,max_length=10)
    phone = models.CharField(max_length=20)
    last_update = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.address}\n{self.address2}"

    class Meta:
        db_table = 'address'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True,db_index=True)
    name = models.CharField(max_length=25)
    last_update = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class City(models.Model):
    city_id = models.AutoField(primary_key=True,db_index=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.RESTRICT)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.city

    class Meta:
        db_table = 'city'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True,db_index=True)
    country = models.CharField(max_length=50)
    last_update = models.DateField(auto_now=True, blank=True, null=True)  # This field type is a guess.

    def __str__(self):
        return self.country

    class Meta:
        db_table = 'country'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True,db_index=True)
    store = models.ForeignKey('Store', on_delete=models.RESTRICT)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(blank=True, null=True,max_length=50)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    active = models.CharField(max_length=1)
    create_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


    class Meta:
        db_table = 'customer'


class Film(models.Model):
    film_id = models.AutoField(primary_key=True,db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    release_year = models.CharField(blank=True, null=True,max_length=4)
    language = models.ForeignKey('Language', on_delete=models.RESTRICT)
    original_language = models.ForeignKey('Language', on_delete=models.RESTRICT, related_name='film_original_language_set', blank=True, null=True)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    rating = models.CharField(blank=True, null=True,max_length=10)
    special_features = models.CharField(blank=True, null=True,max_length=100)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'film'


class FilmActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.RESTRICT)  # The composite primary key (actor_id, film_id) found, that is not supported. The first column is selected.
    film = models.ForeignKey(Film, on_delete=models.RESTRICT)
    last_update = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.actor.__str__()} en {self.film.__str__()}"

    class Meta:
        db_table = 'film_actor'


class FilmCategory(models.Model):
    film = models.OneToOneField(Film, on_delete=models.RESTRICT, primary_key=True)  # The composite primary key (film_id, category_id) found, that is not supported. The first column is selected.
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.film.__str__()} en {self.category.__str__()}"

    class Meta:
        db_table = 'film_category'


class FilmText(models.Model):
    film_id = models.AutoField(primary_key=True,db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'film_text'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True,db_index=True)
    film = models.ForeignKey(Film, on_delete=models.RESTRICT)
    store = models.ForeignKey('Store', on_delete=models.RESTRICT)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.film.__str__()
    
    class Meta:
        db_table = 'inventory'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True,db_index=True)
    name = models.CharField(max_length=20)
    last_update = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'language'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True,db_index=True)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    staff = models.ForeignKey('Staff', on_delete=models.RESTRICT)
    rental = models.ForeignKey('Rental', on_delete=models.RESTRICT, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    payment_date = models.DateField()  # This field type is a guess.
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return f"pago de {self.customer.__str__()}"

    class Meta:
        db_table = 'payment'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True,db_index=True)
    rental_date = models.DateField()  # This field type is a guess.
    inventory = models.ForeignKey(Inventory, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    return_date = models.DateField(blank=True, null=True)  # This field type is a guess.
    staff = models.ForeignKey('Staff', on_delete=models.RESTRICT)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return f"rento {self.customer.__str__()} {self.inventory.__str__()}"

    class Meta:
        unique_together = (('rental_date', 'inventory', 'customer'),)
        db_table = 'rental'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True,db_index=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    picture = models.BinaryField(blank=True, null=True)
    email = models.CharField(blank=True, null=True,max_length=50)
    store = models.ForeignKey('Store', on_delete=models.RESTRICT)
    active = models.SmallIntegerField()
    username = models.CharField(max_length=16)
    password = models.CharField(blank=True, null=True,max_length=40)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
    class Meta:
        db_table = 'staff'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True,db_index=True)
    manager_staff = models.ForeignKey(Staff, on_delete=models.RESTRICT,related_name='manager_staff_1')
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.manager_staff.__str__()}"
    
    class Meta:
        db_table = 'store'
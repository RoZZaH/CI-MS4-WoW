from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.text import slugify
from django_countries.fields import CountryField
from setfield import SetField


class Winery(TimeStampedModel):

    class Meta:
        verbose_name_plural = 'Wineries / Vineyards'

    brand = models.CharField("Winery Brand", max_length=155, blank=True)
    name = models.CharField("Winery", max_length=120, blank=False, unique=True)
    description = models.TextField("Description", blank=True)


    def __str__(self):
        return self.name


    def make_brand(self):
        return self.name.upper()


    def save(self, *args, **kwargs):
        if not self.brand:
            self.brand= self.make_brand()
        super(Winery, self).save(*args, **kwargs)


class Region(models.Model):
    name = models.CharField("Region", max_length=120)
    country = CountryField("Country of Origin", blank=False)
    locales = SetField(models.CharField(max_length=200), default=list, blank=True)

    def __str__(self):
        return self.name  + ", " + self.country.name


class Wine(TimeStampedModel):
    winery = models.ForeignKey(Winery, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField("Wine Name (Label not Winery)", max_length=120, blank=False)
    vintage = models.IntegerField("Vintage (Year)")
    grape_blend = models.CharField("Grape (Blend)", max_length=255)
    one_liner = models.TextField("One Line Description", blank=True)
    description = models.TextField("Description", blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    class Type(models.TextChoices):
        RED = "red", "Red"
        WHITE = "white", "White"
        ROSE = "rose", "Rosé"
        SPARKLING_WHITE = "sparkling white", "Sparkling White" 
        SPARKLING_ROSE = "sparkling rose", "Sparkling Rosé" 
        FORTIFIED = "fortified", "Fortified"
        DESSERT = "dessert", "Dessert"

    wtype = models.CharField("Red/White/Rose", max_length=60,
                            choices = Type.choices, default=Type.RED)
    

    class Style(models.TextChoices):
        ''' 
        style / taste of wine
        www.wine-searcher.com/styles
        '''
        UNSPECIFIED             =   "unspecified"               , "Unspecified"
        LIGHT_AND_PERFUMED      =   "light and perfumed"        , "Light and Perfumed"
        SAVORY_AND_CLASSIC      =   "savory and classic"        , "Savory and Classic"
        BOLD_AND_STRUCTURED     =   "bold and structured"       , "Bold and Structured"
        RICH_AND_INTENSE        =   "rich and intense"          , "Rich and Intense"
        AROMATIC_AND_FLORAL     =   "aromatic and floral"       , "Aromatic and Floral"
        GREEN_AND_FLINTY        =   "green and flinty"          , "Green and Flinty"
        TROPICAL_AND_BALANCED   =   "tropical and balanced"     , "Tropical and Balanced"
        BUTTERY_AND_COMPLEX     =   "buttery and complex"       , "Buttery and Complex"
        DRY_AND_NUTTY           =   "dry and nutty"             , "Dry and Nutty"
        CHOCOLATE_AND_CARAMEL   =   "chocolate and caramel"     , "Chocolate and Caramel"
        CARAMELIZED_AND_STICKY  =   "caramelized and sticky"    , "Caramelized and Sticky"
        RICH_AND_WARMING        =   "rich and warming"          , "Rich and Warming"
        LUSH_AND_BALANCED       =   "lush and balanced"         , "Lush and Balanced"
        CRISP_AND_DRY           =   "crisp and dry"             , "Crisp and Dry"
        RICH_AND_FRUITY         =   "rich and fruity"           , "Rich and Fruity"
        FRESH_AND_YOUTHFUL      =   "fresh and youthful"        , "Fresh and Youthful"
        COMPLEX_AND_TRADITIONAL =   "complex and traditional"   , "Complex and Traditional"
        BERRIES_AND_CREAM       =   "berries and cream"         , "Berries and Cream"
        SWEET_AND_SPRITZY       =   "sweet and spritzy"         , "Sweet and Spritzy"


    style = models.CharField("Style", max_length=60, 
                            choices=Style.choices, default=Style.UNSPECIFIED)

    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True)
   
    list_price = models.DecimalField(max_digits=6, decimal_places=2, default=999.99, blank=False)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    parker_points = models.IntegerField(blank=True, default=90)
    star_rating = models.DecimalField(max_digits=2, decimal_places=1, default=3.0, blank=True)
    alcohol_content = models.DecimalField(max_digits=3, decimal_places=1, default=14.0, blank=True)

    def make_slug(self):
        return '-'.join((slugify(self.winery), slugify(self.name), slugify(self.vintage)))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.make_slug()
        super(Wine, self).save(*args, **kwargs)

        # post_save for new specific locale
    def __str__(self):
        if self.slug:
            return self.slug.title()
        else:
            return self.make_slug()









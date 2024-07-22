# models.py
from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    firstname=models.CharField(max_length=30,blank=True)
    lastname=models.CharField(max_length=30,blank=True)
    phonenumber=models.IntegerField(max_length=30,null=True)
    address_line=models.CharField(max_length=30,blank=True)
    postcode=models.CharField(max_length=30,blank=True)
    email=models.EmailField(max_length=30,blank=True)
    country=models.CharField(max_length=30,blank=True)
    state_region=models.CharField(max_length=30,blank=True)
    pro_pic = models.ImageField(upload_to='profilepic/',default='profilepic/default.png')
    
    def __str__(self):
        return self.user.username
    
    def get_prof_image_url(self):
        if self.pro_pic:
            return self.pro_pic.url
        return 'profilepic/default.png'  # or a default image path
    
    
class House(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    country=models.CharField(default='Afghanistan', max_length=255, choices=[ ('AF', 'Afghanistan'),
        ('AL', 'Albania'),
        ('DZ', 'Algeria'),
        ('AS', 'American Samoa'),
        ('AD', 'Andorra'),
        ('AO', 'Angola'),
        ('AI', 'Anguilla'),
        ('AG', 'Antigua and Barbuda'),
        ('AR', 'Argentina'),
        ('AM', 'Armenia'),
        ('AW', 'Aruba'),
        ('AU', 'Australia'),
        ('AT', 'Austria'),
        ('AZ', 'Azerbaijan'),
        ('BS', 'Bahamas'),
        ('BH', 'Bahrain'),
        ('BD', 'Bangladesh'),
        ('BB', 'Barbados'),
        ('BY', 'Belarus'),
        ('BE', 'Belgium'),
        ('BZ', 'Belize'),
        ('BJ', 'Benin'),
        ('BM', 'Bermuda'),
        ('BT', 'Bhutan'),
        ('BO', 'Bolivia'),
        ('BA', 'Bosnia and Herzegovina'),
        ('BW', 'Botswana'),
        ('BR', 'Brazil'),
        ('BN', 'Brunei Darussalam'),
        ('BG', 'Bulgaria'),
        ('BF', 'Burkina Faso'),
        ('BI', 'Burundi'),
        ('KH', 'Cambodia'),
        ('CM', 'Cameroon'),
        ('CA', 'Canada'),
        ('CV', 'Cape Verde'),
        ('KY', 'Cayman Islands'),
        ('CF', 'Central African Republic'),
        ('TD', 'Chad'),
        ('CL', 'Chile'),
        ('CN', 'China'),
        ('CO', 'Colombia'),
        ('KM', 'Comoros'),
        ('CG', 'Congo'),
        ('CD', 'Congo, Democratic Republic'),
        ('CR', 'Costa Rica'),
        ('CI', "Cote d'Ivoire"),
        ('HR', 'Croatia'),
        ('CU', 'Cuba'),
        ('CY', 'Cyprus'),
        ('CZ', 'Czech Republic'),
        ('DK', 'Denmark'),
        ('DJ', 'Djibouti'),
        ('DM', 'Dominica'),
        ('DO', 'Dominican Republic'),
        ('EC', 'Ecuador'),
        ('EG', 'Egypt'),
        ('SV', 'El Salvador'),
        ('GQ', 'Equatorial Guinea'),
        ('ER', 'Eritrea'),
        ('EE', 'Estonia'),
        ('ET', 'Ethiopia'),
        ('FJ', 'Fiji'),
        ('FI', 'Finland'),
        ('FR', 'France'),
        ('GA', 'Gabon'),
        ('GM', 'Gambia'),
        ('GE', 'Georgia'),
        ('DE', 'Germany'),
        ('GH', 'Ghana'),
        ('GR', 'Greece'),
        ('GD', 'Grenada'),
        ('GU', 'Guam'),
        ('GT', 'Guatemala'),
        ('GN', 'Guinea'),
        ('GW', 'Guinea-Bissau'),
        ('GY', 'Guyana'),
        ('HT', 'Haiti'),
        ('HN', 'Honduras'),
        ('HU', 'Hungary'),
        ('IS', 'Iceland'),
        ('IN', 'India'),
        ('ID', 'Indonesia'),
        ('IR', 'Iran'),
        ('IQ', 'Iraq'),
        ('IE', 'Ireland'),
        ('IL', 'Israel'),
        ('IT', 'Italy'),
        ('JM', 'Jamaica'),
        ('JP', 'Japan'),
        ('JO', 'Jordan'),
        ('KZ', 'Kazakhstan'),
        ('KE', 'Kenya'),
        ('KI', 'Kiribati'),
        ('KW', 'Kuwait'),
        ('KG', 'Kyrgyzstan'),
        ('LA', 'Lao People\'s Democratic Republic'),
        ('LV', 'Latvia'),
        ('LB', 'Lebanon'),
        ('LS', 'Lesotho'),
        ('LR', 'Liberia'),
        ('LY', 'Libya'),
        ('LI', 'Liechtenstein'),
        ('LT', 'Lithuania'),
        ('LU', 'Luxembourg'),
        ('MG', 'Madagascar'),
        ('MW', 'Malawi'),
        ('MY', 'Malaysia'),
        ('MV', 'Maldives'),
        ('ML', 'Mali'),
        ('MT', 'Malta'),
        ('MH', 'Marshall Islands'),
        ('MR', 'Mauritania'),
        ('MU', 'Mauritius'),
        ('MX', 'Mexico'),
        ('FM', 'Micronesia'),
        ('MD', 'Moldova'),
        ('MC', 'Monaco'),
        ('MN', 'Mongolia'),
        ('ME', 'Montenegro'),
        ('MA', 'Morocco'),
        ('MZ', 'Mozambique'),
        ('MM', 'Myanmar'),
        ('NA', 'Namibia'),
        ('NR', 'Nauru'),
        ('NP', 'Nepal'),
        ('NL', 'Netherlands'),
        ('NZ', 'New Zealand'),
        ('NI', 'Nicaragua'),
        ('NE', 'Niger'),
        ('NG', 'Nigeria'),
        ('KP', 'North Korea'),
        ('MK', 'North Macedonia'),
        ('NO', 'Norway'),
        ('OM', 'Oman'),
        ('PK', 'Pakistan'),
        ('PW', 'Palau'),
        ('PS', 'Palestine'),
        ('PA', 'Panama'),
        ('PG', 'Papua New Guinea'),
        ('PY', 'Paraguay'),
        ('PE', 'Peru'),
        ('PH', 'Philippines'),
        ('PL', 'Poland'),
        ('PT', 'Portugal'),
        ('PR', 'Puerto Rico'),
        ('QA', 'Qatar'),
        ('RO', 'Romania'),
        ('RU', 'Russia'),
        ('RW', 'Rwanda'),
        ('KN', 'Saint Kitts and Nevis'),
        ('LC', 'Saint Lucia'),
        ('VC', 'Saint Vincent and the Grenadines'),
        ('WS', 'Samoa'),
        ('SM', 'San Marino'),
        ('ST', 'Sao Tome and Principe'),
        ('SA', 'Saudi Arabia'),
        ('SN', 'Senegal'),
        ('RS', 'Serbia'),
        ('SC', 'Seychelles'),
        ('SL', 'Sierra Leone'),
        ('SG', 'Singapore'),
        ('SK', 'Slovakia'),
        ('SI', 'Slovenia'),
        ('SB', 'Solomon Islands'),
        ('SO', 'Somalia'),
        ('ZA', 'South Africa'),
        ('KR', 'South Korea'),
        ('SS', 'South Sudan'),
        ('ES', 'Spain'),
        ('LK', 'Sri Lanka'),
        ('SD', 'Sudan'),
        ('SR', 'Suriname'),
        ('SZ', 'Swaziland'),
        ('SE', 'Sweden'),
        ('CH', 'Switzerland'),
        ('SY', 'Syria'),
        ('TW', 'Taiwan'),
        ('TJ', 'Tajikistan'),
        ('TZ', 'Tanzania'),
        ('TH', 'Thailand'),
        ('TL', 'Timor-Leste'),
        ('TG', 'Togo'),
        ('TO', 'Tonga'),
        ('TT', 'Trinidad and Tobago'),
        ('TN', 'Tunisia'),
        ('TR', 'Turkey'),
        ('TM', 'Turkmenistan'),
        ('TV', 'Tuvalu'),
        ('UG', 'Uganda'),
        ('UA', 'Ukraine'),
        ('AE', 'United Arab Emirates'),
        ('GB', 'United Kingdom'),
        ('US', 'United States'),
        ('UY', 'Uruguay'),
        ('UZ', 'Uzbekistan'),
        ('VU', 'Vanuatu'),
        ('VA', 'Vatican City'),
        ('VE', 'Venezuela'),
        ('VN', 'Vietnam'),
        ('YE', 'Yemen'),
        ('ZM', 'Zambia'),
        ('ZW', 'Zimbabwe'),])
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[
        ('for_sale', 'For Sale'),
        ('for_rent', 'For Rent'),
        ('sold', 'Sold')
    ],default='for_rent')
    date_posted = models.DateTimeField(auto_now_add=True)
    area = models.FloatField(null=True)
    rooms_count = models.IntegerField(null=True)
    bathrooms_count = models.IntegerField(null=True)
    bedrooms_count = models.IntegerField(null=True)
   
    year_built = models.IntegerField(null=True)
    property_type = models.CharField(max_length=50, choices=[
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('villa', 'Villa'),
        ('commercial', 'Commercial')
    ],default='apartment')
    parking_spaces = models.IntegerField(null=True, blank=True)
    furnishing_status = models.CharField(max_length=50, choices=[
        ('furnished', 'Furnished'),
        ('unfurnished', 'Unfurnished'),
        ('semi_furnished', 'Semi-Furnished')
    ],default='furnished')
    balcony = models.BooleanField(default=False,null=True)
    garden = models.BooleanField(default=False,null=True)
    pool = models.BooleanField(default=False,null=True)
    heating_type = models.CharField(max_length=50, choices=[
        ('central', 'Central Heating'),
        ('electric', 'Electric Heating'),
        ('none', 'No Heating')
    ],default='central')
    cooling_type = models.CharField(max_length=50, choices=[
        ('central', 'Central Air'),
        ('window', 'Window Units'),
        ('none', 'No Cooling')
    ],default='central')
    pet_policy = models.CharField(max_length=50, choices=[
        ('allowed', 'Pets Allowed'),
        ('not_allowed', 'No Pets Allowed')
    ],default='allowed')
    is_for_sale=models.BooleanField(default=True)
    floors=models.IntegerField(null=True, blank=True)
    security_features = models.CharField(max_length=255, null=True, blank=True)
    nearby_amenities = models.CharField(max_length=255, null=True, blank=True)
    # images = models.ManyToManyField('Image',to='' blank=True)
   
    contact_phone = models.CharField(max_length=15,null=True)
    contact_email = models.EmailField(null=True)
    published = models.BooleanField(default=False)
   
    default_pic = models.ImageField(upload_to='property_images/', default='property_images/defhouse.jpg')
    
    # Additional images for the house
    pics = models.ImageField('HouseImage',  null=True)
    def __str__(self):
        return self.title
    
    def get_image_url(self):
        if self.pics:
            return self.pics.url
        return 'property_images/default.jpg'  # or a default image path
    
    def get_default_image_url(self):
        if self.default_pic:
            return self.default_pic.url
        return 'property_images/default.jpg'
    
class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.house.title}"
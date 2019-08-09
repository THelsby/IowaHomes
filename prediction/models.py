from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class HouseInformation(models.Model):
    MS_SUBCLASS_CHOICES = (
        ('20', '1-STORY 1946 & NEWER ALL STYLES'),
        ('30', '1-STORY 1945 & OLDER'),
        ('40', '1-STORY W/FINISHED ATTIC ALL AGES'),
        ('45', '1-1/2 STORY - UNFINISHED ALL AGES'),
        ('50', '1-1/2 STORY FINISHED ALL AGES'),
        ('60', '2-STORY 1946 & NEWER'),
        ('70', '2-STORY 1945 & OLDER'),
        ('75', '2-1/2 STORY ALL AGES'),
        ('80', 'SPLIT OR MULTI-LEVEL'),
        ('85', 'SPLIT FOYER'),
        ('90', 'DUPLEX - ALL STYLES AND AGES'),
        ('120', '1-STORY PUD (Planned Unit Development) - 1946 & NEWER'),
        ('150', '1-1/2 STORY PUD - ALL AGES'),
        ('160', '2-STORY PUD - 1946 & NEWER'),
        ('180', 'PUD - MULTILEVEL - INCL SPLIT LEV/FOYER'),
        ('190', '2 FAMILY CONVERSION - ALL STYLES AND AGES')
    )
    MS_ZONING_CHOICES = (
        ('A', 'Agriculture'),
        ('C', 'Commercial'),
        ('FV', 'Floating Village Residential'),
        ('I', 'Industrial'),
        ('RH', 'Residential High Density'),
        ('RL', 'Residential Low Density'),
        ('RP', 'Residential Low Density Park'),
        ('RM', 'Residential Medium Density')
    )

    STREET_CHOICES = (
        ('Grvl', 'Gravel'),
        ('Pave', 'Paved')
    )

    ALLEY_CHOICES = (
        ('Grvl', 'Gravel'),
        ('Pave', 'Paved'),
        ('NA', 'No alley access')
    )

    LOT_SHAPE_CHOICES = (
        ('Reg', 'Regular'),
        ('IR1', 'Slightly irregular'),
        ('IR2', 'Moderately Irregular'),
        ('IR3', 'Irregular')
    )

    LAND_CONTOUR_CHOICES = (
        ('Lvl', 'Near Flat/Level'),
        ('Bnk', 'Quick and significant rise from street grade to building'),
        ('HLS', 'Significant slope from side to side'),
        ('low', 'Depression')
    )
    LOT_CONFIG_CHOICES = (
        ('Inside', 'Inside lot'),
        ('Corner', 'Corner lot'),
        ('CulDSac', 'Cul-de-sac'),
        ('FR2', 'Frontage on 2 sides of property'),
        ('FR3', 'Frontage on 3 sides of property')
    )
    LAND_SLOPE_CHOICE = (
        ('Gtl', 'Gentle slope'),
        ('Mod', 'Moderate Slope'),
        ('Sev', 'Severe Slope')
    )
    NEIGHBORHOOD_CHOICES = (
        ('Blmngtn', 'Bloomington Heights'),
        ('Blueste', 'Bluestem'),
        ('BrDale', 'Briardale'),
        ('BrkSide', 'Brookside'),
        ('ClearCr', 'Clear Creek'),
        ('CollgCr', 'College Creek'),
        ('Crawfor', 'Crawford'),
        ('Edwards', 'Edwards'),
        ('Gilbert', 'Gilbert'),
        ('IDOTRR', 'Iowa DOT and Rail Road'),
        ('MeadowV', 'Meadow Village'),
        ('Mitchel', 'Mitchell'),
        ('Names', 'North Ames'),
        ('NoRidge', 'Northridge'),
        ('NPkVill', 'Northpark Villa'),
        ('NridgHt', 'Northridge Heights'),
        ('NWAmes', 'Northwest Ames'),
        ('OldTown', 'Old Town'),
        ('SWISU', 'South & West of Iowa State University'),
        ('Sawyer', 'Sawyer'),
        ('SawyerW', 'Sawyer West'),
        ('Somerst', 'Somerset'),
        ('StoneBr', 'Stone Brook'),
        ('Timber', 'Timberland'),
        ('Veeneker', 'Veenker'),
    )
    CONDITION_CHOICES = (
        ('Artery', 'Adjacent to arterial street'),
        ('Feedr', 'Adjacent to feeder street'),
        ('Norm', 'Normal'),
        ('RRNn', "Within 200' of North-South Railroad"),
        ('RRAn', 'Adjacent to North-South Railroad'),
        ('PosN', 'Near positive off-site feature--park, greenbelt, etc.'),
        ('PosA', 'Adjacent to postive off-site feature'),
        ('RRNe', "Within 200' of East-West Railroad"),
        ('RRAe', 'Adjacent to East-West Railroad'),
    )
    BLDGTYPE_CHOICES = (
        ('1Fam', 'Single-family Detached'),
        ('2FmCon', 'Two-family Conversion; originally built as one-family dwelling'),
        ('Duplx', 'Duplex'),
        ('TwnhsE', 'Townhouse End Unit'),
        ('TwnhsI', 'Townhouse Inside Unit')
    )
    HOUSE_STYLE_CHOICES = (
        ('1Story', 'One story'),
        ('1.5Fin', 'One and one-half story | 2nd level finished'),
        ('1.5Unf', 'One and one-half story | 2nd level unfinished'),
        ('2Story', 'Two story'),
        ('2.5Fin', 'Two and one-half story | 2nd level finished'),
        ('2.5Unf', 'Two and one-half story | 2nd level unfinished'),
        ('SFoyer', 'Split Foyer'),
        ('SLvl', 'Split Level')
    )
    OVERALL_CHOICES = (
        ('10', 'Very Excellent'),
        ('9', 'Excellent'),
        ('8', 'Very Good'),
        ('7', 'Good'),
        ('6', 'Above Average'),
        ('5', 'Average'),
        ('4', 'Below Average'),
        ('3', 'Fair'),
        ('2', 'Poor'),
        ('1', 'Very Poor')
    )

    MSSubClass = models.IntegerField(choices=MS_SUBCLASS_CHOICES,
                                     help_text='Identifies the type of dwelling involved in the sale.')
    MSZoning = models.CharField(max_length=2, choices=MS_ZONING_CHOICES,
                                help_text='Identifies the general zoning classification of the sale.')
    LotFrontage = models.IntegerField(default=0, validators=[MaxValueValidator(500), MinValueValidator(1)],
                                      help_text='Linear feet of street connected to property (Min 0 | Max 500)')
    LotArea = models.IntegerField(default=0, validators=[MaxValueValidator(50000), MinValueValidator(1)],
                                  help_text='Lot size in square feet (Min 0 | Max 50000)')
    Street = models.CharField(max_length=4, choices=STREET_CHOICES,
                              help_text='Type of road access to property')
    Alley = models.CharField(max_length=4, choices=ALLEY_CHOICES, help_text='Type of alley access to property')
    LotShape = models.CharField(max_length=3, choices=LOT_SHAPE_CHOICES, help_text='General shape of property')
    LandContour = models.CharField(max_length=3, choices=LAND_CONTOUR_CHOICES, help_text='Flatness of the property')
    LandSlope = models.CharField(max_length=3, choices=LAND_SLOPE_CHOICE, help_text='Slope of property')
    Neighborhood = models.CharField(max_length=8, choices=NEIGHBORHOOD_CHOICES,
                                    help_text='Physical locations within Ames city limits')
    ConditionOne = models.CharField(max_length=6, choices=CONDITION_CHOICES,
                                    help_text='Proximity to various conditions')
    ConditionTwo = models.CharField(max_length=6, choices=CONDITION_CHOICES,
                                    help_text='Proximity to various conditions (if more than one is present)')
    BldgType = models.CharField(max_length=6, choices=BLDGTYPE_CHOICES, help_text='Type of dwelling')
    HouseStyle = models.CharField(max_length=6, choices=HOUSE_STYLE_CHOICES, help_text='Style of dwelling')
    OverallQual = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(1)],
                                      choices=OVERALL_CHOICES,
                                      help_text='Rates the overall material and finish of the house')
    OverallCond = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(1)],
                                      choices=OVERALL_CHOICES, help_text='Rates the overall condition of the house')
    # TODO Figure out how to have year only
    YearBuilt = models.IntegerField(default=2019, validators=[MaxValueValidator(2020), MinValueValidator(0)],
                                    help_text='Original construction date')

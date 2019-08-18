import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class HouseInformation(models.Model):
    MS_SUBCLASS_CHOICES = (
        (20, '1-STORY 1946 & NEWER ALL STYLES'),
        (30, '1-STORY 1945 & OLDER'),
        (40, '1-STORY W/FINISHED ATTIC ALL AGES'),
        (45, '1-1/2 STORY - UNFINISHED ALL AGES'),
        (50, '1-1/2 STORY FINISHED ALL AGES'),
        (60, '2-STORY 1946 & NEWER'),
        (70, '2-STORY 1945 & OLDER'),
        (75, '2-1/2 STORY ALL AGES'),
        (80, 'SPLIT OR MULTI-LEVEL'),
        (85, 'SPLIT FOYER'),
        (90, 'DUPLEX - ALL STYLES AND AGES'),
        (120, '1-STORY PUD (Planned Unit Development) - 1946 & NEWER'),
        (150, '1-1/2 STORY PUD - ALL AGES'),
        (160, '2-STORY PUD - 1946 & NEWER'),
        (180, 'PUD - MULTILEVEL - INCL SPLIT LEV/FOYER'),
        (190, '2 FAMILY CONVERSION - ALL STYLES AND AGES')
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
        (10, 'Very Excellent'),
        (9, 'Excellent'),
        (8, 'Very Good'),
        (7, 'Good'),
        (6, 'Above Average'),
        (5, 'Average'),
        (4, 'Below Average'),
        (3, 'Fair'),
        (2, 'Poor'),
        (1, 'Very Poor')
    )
    ROOF_STYLE_CHOICES = (
        ('Flat', 'Flat'),
        ('Gable', 'Gable'),
        ('Gambrel', 'Gabrel (Barn)'),
        ('Hip', 'Hip'),
        ('Mansard', 'Mansard'),
        ('Shed', 'Shed')
    )
    ROOF_MAT_CHOICES = (
        ('ClyTile', 'Clay or Tile'),
        ('CompShg', 'Standard (Composite) Shingle'),
        ('Membran', 'Membrane'),
        ('Metal', 'Metal'),
        ('Roll', 'Roll'),
        ('Tar&Grv', 'Gravel & Tar'),
        ('WdShake', 'Wood Shakes'),
        ('WdShngl', 'Wood Shingles')
    )
    EXTERIOR_CHOICES = (
        ('AsbShng', 'Asbestos Shingles'),
        ('AsphShn', 'Asphalt Shingles'),
        ('BrkComm', 'Brick Common'),
        ('BrkFace', 'Brick Face'),
        ('CBlock', 'Cinder Block'),
        ('CemntBd', 'Cement Board'),
        ('HdBoard', 'Hard Board'),
        ('ImStucc', 'Imitation Stucco'),
        ('MetalSd', 'Metal Siding'),
        ('Other', 'Other'),
        ('Plywood', 'Plywood'),
        ('PreCast', 'PreCast'),
        ('Stone', 'Stone'),
        ('Stucco', 'Stucco'),
        ('VinylSd', 'Vinyl Siding'),
        ('Wd Sdng', 'Wood Siding'),
        ('WdShing', 'Wood Shingles')
    )
    MAS_VNR_CHOICES = (
        ('BrkCmn', 'Brick Common'),
        ('BrkFace', 'Brick Face'),
        ('CBlock', 'Cinder Block'),
        ('None', 'None'),
        ('Stone', 'Stone')
    )
    EXTERIOR_QUALITY_CHOICES = (
        ('Ex', 'Excellent'),
        ('Gd', 'Good'),
        ('TA', 'Average / Typical'),
        ('Fa', 'Fair'),
        ('Po', 'Poor')
    )
    FOUNDATION_CHOICES = (
        ('BrkTil', 'Brick & Tile'),
        ('CBlock', 'Cinder Block'),
        ('PConc', 'Poured Contrete'),
        ('Slab', 'Slab'),
        ('Stone', 'Stone'),
        ('Wood', 'Wood')
    )
    BSMT_QUAL_CHOICES = (
        ('Ex', 'Excellent (100+ inches)'),
        ('Gd', 'Good (90 - 99 inches)'),
        ('TA', 'Typical (80 - 89 inches)'),
        ('Fa', 'Fair (70 - 79 inches)'),
        ('Po', 'Poor (<70 inches)'),
        ('NA', 'No Basement')
    )
    BSMT_COND_CHOICES = (
        ('Ex', 'Excellent'),
        ('Gd', 'Good'),
        ('TA', 'Typical - slight dampness allowed'),
        ('Fa', 'Fair - dampness or some cracking or settling'),
        ('Po', 'Poor - Severe cracking, settling, or wetness'),
        ('NA', 'No Basement')
    )
    BSMT_EXPOSURE_CHOICES = (
        ('Gd', 'Good Exposure'),
        ('Av', 'Average Exposure (split levels or foyers typically score average or above)'),
        ('Mn', 'Minimum Exposure'),
        ('No', 'No Exposure'),
        ('NA', 'No Basement')
    )
    BSMT_FIN_TYPE_CHOICES = (
        ('GLQ', 'Good Living Quarters'),
        ('ALQ', 'Average Living Quarters'),
        ('BLQ', 'Below Average Living Quarters'),
        ('Rec', 'Average Rec Room'),
        ('LwQ', 'Low Quality'),
        ('Unf', 'Unfinshed'),
        ('NA', 'No Basement')
    )
    HEATING_CHOICES = (
        ('Floor', 'Floor Furnace'),
        ('GasA', 'Gas forced warm air furnace'),
        ('GasW', 'Gas hot water or steam heat'),
        ('Grav', 'Gravity furnace'),
        ('OthW', 'Hot water or steam heat other than gas'),
        ('Wall', 'Wall furnace')
    )
    HEATING_QC_CHOICES = (
        ('Ex', 'Excellent'),
        ('Gd', 'Good'),
        ('TA', 'Average / Typical'),
        ('Fa', 'Fair'),
        ('Po', 'Poor'),
    )
    CENTRAL_AIR_CHOICES = (
        ('N', 'No'),
        ('Y', 'Yes')
    )
    ELECTRICAL_CHOICES = (
        ('SBrkr', 'Standard Circuit Breakers & Romex'),
        ('FuseA', 'Fuse Box over 60 AMP and all Romex wiring (Average)'),
        ('FuseF', '60 AMP Fuse Box and mostly Romex wiring (Fair)'),
        ('FuseP', '60 AMP Fuse Box and mostly knob & tube wiring (poor)'),
        ('Mix', 'Mixed')
    )
    FUNCTIONAL_CHOICES = (
        ('Typ', 'Typical Functionality'),
        ('Min1', 'Minor Deductions 1'),
        ('Min2', 'Minor Deductions 2'),
        ('Mod', 'Moderate Deductions'),
        ('Maj1', 'Major Deductions 1'),
        ('Maj2', 'Major Deductions 2'),
        ('Sev', 'Severely Damaged'),
        ('Sal', 'Salvage only')
    )
    FIREPLACE_QUALITY_CHOICES = (
        ('Ex', 'Excellent - Exceptional Masonry Fireplace'),
        ('Gd', 'Good - Masonry Fireplace in main level'),
        ('TA', 'Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement'),
        ('Fa', 'Fair - Prefabricated Fireplace in basement'),
        ('Po', 'Poor - Ben Franklin Stove')
    )
    GARAGE_TYPE_CHOICE = (
        ('2Types', 'More than one type of garage'),
        ('Attchd', 'Attached to home'),
        ('Basment', 'Basement Garage'),
        ('BuiltIn', 'Built-In (Garage part of house - typically has room above garage)'),
        ('CarPort', 'Car Port'),
        ('Detchd', 'Detached from home'),
        ('NA', 'No Garage')
    )
    GARAGE_FINISH_CHOICE = (
        ('Fin', 'Finished'),
        ('RFn', 'Rough Finished'),
        ('Unf', 'Unfinished'),
        ('NA', 'No Garage')
    )
    PAVED_DRIVE_CHOICES = (
        ('Y', 'Paved'),
        ('P', 'Partial Pavement'),
        ('N', 'Dirt / Gravel')
    )
    POOL_QC_CHOICES = (
        ('Ex', 'Excellent'),
        ('Gd', 'Good'),
        ('TA', 'Average / Typical'),
        ('Fa', 'Fair'),
        ('NA', 'No Pool'),
    )
    FENCE_QUALITY_CHOICES = (
        ('GdPrv', 'Good Privacy'),
        ('MnPrv', 'Minimum Privacy'),
        ('GdWo', 'Good Wood'),
        ('MnWw', 'Minimum Wood / Wire'),
        ('NA', 'No Fence')
    )
    MISC_FEATURE_CHOICES = (
        ('Elev', 'Elevator'),
        ('Gar2', '2nd Garage (if not described in garage section)'),
        ('Othr', 'Other'),
        ('Shed', 'Shed (over 100 SF)'),
        ('Tenc', 'Tennis Court'),
        ('NA', 'None')
    )
    MSSubClass = models.IntegerField(choices=MS_SUBCLASS_CHOICES,
                                     help_text='Identifies the type of dwelling involved in the sale.', null=True)
    MSZoning = models.CharField(max_length=2, choices=MS_ZONING_CHOICES,
                                help_text='Identifies the general zoning classification of the sale.', null=True)
    LotFrontage = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(500)],
                                      help_text='Linear feet of street connected to property (Min 0 | Max 500)',
                                      null=True)
    LotArea = models.IntegerField(default=0, validators=[MaxValueValidator(50000), MinValueValidator(1)],
                                  help_text='Lot size in square feet (Min 0 | Max 50000)', null=True)
    Street = models.CharField(max_length=4, choices=STREET_CHOICES,
                              help_text='Type of road access to property', null=True)
    Alley = models.CharField(max_length=4, choices=ALLEY_CHOICES, help_text='Type of alley access to property',
                             null=True)
    LotShape = models.CharField(max_length=3, choices=LOT_SHAPE_CHOICES, help_text='General shape of property',
                                null=True)
    LandContour = models.CharField(max_length=3, choices=LAND_CONTOUR_CHOICES, help_text='Flatness of the property',
                                   null=True)
    LotConfig = models.CharField(max_length=7, choices=LOT_CONFIG_CHOICES, help_text='Lot configuration',
                                 null=True)
    LandSlope = models.CharField(max_length=3, choices=LAND_SLOPE_CHOICE, help_text='Slope of property', null=True)
    Neighborhood = models.CharField(max_length=8, choices=NEIGHBORHOOD_CHOICES,
                                    help_text='Physical locations within Ames city limits', null=True)
    Condition1 = models.CharField(max_length=6, choices=CONDITION_CHOICES,
                                  help_text='Proximity to various conditions', null=True)
    Condition2 = models.CharField(max_length=6, choices=CONDITION_CHOICES,
                                  help_text='Proximity to various conditions (if more than one is present)', null=True)
    BldgType = models.CharField(max_length=6, choices=BLDGTYPE_CHOICES, help_text='Type of dwelling', null=True)
    HouseStyle = models.CharField(max_length=10, choices=HOUSE_STYLE_CHOICES, help_text='Style of dwelling', null=True)
    OverallQual = models.IntegerField(choices=OVERALL_CHOICES,
                                      help_text='Rates the overall material and finish of the house', null=True)
    OverallCond = models.IntegerField(choices=OVERALL_CHOICES, help_text='Rates the overall condition of the house',
                                      null=True)
    # TODO Figure out how to have year only
    YearBuilt = models.IntegerField(default=2019, validators=[MaxValueValidator(2020), MinValueValidator(0)],
                                    help_text='Original construction year', null=True)
    YearRemodAdd = models.IntegerField(default=2019, validators=[MaxValueValidator(2020), MinValueValidator(0)],
                                       help_text='Remodel year (same as construction date if no remodeling or '
                                                 'additions)', null=True)
    RoofStyle = models.CharField(max_length=7, choices=ROOF_STYLE_CHOICES, help_text='Type of roof', null=True)
    RoofMatl = models.CharField(max_length=7, choices=ROOF_MAT_CHOICES, help_text='Roof material', null=True)
    Exterior1st = models.CharField(max_length=7, choices=EXTERIOR_CHOICES, help_text='Exterior covering on house',
                                   null=True)
    Exterior2nd = models.CharField(max_length=7, choices=EXTERIOR_CHOICES, help_text='Exterior covering on house (if '
                                                                                     'more than one material)',
                                   null=True)
    MasVnrType = models.CharField(max_length=7, choices=MAS_VNR_CHOICES, help_text='Masonry veneer type', null=True)
    MasVnrArea = models.IntegerField(default=0, validators=[MaxValueValidator(3000), MinValueValidator(0)],
                                     help_text='Lot size in square feet (Min 0 | Max 3000)', null=True)
    ExterQual = models.CharField(max_length=2, choices=EXTERIOR_QUALITY_CHOICES, help_text='Evaluates the quality of '
                                                                                           'the material on the '
                                                                                           'exterior', null=True)
    ExterCond = models.CharField(max_length=2, choices=EXTERIOR_QUALITY_CHOICES, help_text='Evaluates the quality of '
                                                                                           'the material on the '
                                                                                           'exterior', null=True)
    Foundation = models.CharField(max_length=6, choices=FOUNDATION_CHOICES, help_text='Type of foundation', null=True)
    BsmtQual = models.CharField(max_length=2, choices=BSMT_QUAL_CHOICES, help_text='Evaluates the height of the '
                                                                                   'basement', null=True)
    BsmtCond = models.CharField(max_length=2, choices=BSMT_COND_CHOICES, help_text='Evaluates the general condition '
                                                                                   'of the basement', null=True)
    BsmtExposure = models.CharField(max_length=2, choices=BSMT_EXPOSURE_CHOICES, help_text='Refers to walkout or '
                                                                                           'garden '
                                                                                           'level walls', null=True)
    BsmtFinType1 = models.CharField(max_length=3, choices=BSMT_FIN_TYPE_CHOICES, help_text='Rating of basement '
                                                                                           'finished area', null=True)
    BsmtFinSF1 = models.IntegerField(default=0, validators=[MaxValueValidator(6000), MinValueValidator(0)],
                                     help_text='Type 1 finished square feet (Min 0 | Max 6000)', null=True)
    BsmtFinType2 = models.CharField(max_length=3, choices=BSMT_FIN_TYPE_CHOICES, help_text='Rating of basement '
                                                                                           'finished area (if '
                                                                                           'multiple types)', null=True)
    BsmtFinSF2 = models.IntegerField(default=0, validators=[MaxValueValidator(6000), MinValueValidator(0)],
                                     help_text='Type 2 finished square feet (Min 0 | Max 6000)', null=True)
    BsmtUnfSF = models.IntegerField(default=0, validators=[MaxValueValidator(4000), MinValueValidator(0)],
                                    help_text='Unfinished square feet of basement area (Min 0 | Max 4000)', null=True)
    TotalBsmtSF = models.IntegerField(default=0, validators=[MaxValueValidator(6500), MinValueValidator(0)],
                                      help_text='Total square feet of basement area (Min 0 | Max 6500)', null=True)
    Heating = models.CharField(max_length=5, choices=HEATING_CHOICES, help_text='Type of heating', null=True)
    HeatingQC = models.CharField(max_length=2, choices=HEATING_QC_CHOICES, help_text='Heating quality and condition',
                                 null=True)
    CentralAir = models.CharField(max_length=1, choices=CENTRAL_AIR_CHOICES, help_text='Central air conditioning',
                                  null=True)
    Electrical = models.CharField(max_length=5, choices=ELECTRICAL_CHOICES, help_text='Electrical system', null=True)
    OneFlrSF = models.IntegerField(default=0, validators=[MaxValueValidator(5000), MinValueValidator(0)],
                                   help_text='First Floor square feet (Min 0 | Max 5000)', null=True)
    TwoFlrSF = models.IntegerField(default=0, validators=[MaxValueValidator(5000), MinValueValidator(0)],
                                   help_text='Second floor square feet (Min 0 | Max 5000)', null=True)
    LowQualFinSF = models.IntegerField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)],
                                       help_text='Low quality finished square feet (all floors) (Min 0 | Max 1000)',
                                       null=True)
    GrLivArea = models.IntegerField(default=0, validators=[MaxValueValidator(6000), MinValueValidator(0)],
                                    help_text='Above grade (ground) living area square feet (Min 0 | Max 6000)',
                                    null=True)
    BsmtFullBath = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)],
                                       help_text='Basement full bathrooms (Min 0 | Max 10)', null=True)
    BsmtHalfBath = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)],
                                       help_text='Basement half bathrooms (Min 0 | Max 10)', null=True)
    FullBath = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)],
                                   help_text='Full bathrooms above grade (Min 0 | Max 10)', null=True)
    HalfBath = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)],
                                   help_text='Half baths above grade (Min 0 | Max 10)', null=True)
    BedroomAbvGr = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)],
                                       help_text='Bedrooms above grade (does NOT include basement bedrooms) (Min 0 | '
                                                 'Max '
                                                 '10)', null=True)
    KitchenAbvGr = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)],
                                       help_text='Kitchens above grade (Min 0 | Max 10)', null=True)
    KitchenQual = models.CharField(max_length=2, choices=HEATING_QC_CHOICES, help_text='Kitchen quality', null=True)
    TotRmsAbvGrd = models.IntegerField(default=0, validators=[MaxValueValidator(20), MinValueValidator(0)],
                                       help_text='Total rooms above grade (does not include bathrooms) (Min 0 | '
                                                 'Max '
                                                 '20)', null=True)
    Functional = models.CharField(max_length=4, choices=FUNCTIONAL_CHOICES,
                                  help_text='Home functionality (Assume typical unless deductions are warranted)',
                                  null=True)
    Fireplaces = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)],
                                     help_text='Number of fireplaces (Min 0 | Max 10)', null=True)
    FireplaceQu = models.CharField(max_length=6, choices=FIREPLACE_QUALITY_CHOICES, help_text='Fireplace quality',
                                   null=True)
    GarageType = models.CharField(max_length=6, choices=GARAGE_TYPE_CHOICE, help_text='Garage location', null=True)
    # TODO DATE
    GarageYrBlt = models.IntegerField(default=2019, validators=[MaxValueValidator(2020), MinValueValidator(0)],
                                      help_text='Year garage was built', null=True)
    GarageFinish = models.CharField(max_length=3, choices=GARAGE_FINISH_CHOICE,
                                    help_text='Interior finish of the garage', null=True)
    GarageCars = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)],
                                     help_text='Size of garage in car capacity (Min 0 | Max 10)', null=True)
    GarageArea = models.IntegerField(default=0, validators=[MaxValueValidator(2000), MinValueValidator(0)],
                                     help_text='Size of garage in square feet (Min 0 | Max 2000)', null=True)
    GarageQual = models.CharField(max_length=2, choices=HEATING_QC_CHOICES, help_text='Garage quality', null=True)
    GarageCond = models.CharField(max_length=2, choices=HEATING_QC_CHOICES,
                                  help_text='Garage conditionGarage condition', null=True)
    PavedDrive = models.CharField(max_length=2, choices=PAVED_DRIVE_CHOICES, help_text='Paved driveway', null=True)
    WoodDeckSF = models.IntegerField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)],
                                     help_text='Wood deck area in square feet (Min 0 | Max 1000)', null=True)
    # TODO create plots are find better values
    OpenPorchSF = models.IntegerField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)],
                                      help_text='Open porch area in square feet (Min 0 | Max 1000)', null=True)
    EnclosedPorch = models.IntegerField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)],
                                        help_text='Enclosed porch area in square feet (Min 0 | Max 1000)', null=True)
    ThreeSsnPorch = models.IntegerField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)],
                                        help_text='Three season porch area in square feet (Min 0 | Max 1000)',
                                        null=True)
    ScreenPorch = models.IntegerField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)],
                                      help_text='Screen porch area in square feet (Min 0 | Max 1000)', null=True)
    PoolArea = models.IntegerField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)],
                                   help_text='Pool area in square feet (Min 0 | Max 1000)', null=True)
    PoolQC = models.CharField(max_length=2, choices=POOL_QC_CHOICES, help_text='Pool quality', null=True)
    Fence = models.CharField(max_length=5, choices=FENCE_QUALITY_CHOICES, help_text='Fence quality', null=True)
    MiscFeature = models.CharField(max_length=5, choices=MISC_FEATURE_CHOICES,
                                   help_text='Miscellaneous feature not covered in other categories', null=True)
    # TODO CHECK IF NEEDED
    MiscVal = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)],
                                  help_text='Pool area in square feet (Min 0 | Max 1000)', null=True)


class PredictionLog(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    housePredId = models.ForeignKey(HouseInformation, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=now, editable=False)

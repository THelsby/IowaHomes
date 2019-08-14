# Generated by Django 2.2.4 on 2019-08-14 08:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_auto_20190809_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseinformation',
            name='Alley',
            field=models.CharField(choices=[('Grvl', 'Gravel'), ('Pave', 'Paved'), ('NA', 'No alley access')], help_text='Type of alley access to property', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BedroomAbvGr',
            field=models.IntegerField(default=0, help_text='Bedrooms above grade (does NOT include basement bedrooms) (Min 0 | Max 10)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BldgType',
            field=models.CharField(choices=[('1Fam', 'Single-family Detached'), ('2FmCon', 'Two-family Conversion; originally built as one-family dwelling'), ('Duplx', 'Duplex'), ('TwnhsE', 'Townhouse End Unit'), ('TwnhsI', 'Townhouse Inside Unit')], help_text='Type of dwelling', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BsmtCond',
            field=models.CharField(choices=[('Ex', 'Excellent'), ('Gd', 'Good'), ('TA', 'Typical - slight dampness allowed'), ('Fa', 'Fair - dampness or some cracking or settling'), ('Po', 'Poor - Severe cracking, settling, or wetness'), ('NA', 'No Basement')], help_text='Evaluates the general condition of the basement', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BsmtExposure',
            field=models.CharField(choices=[('Gd', 'Good Exposure'), ('Av', 'Average Exposure (split levels or foyers typically score average or above)'), ('Mn', 'Minimum Exposure'), ('No', 'No Exposure'), ('NA', 'No Basement')], help_text='Refers to walkout or garden level walls', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BsmtFinSF1',
            field=models.IntegerField(default=0, help_text='Type 1 finished square feet (Min 0 | Max 6000)', null=True, validators=[django.core.validators.MaxValueValidator(6000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BsmtFinSF2',
            field=models.IntegerField(default=0, help_text='Type 2 finished square feet (Min 0 | Max 6000)', null=True, validators=[django.core.validators.MaxValueValidator(6000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BsmtFinType1',
            field=models.CharField(choices=[('Gd', 'Good Exposure'), ('Av', 'Average Exposure (split levels or foyers typically score average or above)'), ('Mn', 'Minimum Exposure'), ('No', 'No Exposure'), ('NA', 'No Basement')], help_text='Rating of basement finished area', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BsmtFinType2',
            field=models.CharField(choices=[('Gd', 'Good Exposure'), ('Av', 'Average Exposure (split levels or foyers typically score average or above)'), ('Mn', 'Minimum Exposure'), ('No', 'No Exposure'), ('NA', 'No Basement')], help_text='Rating of basement finished area (if multiple types)', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BsmtFullBath',
            field=models.IntegerField(default=0, help_text='Basement full bathrooms (Min 0 | Max 10)', null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BsmtHalfBath',
            field=models.IntegerField(default=0, help_text='Basement half bathrooms (Min 0 | Max 10)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BsmtQual',
            field=models.CharField(choices=[('Ex', 'Excellent (100+ inches)'), ('Gd', 'Good (90 - 99 inches)'), ('TA', 'Typical (80 - 89 inches)'), ('Fa', 'Fair (70 - 79 inches)'), ('Po', 'Poor (<70 inches)'), ('NA', 'No Basement')], help_text='Evaluates the height of the basement', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='BsmtUnfSF',
            field=models.IntegerField(default=0, help_text='Unfinished square feet of basement area (Min 0 | Max 4000)', null=True, validators=[django.core.validators.MaxValueValidator(4000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='CentralAir',
            field=models.CharField(choices=[('N', 'No'), ('Y', 'Yes')], help_text='Central air conditioning', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Condition1',
            field=models.CharField(choices=[('Artery', 'Adjacent to arterial street'), ('Feedr', 'Adjacent to feeder street'), ('Norm', 'Normal'), ('RRNn', "Within 200' of North-South Railroad"), ('RRAn', 'Adjacent to North-South Railroad'), ('PosN', 'Near positive off-site feature--park, greenbelt, etc.'), ('PosA', 'Adjacent to postive off-site feature'), ('RRNe', "Within 200' of East-West Railroad"), ('RRAe', 'Adjacent to East-West Railroad')], help_text='Proximity to various conditions', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Condition2',
            field=models.CharField(choices=[('Artery', 'Adjacent to arterial street'), ('Feedr', 'Adjacent to feeder street'), ('Norm', 'Normal'), ('RRNn', "Within 200' of North-South Railroad"), ('RRAn', 'Adjacent to North-South Railroad'), ('PosN', 'Near positive off-site feature--park, greenbelt, etc.'), ('PosA', 'Adjacent to postive off-site feature'), ('RRNe', "Within 200' of East-West Railroad"), ('RRAe', 'Adjacent to East-West Railroad')], help_text='Proximity to various conditions (if more than one is present)', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Electrical',
            field=models.CharField(choices=[('SBrkr', 'Standard Circuit Breakers & Romex'), ('FuseA', 'Fuse Box over 60 AMP and all Romex wiring (Average)'), ('FuseF', '60 AMP Fuse Box and mostly Romex wiring (Fair)'), ('FuseP', '60 AMP Fuse Box and mostly knob & tube wiring (poor)'), ('Mix', 'Mixed')], help_text='Electrical system', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='EnclosedPorch',
            field=models.IntegerField(default=0, help_text='Enclosed porch area in square feet (Min 0 | Max 1000)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='ExterCond',
            field=models.CharField(choices=[('Ex', 'Excellent'), ('Gd', 'Good'), ('TA', 'Average / Typical'), ('Fa', 'Fair'), ('Po', 'Poor')], help_text='Evaluates the quality of the material on the exterior', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='ExterQaul',
            field=models.CharField(choices=[('Ex', 'Excellent'), ('Gd', 'Good'), ('TA', 'Average / Typical'), ('Fa', 'Fair'), ('Po', 'Poor')], help_text='Evaluates the quality of the material on the exterior', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Exterior1',
            field=models.CharField(choices=[('AsbShng', 'Asbestos Shingles'), ('AsphShn', 'Asphalt Shingles'), ('BrkComm', 'Brick Common'), ('BrkFace', 'Brick Face'), ('CBlock', 'Cinder Block'), ('CemntBd', 'Cement Board'), ('HdBoard', 'Hard Board'), ('ImStucc', 'Imitation Stucco'), ('MetalSd', 'Metal Siding'), ('Other', 'Other'), ('Plywood', 'Plywood'), ('PreCast', 'PreCast'), ('Stone', 'Stone'), ('Stucco', 'Stucco'), ('VinylSd', 'Vinyl Siding'), ('Wd Sdng', 'Wood Siding'), ('WdShing', 'Wood Shingles')], help_text='Exterior covering on house', max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Exterior2',
            field=models.CharField(choices=[('AsbShng', 'Asbestos Shingles'), ('AsphShn', 'Asphalt Shingles'), ('BrkComm', 'Brick Common'), ('BrkFace', 'Brick Face'), ('CBlock', 'Cinder Block'), ('CemntBd', 'Cement Board'), ('HdBoard', 'Hard Board'), ('ImStucc', 'Imitation Stucco'), ('MetalSd', 'Metal Siding'), ('Other', 'Other'), ('Plywood', 'Plywood'), ('PreCast', 'PreCast'), ('Stone', 'Stone'), ('Stucco', 'Stucco'), ('VinylSd', 'Vinyl Siding'), ('Wd Sdng', 'Wood Siding'), ('WdShing', 'Wood Shingles')], help_text='Exterior covering on house (if more than one material)', max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Fence',
            field=models.CharField(choices=[('GdPrv', 'Good Privacy'), ('MnPrv', 'Minimum Privacy'), ('GdWo', 'Good Wood'), ('MnWw', 'Minimum Wood / Wire'), ('NA', 'No Fence')], help_text='Fence quality', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='FireplaceQu',
            field=models.CharField(choices=[('Ex', 'Excellent - Exceptional Masonry Fireplace'), ('Gd', 'Good - Masonry Fireplace in main level'), ('TA', 'Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement'), ('Fa', 'Fair - Prefabricated Fireplace in basement'), ('Po', 'Poor - Ben Franklin Stove'), ('NA', 'No Fireplace')], help_text='Fireplace quality', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Fireplaces',
            field=models.IntegerField(default=0, help_text='Number of fireplaces (Min 0 | Max 10)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Foundation',
            field=models.CharField(choices=[('BrkTil', 'Brick & Tile'), ('CBlock', 'Cinder Block'), ('PConc', 'Poured Contrete'), ('Slab', 'Slab'), ('Stone', 'Stone'), ('Wood', 'Wood')], help_text='Type of foundation', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='FullBath',
            field=models.IntegerField(default=0, help_text='Full bathrooms above grade (Min 0 | Max 10)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Functional',
            field=models.CharField(choices=[('Typ', 'Typical Functionality'), ('Min1', 'Minor Deductions 1'), ('Min2', 'Minor Deductions 2'), ('Mod', 'Moderate Deductions'), ('Maj1', 'Major Deductions 1'), ('Maj2', 'Major Deductions 2'), ('Sev', 'Severely Damaged'), ('Sal', 'Salvage only')], help_text='Home functionality (Assume typical unless deductions are warranted)', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='GarageArea',
            field=models.IntegerField(default=0, help_text='Size of garage in square feet (Min 0 | Max 2000)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(2000)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='GarageCars',
            field=models.IntegerField(default=0, help_text='Size of garage in car capacity (Min 0 | Max 10)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='GarageCond',
            field=models.CharField(choices=[('Ex', 'Excellent'), ('Gd', 'Good'), ('TA', 'Average / Typical'), ('Fa', 'Fair'), ('Po', 'Poor')], help_text='Garage conditionGarage condition', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='GarageFinish',
            field=models.CharField(choices=[('Fin', 'Finished'), ('RFn', 'Rough Finished'), ('Unf', 'Unfinished'), ('NA', 'No Garage')], help_text='Interior finish of the garage', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='GarageQual',
            field=models.CharField(choices=[('Ex', 'Excellent'), ('Gd', 'Good'), ('TA', 'Average / Typical'), ('Fa', 'Fair'), ('Po', 'Poor')], help_text='Garage quality', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='GarageType',
            field=models.CharField(choices=[('2Types', 'More than one type of garage'), ('Attchd', 'Attached to home'), ('Basment', 'Basement Garage'), ('BuiltIn', 'Built-In (Garage part of house - typically has room above garage)'), ('CarPort', 'Car Port'), ('Detchd', 'Detached from home'), ('NA', 'No Garage')], help_text='Garage location', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='GarageYrBlt',
            field=models.IntegerField(default=2019, help_text='Year garage was built', null=True, validators=[django.core.validators.MaxValueValidator(2020), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='GrLivArea',
            field=models.IntegerField(default=0, help_text='Above grade (ground) living area square feet (Min 0 | Max 6000)', null=True, validators=[django.core.validators.MaxValueValidator(6000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='HalfBath',
            field=models.IntegerField(default=0, help_text='Half baths above grade (Min 0 | Max 10)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Heating',
            field=models.CharField(choices=[('Floor', 'Floor Furnace'), ('GasA', 'Gas forced warm air furnace'), ('GasW', 'Gas hot water or steam heat'), ('Grav', 'Gravity furnace'), ('OthW', 'Hot water or steam heat other than gas'), ('Wall', 'Wall furnace')], help_text='Type of heating', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='HeatingQC',
            field=models.CharField(choices=[('Ex', 'Excellent'), ('Gd', 'Good'), ('TA', 'Average / Typical'), ('Fa', 'Fair'), ('Po', 'Poor')], help_text='Heating quality and condition', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='HouseStyle',
            field=models.CharField(choices=[('1Story', 'One story'), ('1.5Fin', 'One and one-half story | 2nd level finished'), ('1.5Unf', 'One and one-half story | 2nd level unfinished'), ('2Story', 'Two story'), ('2.5Fin', 'Two and one-half story | 2nd level finished'), ('2.5Unf', 'Two and one-half story | 2nd level unfinished'), ('SFoyer', 'Split Foyer'), ('SLvl', 'Split Level')], help_text='Style of dwelling', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='KitchenAbvGr',
            field=models.IntegerField(default=0, help_text='Kitchens above grade (Min 0 | Max 10)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='KitchenQual',
            field=models.CharField(choices=[('Ex', 'Excellent'), ('Gd', 'Good'), ('TA', 'Average / Typical'), ('Fa', 'Fair'), ('Po', 'Poor')], help_text='Kitchen quality', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='LandContour',
            field=models.CharField(choices=[('Lvl', 'Near Flat/Level'), ('Bnk', 'Quick and significant rise from street grade to building'), ('HLS', 'Significant slope from side to side'), ('low', 'Depression')], help_text='Flatness of the property', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='LandSlope',
            field=models.CharField(choices=[('Gtl', 'Gentle slope'), ('Mod', 'Moderate Slope'), ('Sev', 'Severe Slope')], help_text='Slope of property', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='LotArea',
            field=models.IntegerField(default=0, help_text='Lot size in square feet (Min 0 | Max 50000)', null=True, validators=[django.core.validators.MaxValueValidator(50000), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='LotFrontage',
            field=models.IntegerField(default=0, help_text='Linear feet of street connected to property (Min 0 | Max 500)', null=True, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='LotShape',
            field=models.CharField(choices=[('Reg', 'Regular'), ('IR1', 'Slightly irregular'), ('IR2', 'Moderately Irregular'), ('IR3', 'Irregular')], help_text='General shape of property', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='LowQualFinSF',
            field=models.IntegerField(default=0, help_text='Low quality finished square feet (all floors) (Min 0 | Max 1000)', null=True, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='MSZoning',
            field=models.CharField(choices=[('A', 'Agriculture'), ('C', 'Commercial'), ('FV', 'Floating Village Residential'), ('I', 'Industrial'), ('RH', 'Residential High Density'), ('RL', 'Residential Low Density'), ('RP', 'Residential Low Density Park'), ('RM', 'Residential Medium Density')], help_text='Identifies the general zoning classification of the sale.', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='MasVnrArea',
            field=models.IntegerField(default=0, help_text='Lot size in square feet (Min 0 | Max 3000)', null=True, validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='MasVnrType',
            field=models.CharField(choices=[('BrkCmn', 'Brick Common'), ('BrkFace', 'Brick Face'), ('CBlock', 'Cinder Block'), ('None', 'None'), ('Stone', 'Stone')], help_text='Masonry veneer type', max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='MiscFeature',
            field=models.CharField(choices=[('Elev', 'Elevator'), ('Gar2', '2nd Garage (if not described in garage section)'), ('Othr', 'Other'), ('Shed', 'Shed (over 100 SF)'), ('Tenc', 'Tennis Court'), ('NA', 'None')], help_text='Miscellaneous feature not covered in other categories', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='MiscVal',
            field=models.IntegerField(default=0, help_text='Pool area in square feet (Min 0 | Max 1000)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Neighborhood',
            field=models.CharField(choices=[('Blmngtn', 'Bloomington Heights'), ('Blueste', 'Bluestem'), ('BrDale', 'Briardale'), ('BrkSide', 'Brookside'), ('ClearCr', 'Clear Creek'), ('CollgCr', 'College Creek'), ('Crawfor', 'Crawford'), ('Edwards', 'Edwards'), ('Gilbert', 'Gilbert'), ('IDOTRR', 'Iowa DOT and Rail Road'), ('MeadowV', 'Meadow Village'), ('Mitchel', 'Mitchell'), ('Names', 'North Ames'), ('NoRidge', 'Northridge'), ('NPkVill', 'Northpark Villa'), ('NridgHt', 'Northridge Heights'), ('NWAmes', 'Northwest Ames'), ('OldTown', 'Old Town'), ('SWISU', 'South & West of Iowa State University'), ('Sawyer', 'Sawyer'), ('SawyerW', 'Sawyer West'), ('Somerst', 'Somerset'), ('StoneBr', 'Stone Brook'), ('Timber', 'Timberland'), ('Veeneker', 'Veenker')], help_text='Physical locations within Ames city limits', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='OneFlrSF',
            field=models.IntegerField(default=0, help_text='First Floor square feet (Min 0 | Max 5000)', null=True, validators=[django.core.validators.MaxValueValidator(5000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='OpenPorchSF',
            field=models.IntegerField(default=0, help_text='Open porch area in square feet (Min 0 | Max 1000)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='OverallCond',
            field=models.IntegerField(choices=[('10', 'Very Excellent'), ('9', 'Excellent'), ('8', 'Very Good'), ('7', 'Good'), ('6', 'Above Average'), ('5', 'Average'), ('4', 'Below Average'), ('3', 'Fair'), ('2', 'Poor'), ('1', 'Very Poor')], help_text='Rates the overall condition of the house', null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='OverallQual',
            field=models.IntegerField(choices=[('10', 'Very Excellent'), ('9', 'Excellent'), ('8', 'Very Good'), ('7', 'Good'), ('6', 'Above Average'), ('5', 'Average'), ('4', 'Below Average'), ('3', 'Fair'), ('2', 'Poor'), ('1', 'Very Poor')], help_text='Rates the overall material and finish of the house', null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='PavedDrive',
            field=models.CharField(choices=[('Y', 'Paved'), ('P', 'Partial Pavement'), ('N', 'Dirt / Gravel')], help_text='Paved driveway', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='PoolArea',
            field=models.IntegerField(default=0, help_text='Pool area in square feet (Min 0 | Max 1000)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='PoolQC',
            field=models.CharField(choices=[('Ex', 'Excellent'), ('Gd', 'Good'), ('TA', 'Average / Typical'), ('Fa', 'Fair'), ('Po', 'Poor')], help_text='Pool quality', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='RoofMat',
            field=models.CharField(choices=[('ClyTile', 'Clay or Tile'), ('CompShg', 'Standard (Composite) Shingle'), ('Membran', 'Membrane'), ('Metal', 'Metal'), ('Roll', 'Roll'), ('Tar&Grv', 'Gravel & Tar'), ('WdShake', 'Wood Shakes'), ('WdShngl', 'Wood Shingles')], help_text='Roof material', max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='RoofStyle',
            field=models.CharField(choices=[('Flat', 'Flat'), ('Gable', 'Gable'), ('Gambrel', 'Gabrel (Barn)'), ('Hip', 'Hip'), ('Mansard', 'Mansard'), ('Shed', 'Shed')], help_text='Type of roof', max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='ScreenPorch',
            field=models.IntegerField(default=0, help_text='Screen porch area in square feet (Min 0 | Max 1000)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='Street',
            field=models.CharField(choices=[('Grvl', 'Gravel'), ('Pave', 'Paved')], help_text='Type of road access to property', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='ThreeSsnPorch',
            field=models.IntegerField(default=0, help_text='Three season porch area in square feet (Min 0 | Max 1000)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='TotRmsAbvGrd',
            field=models.IntegerField(default=0, help_text='Total rooms above grade (does not include bathrooms) (Min 0 | Max 20)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(20)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='TotalBsmtSF',
            field=models.IntegerField(default=0, help_text='Total square feet of basement area (Min 0 | Max 6500)', null=True, validators=[django.core.validators.MaxValueValidator(6500), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='TwoFlrSF',
            field=models.IntegerField(default=0, help_text='Second floor square feet (Min 0 | Max 5000)', null=True, validators=[django.core.validators.MaxValueValidator(5000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='WoodDeckSF',
            field=models.IntegerField(default=0, help_text='Wood deck area in square feet (Min 0 | Max 1000)', null=True, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='YearBuilt',
            field=models.IntegerField(default=2019, help_text='Original construction year', null=True, validators=[django.core.validators.MaxValueValidator(2020), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='houseinformation',
            name='YearRemodAdd',
            field=models.IntegerField(default=2019, help_text='Remodel year (same as construction date if no remodeling or additions)', null=True, validators=[django.core.validators.MaxValueValidator(2020), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='houseinformation',
            name='MSSubClass',
            field=models.IntegerField(choices=[('20', '1-STORY 1946 & NEWER ALL STYLES'), ('30', '1-STORY 1945 & OLDER'), ('40', '1-STORY W/FINISHED ATTIC ALL AGES'), ('45', '1-1/2 STORY - UNFINISHED ALL AGES'), ('50', '1-1/2 STORY FINISHED ALL AGES'), ('60', '2-STORY 1946 & NEWER'), ('70', '2-STORY 1945 & OLDER'), ('75', '2-1/2 STORY ALL AGES'), ('80', 'SPLIT OR MULTI-LEVEL'), ('85', 'SPLIT FOYER'), ('90', 'DUPLEX - ALL STYLES AND AGES'), ('120', '1-STORY PUD (Planned Unit Development) - 1946 & NEWER'), ('150', '1-1/2 STORY PUD - ALL AGES'), ('160', '2-STORY PUD - 1946 & NEWER'), ('180', 'PUD - MULTILEVEL - INCL SPLIT LEV/FOYER'), ('190', '2 FAMILY CONVERSION - ALL STYLES AND AGES')], help_text='Identifies the type of dwelling involved in the sale.', null=True),
        ),
    ]

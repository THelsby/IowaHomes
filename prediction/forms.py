from django import forms
from .models import HouseInformation


class predictionForm(forms.ModelForm):
    class Meta:
        model = HouseInformation
        fields = ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 'Alley', 'LotShape', 'LandContour',
                  'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'OverallQual',
                  'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle', 'RoofMat', 'Exterior1', 'Exterior2',
                  'MasVnrType', 'MasVnrArea', 'ExterQaul', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond',
                  'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF',
                  'TotalBsmtSF', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'OneFlrSF', 'TwoFlrSF',
                  'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
                  'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu',
                  'GarageType', 'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond',
                  'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', 'ThreeSsnPorch', 'ScreenPorch',
                  'PoolArea', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal']
        widgets = {
            'MSSubClass': forms.Select(attrs={'class': 'form-control'}),
            'MSZoning': forms.Select(attrs={'class': 'form-control'}),
            'LotFrontage': forms.NumberInput(attrs={'class': 'form-control'}),
            'LotArea': forms.NumberInput(attrs={'class': 'form-control'}),
            'Street': forms.Select(attrs={'class': 'form-control'}),
            'Alley': forms.Select(attrs={'class': 'form-control'}),
            'LotShape': forms.Select(attrs={'class': 'form-control'}),
            'LandContour': forms.Select(attrs={'class': 'form-control'}),
            'LandSlope': forms.Select(attrs={'class': 'form-control'}),
            'Neighborhood': forms.Select(attrs={'class': 'form-control'}),
            'Condition1': forms.Select(attrs={'class': 'form-control'}),
            'Condition2': forms.Select(attrs={'class': 'form-control'}),
            'BldgType': forms.Select(attrs={'class': 'form-control'}),
            'HouseStyle': forms.Select(attrs={'class': 'form-control'}),
            'OverallQual': forms.Select(attrs={'class': 'form-control'}),
            'OverallCond': forms.Select(attrs={'class': 'form-control'}),
            'YearBuilt': forms.NumberInput(attrs={'class': 'form-control'}),
            'RoofStyle': forms.Select(attrs={'class': 'form-control'}),
            'RoofMat': forms.Select(attrs={'class': 'form-control'}),
            'Exterior1': forms.Select(attrs={'class': 'form-control'}),
            'Exterior2': forms.Select(attrs={'class': 'form-control'}),
            'MasVnrType': forms.Select(attrs={'class': 'form-control'}),
            'MasVnrArea': forms.NumberInput(attrs={'class': 'form-control'}),
            'ExterQaul': forms.Select(attrs={'class': 'form-control'}),
            'ExterCond': forms.Select(attrs={'class': 'form-control'}),
            'Foundation': forms.Select(attrs={'class': 'form-control'}),
            'BsmtQual': forms.Select(attrs={'class': 'form-control'}),
            'BsmtCond': forms.Select(attrs={'class': 'form-control'}),
            'BsmtExposure': forms.Select(attrs={'class': 'form-control'}),
            'BsmtFinType1': forms.Select(attrs={'class': 'form-control'}),
            'BsmtFinSF1': forms.NumberInput(attrs={'class': 'form-control'}),
            'BsmtFinType2': forms.Select(attrs={'class': 'form-control'}),
            'BsmtFinSF2': forms.NumberInput(attrs={'class': 'form-control'}),
            'BsmtUnfSF': forms.NumberInput(attrs={'class': 'form-control'}),
            'TotalBsmtSF': forms.NumberInput(attrs={'class': 'form-control'}),
            'Heating': forms.Select(attrs={'class': 'form-control'}),
            'HeatingQC': forms.Select(attrs={'class': 'form-control'}),
            'CentralAir': forms.Select(attrs={'class': 'form-control'}),
            'Electrical': forms.Select(attrs={'class': 'form-control'}),
            'OneFlrSF': forms.NumberInput(attrs={'class': 'form-control'}),
            'TwoFlrSF': forms.NumberInput(attrs={'class': 'form-control'}),
            'LowQualFinSF': forms.NumberInput(attrs={'class': 'form-control'}),
            'GrLivArea': forms.NumberInput(attrs={'class': 'form-control'}),
            'BsmtFullBath': forms.NumberInput(attrs={'class': 'form-control'}),
            'BsmtHalfBath': forms.NumberInput(attrs={'class': 'form-control'}),
            'FullBath': forms.NumberInput(attrs={'class': 'form-control'}),
            'HalfBath': forms.NumberInput(attrs={'class': 'form-control'}),
            'BedroomAbvGr': forms.NumberInput(attrs={'class': 'form-control'}),
            'KitchenAbvGr': forms.NumberInput(attrs={'class': 'form-control'}),
            'KitchenQual': forms.Select(attrs={'class': 'form-control'}),
            'TotRmsAbvGrd': forms.NumberInput(attrs={'class': 'form-control'}),
            'Functional': forms.Select(attrs={'class': 'form-control'}),
            'Fireplaces': forms.NumberInput(attrs={'class': 'form-control'}),
            'FireplaceQu': forms.Select(attrs={'class': 'form-control'}),
            'GarageType': forms.Select(attrs={'class': 'form-control'}),
            'GarageYrBlt': forms.NumberInput(attrs={'class': 'form-control'}),
            'GarageFinish': forms.Select(attrs={'class': 'form-control'}),
            'GarageCars': forms.NumberInput(attrs={'class': 'form-control'}),
            'GarageArea': forms.NumberInput(attrs={'class': 'form-control'}),
            'GarageQual': forms.Select(attrs={'class': 'form-control'}),
            'GarageCond': forms.Select(attrs={'class': 'form-control'}),
            'PavedDrive': forms.Select(attrs={'class': 'form-control'}),
            'WoodDeckSF': forms.NumberInput(attrs={'class': 'form-control'}),
            'OpenPorchSF': forms.NumberInput(attrs={'class': 'form-control'}),
            'EnclosedPorch': forms.NumberInput(attrs={'class': 'form-control'}),
            'ThreeSsnPorch': forms.NumberInput(attrs={'class': 'form-control'}),
            'ScreenPorch': forms.NumberInput(attrs={'class': 'form-control'}),
            'PoolArea': forms.NumberInput(attrs={'class': 'form-control'}),
            'PoolQC': forms.Select(attrs={'class': 'form-control'}),
            'Fence': forms.Select(attrs={'class': 'form-control'}),
            'MiscFeature': forms.Select(attrs={'class': 'form-control'}),
            'MiscVal': forms.NumberInput(attrs={'class': 'form-control'}),
        }

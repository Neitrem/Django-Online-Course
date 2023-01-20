
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def correct_string_length(value, threshold):
    if len(value) < threshold:
        raise ValidationError(
            _('| %(value)s | is to short to be a password. Min length is %(threshold)d'),
            params={'value': value, 'threshold': threshold},
        )
        
def correct_age_value(value, threshold):
    if value:  
        if value < threshold:
            raise ValidationError('Users under 16 are not allowed')
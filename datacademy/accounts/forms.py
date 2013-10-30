from userena.utils import get_profile_model
from userena.forms import EditProfileForm


# Override to exclude specific fields
class EditDatacademyProfileForm(EditProfileForm):
    class Meta:
        model = get_profile_model()
        exclude = ('user', 'courses', 'lectures', 'exercises', )

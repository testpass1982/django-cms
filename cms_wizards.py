from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool

from .forms import PostWizardForm

class MyAppWizard(Wizard):
    def get_success_url(self, obj, **kwargs):
    """
    This should return the URL of the created object, «obj».
    """
        if 'language' in kwargs:
            with force_language(kwargs['language']):
                url = obj.get_absolute_url()
        else:
            url = obj.get_absolute_url()

        return url

my_app_wizard = MyAppWizard(
    title = 'POST WIZARD',
    weight=200,
    form = PostWizardForm
    description = 'POST CREATION FORM'
)

wizard_pool.register(my_app_wizard)
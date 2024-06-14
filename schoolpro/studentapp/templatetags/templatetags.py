# your_app/templatetags/custom_tags.py
# your_app/templatetags/custom_tags.py
# your_app/templatetags/custom_tags.py

from django import template
from teacherapp.models import UploadFile

register = template.Library()

@register.simple_tag
def get_file_name(fid):
        upld_file = UploadFile.objects.get(id=fid)
        
        return upld_file.filename
   
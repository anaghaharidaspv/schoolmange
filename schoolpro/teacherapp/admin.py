from django.contrib import admin
from .models import excelupload
from import_export.admin import ImportExportModelAdmin
from import_export import resources

admin.site.register(excelupload,ImportExportModelAdmin)
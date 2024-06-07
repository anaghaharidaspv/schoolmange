from datetime import datetime
from django.db import models
from adminapp.models import *

# Create your models here.
class TeacherAttendance(models.Model):
    date = models.DateField()
    teacher_name = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    break_start_time = models.TimeField()
    break_end_time = models.TimeField()
    
    def get_total_working_hours(self):
        """
        Calculate the total working hours excluding break time.
        """
        if None in (self.date, self.arrival_time, self.departure_time, self.break_start_time, self.break_end_time):
            return "N/A"  # Return "N/A" if any of the time fields is None
        arrival = datetime.combine(self.date, self.arrival_time)
        departure = datetime.combine(self.date, self.departure_time)
        break_start = datetime.combine(self.date, self.break_start_time)
        break_end = datetime.combine(self.date, self.break_end_time)
        total_working_time = departure - arrival
        break_time = break_end - break_start
        
        net_working_time = total_working_time - break_time
        return net_working_time.total_seconds() / 3600  # Return hours
    def get_break_time(self):
        """
        
        Calculate the total break time.
        """
        if None in (self.date, self.break_start_time, self.break_end_time):
            return "N/A"  # Return "N/A" if any of the time fields is None
        break_start = datetime.combine(self.date, self.break_start_time)
        break_end = datetime.combine(self.date, self.break_end_time)
        break_time = break_end - break_start
        return break_time.total_seconds() / 3600  # Return hours
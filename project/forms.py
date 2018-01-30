from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
import datetime
from django.forms import modelformset_factory
from .models import *
from django.forms import ModelForm, Textarea,TextInput,DateField
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelChoiceField


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': _('User Name')}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':_('Password')}))
class EmployeeList(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.empname
        
class AddNewSheet(forms.Form):
    TaskDesc = forms.CharField(label=_("Task Descreption"),
               widget=forms.TextInput({'class': 'form-control','placeholder': 'وصف المهمة كامل'}))

    TaskType = forms.ChoiceField(choices=(('M', _('Master')), ('H', _('Help'))),label=_("Task type"),
                    widget=forms.Select({'class': 'form-control','placeholder':'task'}))
    Duration = forms.IntegerField(label=_("Duration"),
               widget=forms.NumberInput({'class': 'form-control','placeholder':'0'}))

UpdateSheet = modelformset_factory(Sheet, fields=('taskdesc', 'tasktype', 'duration'))

class FilterSheet(forms.Form):
    tasktype = forms.ChoiceField(choices=(("", _('')),('M', _('Master')), ('H', _('Help'))),label=_("Task type"),required=False,
                    widget=forms.Select({'class': 'form-control','placeholder':'task'}))
    tasksubmitted= forms.ChoiceField(choices=(
        ("", _('')),
        ('0', _('New')),
        ('1', _('submitted')),
        ('2', _('not submitted')),
    ),required=False,label=_("Status submitted"),widget=forms.Select({'class': 'form-control cust','placeholder':'task'}))
    taskstatus= forms.ChoiceField(choices=(
    ("", _('')),
        ('1', _('in progres')),
        ('2', _('Done')),
        ('3', _('Ignore')),
    ),required=False,label=_("Status task"),widget=forms.Select({'class': 'form-control','placeholder':'task'}))

class SheetForm(ModelForm):
    model = Sheet

class ProjectForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = None
        self.fields['name'].widget.attrs['maxlength'] =255

    class Meta:
        model = Project
        fields = ['name','start','status','end','desc']
       # status = models.ForeignKey(ProjectStatus, widget=forms.Select({'class': 'form-control','placeholder':'task'}) )
        widgets = {
            'name':TextInput(attrs={'class': 'form-control','placeholder':_('Project Name'),'required': True}),
            'start':TextInput(attrs={'class': 'form-control has-feedback-left col-md-3 col-sm-9 col-xs-12 ','id':'single_cal_1','aria-describedby':'inputSuccess2Status','placeholder':_('Start Date'),'required': True}),
            'end':TextInput(attrs={'class': 'form-control has-feedback-left col-md-6 ','id':'single_cal_2','aria-describedby':'inputSuccess2Status','placeholder':_('End Date'),'required': True}),
            'desc': Textarea(attrs={'class':'form-control','placeholder':_('Project Details'),'required': True}),
            'status':forms.Select(attrs={'class': 'form-control','placeholder':_('Select Status')})



        }

        labels = {
            'name': _('Project Name'),
            'status': _('Status'),
            'start':_('Start Date'),
            'end':_('End Date'),
            'desc':_('Project Description'),
        }
        help_texts = {
            'desc': _('write a Description for Project .'),
            'start':_('Please use the following format: <em>YYYY-MM-DD</em>.'),
            'end':_('Please use the following format: <em>YYYY-MM-DD</em>.'),
        }
        error_messages = {
            'name': {
                    'max_length': _("The Project's name is too long."),
                    'required': _("Project's name is required."),
             },
            'start': {
                    'required': _("Start Date  is required."),
             },
            'end': {
                    'required': _("End Date  is required."),
             },
            'desc': {
                    'max_length': _("The Project's Description is too long."),
                    'required': _("Description is required."),
             },

        }
        
  

class TaskStartForm(forms.Form):
       rsd = forms.DateField(label=_("Real Start Date"),
       widget=forms.DateInput(attrs={'class': 'form-control has-feedback-left col-md-3 col-sm-9 col-xs-12 ','id':'single_cal_1','aria-describedby':'inputSuccess2Status','placeholder':_('Real Start Date'),'required': True}))
       notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','label':'Notes', 'size': '40','required': False}), required=False,error_messages={'required': 'note'})
              
class TaskFinishForm(forms.Form):
       ftime = forms.DateField(label=_("Finished on"),
       widget=forms.DateInput(attrs={'class': 'form-control has-feedback-left col-md-3 col-sm-9 col-xs-12 ','id':'single_cal_1','aria-describedby':'inputSuccess2Status','placeholder':_('Finished on Date'),'required': True}))
       notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','label':'Notes', 'size': '40','required': False}), required=False,error_messages={'required': 'notes'})                     
   
class TaskCloseForm(forms.Form):
       ctime = forms.DateField(label=_("Closed on"),
       widget=forms.DateInput(attrs={'class': 'form-control has-feedback-left col-md-3 col-sm-9 col-xs-12 ','id':'single_cal_1','aria-describedby':'inputSuccess2Status','placeholder':_('Closed on Date'),'required': True}))
       notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','label':'Notes', 'size': '40','required': True}),required=True, max_length=500, error_messages={'required': 'note'})                     

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.empname
    
class TeamForm(forms.Form):
      employee = MyModelChoiceField(queryset=Employee.objects.all(), empty_label="(Nothing)",widget=forms.Select(attrs={'class': 'chosen'} ))

    
class AddDelegation(ModelForm):
    employee = EmployeeList(queryset=Employee.objects.all(),to_field_name="empid",label=_("Delegation to"), empty_label=_("Nothing"),required=True,widget=forms.Select(attrs={'class': 'chosen form-control'} ))
    class Meta:
        model = Delegation
        fields = ['employee','start','end']
        widgets = {
            # 'authorized':TextInput(attrs={'class': 'form-control','placeholder':_('Employee name'),'required': True}),
            'start':TextInput(attrs={'class': 'form-control has-feedback-left col-md-3 col-sm-9 col-xs-12 ','id':'single_cal_1','aria-describedby':'inputSuccess2Status','placeholder':_('Start Date'),'required': True}),
            'end':TextInput(attrs={'class': 'form-control has-feedback-left col-md-6 ','id':'single_cal_2','aria-describedby':'inputSuccess2Status','placeholder':_('End Date'),'required': True}),
        }
        labels = {
            'start':_('start Delegation'),
            'end':_('End Delegation'),
        },
    def clean(self):
        cleaned_data = super().clean()
        end = cleaned_data.get("end")
        start = cleaned_data.get("start")
        #Check end date less than start date
        if end < start:
            msg = _("End date is less than start date")
            self.add_error('end', msg)
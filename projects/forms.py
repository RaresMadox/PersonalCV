from django import forms
from django.db.models import fields
from .models import Project

class CreateProject(forms.ModelForm):
    class Meta:
        model=Project
        fields =['title','descrtion','slug','thumb',
        'thumb1','thumb2','thumb3','category','tags']

class UpdateProject(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'
        exclude=['slug']
        # fields=['title','descrtion','thumb',
        # 'thumb1','thumb2','thumb3','category','tags']

        # def save(self,comit=True):
        #     project_post=self.instace
        #     project_post.title=self.cleaned_data['title']
        #     project_post.description=self.cleaned_data['description']
        #     project_post.thumb=self.cleaned_data['thumb']
        #     project_post.thumb1=self.cleaned_data['thumb1']
        #     project_post.thumb2=self.cleaned_data['thumb2']
        #     project_post.thumb3=self.cleaned_data['thumb3']
        #     project_post.category=self.cleaned_data['category']
        #     project_post.tags=self.cleaned_data['tags']
        #     if self.cleaned_data['thumb']:
        #         project_post.thumb=self.cleaned_data['thumb']
        #     if self.cleaned_data['thumb1']:
        #         project_post.thumb1=self.cleaned_data['thumb1']
        #     if self.cleaned_data['thumb2']:
        #         project_post.thumb2=self.cleaned_data['thumb2']
        #     if self.cleaned_data['thumb3']:
        #         project_post.thumb3=self.cleaned_data['thumb3']
            
        #     if comit:
        #         project_post.save()
        #     return project_post





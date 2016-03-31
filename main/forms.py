from django import forms

from main.models import BlogPost


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = (
            "text",
            "image",
            "publish_date",
        )
        widgets = {
            'publish_date': forms.SelectDateWidget,
        }

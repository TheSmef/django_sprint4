from django import forms

from blog.models import Comment, Post


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(
                format='%d/%m/%Y %H:%M',
                attrs={'type': 'datetime-local'}
            )
        }

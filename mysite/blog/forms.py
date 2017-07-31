from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('author','title','text')

        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}), #textinputclass is a user defined class
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}) #postcontent is a user defined class
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')

        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}) #postcontent is a user defined class
        }

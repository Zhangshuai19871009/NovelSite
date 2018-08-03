from django import forms

class ReportErrorForm(forms.Form):
    title = forms.CharField(
        label='标题',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    content = forms.CharField(
        label='内容',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ReportErrorForm, self).__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if title == '':
            raise forms.ValidationError('标题不能为空')
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if content == '':
            raise forms.ValidationError('内容不能为空')
        return content

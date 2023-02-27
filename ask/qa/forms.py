from django import forms

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}), required=False)

    def clean(self):
        if not (self.cleaned_data.get('title') and self.cleaned_data.get('text')):
            raise forms.ValidationError('Fields must be filled!')

    def save(self):
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}), required=False)
    question = forms.ModelChoiceField(Question.objects.all(), empty_label='Not selected')

    def clean(self):
        if not self.cleaned_data.get('text'):
            raise forms.ValidationError('Fields must be filled!')

    def save(self):
        return Answer.objects.create(**self.cleaned_data)

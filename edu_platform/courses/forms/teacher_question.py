from django import forms


class TeacherQuestionForm(forms.Form):
    name = forms.CharField(label="Ім'я", max_length=100)
    email = forms.EmailField(label="Email")
    question = forms.CharField(min_length=10, label="Питання", widget=forms.Textarea)

    def clean_question(self):
        clean_question = self.cleaned_data['question']

        if '???' in clean_question:
            raise forms.ValidationError('Можна будь-ласка без трьох знаків питання?')

        return clean_question



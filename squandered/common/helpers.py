class RemoveHelpTextMixin:
    fields = {}

    def _remove_help_text(self):
        for _, field in self.fields.items():
            field.help_text = None


class BootstrapFormMixin:
    fields = {}

    def _apply_form_control(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'

from flask import abort, flash
from flask_login import login_required, current_user
from appname.models import Widget


class LoginRequiredMixin(object):
    decorators = [login_required]


class WidgetAccessMixin(LoginRequiredMixin):
    widget = None

    def dispatch_request(self, *args, **kwargs):
        if 'widget_id' in kwargs:
            self.widget = Widget.query.get(kwargs['widget_id'])
            if self.widget and not current_user == self.widget.user:
                flash("Access Denied", "danger")
                abort(401)
        return super(WidgetAccessMixin, self).dispatch_request(*args, **kwargs)

    def get_context_data(self, **context):
        context = super(WidgetAccessMixin, self).get_context_data(**context)
        context['widget'] = self.widget
        return context
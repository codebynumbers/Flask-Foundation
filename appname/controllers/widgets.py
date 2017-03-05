from flask import Blueprint, url_for, flash
from flask_login import current_user

from fifty_flask.views.generic import url_rule, FormView
from fifty_tables import NumericColumn, LinkColumn
from fifty_tables.views import SQLAlchemyTableView

from appname.controllers.mixins import WidgetAccessMixin, LoginRequiredMixin
from appname.forms.widget import WidgetForm
from appname.models.widget import Widget

widgets_bp = Blueprint('widgets', __name__, url_prefix='/widgets')


@url_rule(widgets_bp, ['/<widget_id>/edit/', '/edit/'], 'edit')
class WidgetEditView(WidgetAccessMixin, FormView):

    template_name = "widget_edit.html"
    form_cls = WidgetForm

    def _get_widget(self):
        """ Get the model to save.
            Could be new in case of create, or existing.
        """
        if not self.widget:
            self.widget = Widget()
        return self.widget

    def get_form_obj(self):
        return self.widget

    def get_redirect_url(self):
        return url_for('.edit', widget_id=self.widget.id)

    def form_valid(self, form, **context):
        widget = self._get_widget()
        form.populate_obj(widget)
        widget.user = current_user
        widget.save()
        self.widget = widget
        flash("widget saved", "success")
        return super(WidgetEditView, self).form_valid(form, **context)

    def form_invalid(self, form, **context):
        flash("Error saving widget", "danger")
        return super(WidgetEditView, self).form_invalid(form, **context)


@url_rule(widgets_bp, '/', 'list')
class WidgetListView(LoginRequiredMixin, SQLAlchemyTableView):
    template_name = 'widget_list.html'
    default_sort = 'id'
    default_sort_direction = 'asc'

    def get_table_columns(self, params=None, **context):
        return [
            NumericColumn(name='id', label='ID', int_format='{:}'),
            LinkColumn(name='name', label="Name",
                       endpoint='.edit', url_params={'widget_id': 'id'}),
        ]

    def get_query(self, params, **context):
        return Widget.query.filter_by(user=current_user)

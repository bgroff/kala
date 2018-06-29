from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView

from documents.models import Document
from projects.models import Project
from projects.forms.documents.settings.details import DetailsForm


class DocumentDetailsView(LoginRequiredMixin, TemplateView):
    template_name = 'documents/settings/details.html'

    def get_context_data(self, **kwargs):
        return {
            'form': self.form,
            'document': self.document,
            'project': self.project,
            'organization': self.project.organization,
            'can_create': self.project.has_change(self.request.user) or self.project.has_create(self.request.user),
            'can_invite': self.project.organization.has_change(self.request.user) or self.project.organization.has_create(self.request.user)

        }

    def dispatch(self, request, project_pk, document_pk, *args, **kwargs):
        self.project = get_object_or_404(Project.objects.active(), pk=project_pk)
        self.document = get_object_or_404(Document.objects.active(), pk=document_pk)

        if not self.document.has_change(request.user):
            raise PermissionDenied('You do not have permission to edit this project')

        self.form = DetailsForm(request.POST or None, instance=self.document, project=self.project)
        return super(DocumentDetailsView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            self.form.save(commit=False)
            self.form.save_m2m()
            self.form.save()
            messages.success(request, 'The document has been updated.')
            return redirect(reverse('projects:document_details', args=[self.project.pk, self.document.pk]))
        return self.render_to_response(self.get_context_data())

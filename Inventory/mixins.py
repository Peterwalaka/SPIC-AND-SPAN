from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


class GeneratePdfMixin:
    pdf_template = None
    pdf_data = None  # Model data
    pdf_name = None

    def get_pdf_data(self):
        return self.pdf_data

    def get_pdf_name(self):
        return self.pdf_name

    def generate_pdf(self):
        """Generate pdf."""
        # Rendered
        html_string = render_to_string(self.pdf_template, self.get_pdf_data())
        html = HTML(string=html_string)
        result = html.write_pdf()
        # Creating http response
        response = HttpResponse(result, content_type='application/pdf;')
        response['Content-Disposition'] = f"inline; filename={self.get_pdf_name()}.pdf "
        return response

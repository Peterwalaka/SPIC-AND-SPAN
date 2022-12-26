from django.shortcuts import get_object_or_404
from django.views import View

from Inventory.mixins import GeneratePdfMixin
from carts.models import Order


class OrderPdfView(GeneratePdfMixin, View):
    pdf_template = "receipts/order-pdf.html"

    def get_object(self):
        order = get_object_or_404(Order, pk=self.kwargs.get("pk"))
        return order

    def get_pdf_name(self):
        super().get_pdf_name()
        return f"order-{self.get_object().order_id}"

    def get_pdf_data(self):
        super().get_pdf_data()
        return {"order": self.get_object()}

    def get(self, *args, **kwargs):
        return self.generate_pdf()

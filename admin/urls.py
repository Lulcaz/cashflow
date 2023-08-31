from django.urls import re_path

import admin.views as views

urlpatterns = [
    re_path(r'^$', views.index, name='admin-index'),

    re_path(r'^confirm/$', views.confirm_overview, name='admin-confirm'),
    re_path(r'^attest/$', views.attest_overview, name='admin-attest'),
    re_path(r'^pay/$', views.pay_overview, name='admin-pay'),
    re_path(r'^account/$', views.account_overview, name='admin-account'),

    re_path(r'^expense/(?P<pk>\d+)/verification/edit/$', views.edit_expense_verification, name='admin-expense-edit-verification'),
    re_path(r'^expense/(?P<expense_pk>\d+)/verification/$', views.set_verification, name='admin-expense-verification'),
    re_path(r'^expense/(?P<pk>\d+)/confirm/$', views.confirm_expense, name='admin-expense-confirm'),

    re_path(r'^invoice/(?P<invoice_pk>\d+)/verification/$', views.invoice_set_verification, name='admin-invoice-verification'),

    re_path(r'^expense-part/(?P<pk>\d+)/attest/$', views.attest_expense_part, name='admin-expensepart-attest'),
    re_path(r'^invoice-part/(?P<pk>\d+)/attest/$', views.attest_invoice_part, name='admin-invoicepart-attest'),

    re_path(r'^expenses/$', views.expense_overview, name='admin-expense-overview'),
    re_path(r'^invoices/$', views.invoice_overview, name='admin-invoice-overview'),
    re_path(r'^invoices/(?P<pk>\d+)/pay$', views.invoice_pay, name='admin-invoice-pay'),
    re_path(r'^verifications/$', views.search_verification, name='admin-search-verification'),
    re_path(r'^verifications/search/$', views.search_verification_response, name='admin-search-verification-api'),
    re_path(r'^verifications/list$', views.list_verification, name='admin-list-verification'),
    re_path(r'^users/$', views.user_overview, name='admin-user-overview'),
]

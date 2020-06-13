from django.urls import path, include
from . import  views

urlpatterns = [
    path("scrape_msnbc", views.scrape_msnbc, name="scrape_msnbc"),
    path("scrape_cnn", views.scrape_cnn, name="scrape_cnn"),
    path("scrape_fox", views.scrape_fox, name="scrape_fox"),
    # path("s3_upload", views.s3_upload, name="s3_upload"),       # Currently only for s3 testing
    path("del_ms_files", views.del_ms_files, name="del_ms_files"),
    path("del_cnn_files", views.del_cnn_files, name="del_cnn_files"),
    path("del_fox_files", views.del_fox_files, name="del_fox_files"),
    # path("fetch_MSNBC_file", views.fetch_MSNBC_file, name="fetch_MSNBC_file"),      # Currently only for s3 testing
    # path("fetch_CNN_file", views.fetch_CNN_file, name="fetch_CNN_file"),        # Currently only for s3 testing
    # path("fetch_FOX_file", views.fetch_FOX_file, name="fetch_FOX_file"),        # Currently only for s3 testing
]
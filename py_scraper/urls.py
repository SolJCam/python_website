from django.urls import path, include
from . import  views

urlpatterns = [
    path("scrape_msnbc", views.scrape_msnbc, name="scrape_msnbc"),
    path("scrape_cnn", views.scrape_cnn, name="scrape_cnn"),
    path("scrape_fox", views.scrape_fox, name="scrape_fox"),
    path("top_fox_wrds", views.top_fox_wrds, name="top_fox_wrds"),
    path("top_cnn_wrds", views.top_cnn_wrds, name="top_cnn_wrds"),
    path("top_msnbc_wrds", views.top_msnbc_wrds, name="top_msnbc_wrds"),
    # path("s3_upload", views.s3_upload, name="s3_upload"),       # Currently only for s3 testing
    path("msnbc_img", views.msnbc_img, name="msnbc_img"),
    path("cnn_img", views.cnn_img, name="cnn_img"),
    path("fox_img", views.fox_img, name="fox_img"),
    path("del_msnbc_files", views.del_msnbc_files, name="del_msnbc_files"),
    path("del_cnn_files", views.del_cnn_files, name="del_cnn_files"),
    path("del_fox_files", views.del_fox_files, name="del_fox_files"),
    # path("fetch_MSNBC_file", views.fetch_MSNBC_file, name="fetch_MSNBC_file"),      # Currently only for s3 testing
    # path("fetch_CNN_file", views.fetch_CNN_file, name="fetch_CNN_file"),        # Currently only for s3 testing
    # path("fetch_FOX_file", views.fetch_FOX_file, name="fetch_FOX_file"),        # Currently only for s3 testing
]
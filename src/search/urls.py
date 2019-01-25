
from django.conf.urls import url


from bookstore.views import ( 
    ProductListView, 
    #product_list_view,
    #ProductDetailView,
    ProductDetailSlugView,
    #product_detail_view,
    #ProductFeaturedListView,
    #ProductFeaturedDetailView
    
    )


urlpatterns = [

    url(r'^$', ProductListView.as_view()),
    

]
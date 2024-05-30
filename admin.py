from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from models import Vendor, Product, Review, Recommendation, Inventory, Shipping, Loyalty, Analytics, Social, Chatbot, Verification, Mobile, Gamification, Marketing

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

admin = Admin(name='FitriVendorHub', index_view=MyAdminIndexView())

admin.add_view(ModelView(Vendor, schema=VendorSchema))
admin.add_view(ModelView(Product, schema=ProductSchema))
admin.add_view(ModelView(Review, schema=ReviewSchema))
admin.add_view(ModelView(Recommendation, schema=RecommendationSchema))admin.add_view(ModelView(Inventory, schema=InventorySchema))
admin.add_view(ModelView(Shipping, schema=ShippingSchema))
admin.add_view(ModelView(Loyalty, schema=LoyaltySchema))
admin.add_view(ModelView(Analytics, schema=AnalyticsSchema))
admin.add_view(ModelView(Social, schema=SocialSchema))
admin.add_view(ModelView(Chatbot, schema=ChatbotSchema))
admin.add_view(ModelView(Verification, schema=VerificationSchema))
admin.add_view(ModelView(Mobile, schema=MobileSchema))
admin.add_view(ModelView(Gamification, schema=GamificationSchema))
admin.add_view(ModelView(Marketing, schema=MarketingSchema))

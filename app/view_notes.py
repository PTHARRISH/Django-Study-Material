# Notes:
# many=True:
# The many=True parameter is essential
# when serializing collections of objects rather than a single instance.
# Here are comprehensive real-world examples:

# Output: List of product dictionaries
# [
#   {'id': 1, 'name': 'iPhone 15', 'price': 999.99, 'category': 'Electronics'},
#   {'id': 2, 'name': 'Samsung Galaxy S24', 'price': 899.99,
#       'category': 'Electronics'},
#   {'id': 3, 'name': 'MacBook Pro', 'price': 1999.99, 'category': 'Computers'}
# ]


# Responses- Response(data)
# https://www.django-rest-framework.org/api-guide/responses/

# function-based-views - @api_view
# https://www.django-rest-framework.org/api-guide/views/#function-based-views

# The Browsable API
# Format- ?format=
# https://www.django-rest-framework.org/topics/browsable-api/#formats


# Renderers
# REST framework includes a number of built in Renderer classes,
# that allow you to return responses with various media types.
# There is also support for defining your own custom renderers,
# which gives you the flexibility to design your own media types.

# 1.JSONRenderer
#  display json data
# 2.TemplateHTMLRenderer
#  inside a class renderer_classes = [TemplateHTMLRenderer]
#  via Response we can assign template html file
# 3.StaticHTMLRenderer
#  by using this decorator @renderer_classes([StaticHTMLRenderer])
#  inside variable
#  we can assign html tags and we can render the response
# 4.BrowsableAPIRenderer
#  Renders data into HTML for the Browsable API in built view
# 5.AdminRenderer
#  Renders data into HTML for an admin-like display for seializers
# 6.HTMLFormRenderer
#  Renders data returned by a serializer into an HTML form.
# 7.MultiPartRenderer
#  Renderer is used for rendering HTML multipart form data file upload concept.
# 8.Custom renderers


# JSONRenderer
# Renders the request data into JSON, using utf-8 encoding.

# Note that the default style is to include unicode characters,
# and render the response using a compact style with no unnecessary whitespace:

# {"unicode black star":"★","value":999}
# The client may additionally include an 'indent' media type parameter,
# in which case the returned JSON will be indented.
# For example: Accept: application/json;
#              indent=4.


# TemplateHTMLRenderer:-
# Renders data to HTML, using Django's standard template rendering.
# Unlike other renderers,
# the data passed to the Response does not need to be serialized.
# Also, unlike other renderers,
# you may want to include a template_name argument when creating the Response.
# The TemplateHTMLRenderer will create a RequestContext,
# using the response.data as the context dict,
# and determine a template name to use to render the context.

# class UserDetail(generics.RetrieveAPIView):
#     """
#     A view that returns a templated HTML representation of a given user.
#     """
#     queryset = User.objects.all()
#     renderer_classes = [TemplateHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return Response({'user': self.object},
#                           template_name='user_detail.html')

# You can use TemplateHTMLRenderer either to return regular HTML pages
# using REST framework,
# or to return both HTML and API responses from a single endpoint.


# StaticHTMLRenderer:-
# A simple renderer that simply returns pre-rendered HTML.
# Unlike other renderers, the data passed
# to the response object should be a string representing
# the content to be returned.

# An example of a view that uses StaticHTMLRenderer:

# @api_view(['GET'])
# @renderer_classes([StaticHTMLRenderer])
# def simple_html_view(request):
#     data = '<html><body><h1>Hello, world</h1></body></html>'
#     return Response(data)


# BrowsableAPIRenderer:-(Response)
# Renders data into HTML for the Browsable API
# This renderer will determine which other renderer
# would have been given highest priority, and use that to display an API style
# response within the HTML page.

# AdminRenderer
# Renders data into HTML for an admin-like display:
# This renderer is suitable for CRUD-style web APIs
# that should also present a user-friendly interface for managing the data.
# Note that views that have nested or list serializers
# for their input won't work well with the AdminRenderer,
# as the HTML forms are unable to properly support them.

# Note:
# The AdminRenderer is only able to include links to detail pages
# when a properly configured URL_FIELD_NAME (url by default)
# attribute is present in the data.
# For HyperlinkedModelSerializer this will be the case,
# but for ModelSerializer or plain Serializer classes
# you'll need to make sure to include the field explicitly.
# For example here we use models get_absolute_url method:

# class AccountSerializer(serializers.ModelSerializer):
#     url = serializers.CharField(source='get_absolute_url', read_only=True)

#     class Meta:
#         model = Account
# .media_type: text/html

# .format: 'admin'

# .charset: utf-8

# .template: 'rest_framework/admin.html'

# HTMLFormRenderer
# Renders data returned by a serializer into an HTML form.
# The output of this renderer does not include the enclosing <form> tags,
# a hidden CSRF input or any submit buttons.

# This renderer is not intended to be used directly,
# but can instead be used in templates by passing a serializer
# instance to the render_form template tag.

# {% load rest_framework %}

# <form action="/submit-report/" method="post">
#     {% csrf_token %}
#     {% render_form serializer %}
#     <input type="submit" value="Save" />
# </form>
# For more information see the HTML & Forms documentation.

# .media_type: text/html

# .format: 'form'

# .charset: utf-8

# .template: 'rest_framework/horizontal/form.html'

# MultiPartRenderer
# This renderer is used for rendering HTML multipart form data.
# It is not suitable as a response renderer,
# but is instead used for creating test requests,
# using REST framework's test client and test request factory.

# .media_type: multipart/form-data; boundary=BoUnDaRyStRiNg

# .format: 'multipart'

# .charset: utf-8


# Custom renderers
# To implement a custom renderer,
# you should override BaseRenderer, set the .media_type and .format properties,
# and implement the
# .render(self, data, accepted_media_type=None, renderer_context=None) method.

# The method should return a bytestring,
# which will be used as the body of the HTTP response.

# The arguments passed to the .render() method are:

# data
# The request data, as set by the Response() instantiation.

# accepted_media_type=None
# Example
# The following is an example plaintext renderer
# that will return a response with the data parameter
# as the content of the response.

# from django.utils.encoding import smart_str
# from rest_framework import renderers


# class PlainTextRenderer(renderers.BaseRenderer):
#     media_type = 'text/plain'
#     format = 'txt'

#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         return smart_str(data, encoding=self.charset)

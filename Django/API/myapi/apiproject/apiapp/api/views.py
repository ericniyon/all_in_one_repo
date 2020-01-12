from django.db.models import Q
from rest_framework import generics,mixins
from apiapp.models import BlogPost

from .permissions import IsOwnerOrReadOnly
from .serializers import BlogPostSerializer



class BlogPostAPIView( mixins.CreateModelMixin ,generics.ListAPIView):
	pass
	lookup_field = 'pk'
	serializer_class = BlogPostSerializer
	permission_classes=[IsOwnerOrReadOnly]

	# queryset= BlogPost.objects.all()

	def get_queryset(self):
		qs = BlogPost.objects.all()
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(
				Q(title__icontains=query)|
				Q(title__icontains=query)
				).distinct()
		return qs

	def perform_create(self, serializers):
		serializers.save(user=self.request.user)

	def post(self,request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


	
	def get_serializer_context(self, *args, **kwargs):
		return {'request': self.request}


	# def put(self,request, *args, **kwargs):
	# 	return self.create(request, *args, **kwargs)

	# def patch(self,request, *args, **kwargs):
	# 	return self.create(request, *args, **kwargs)






class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
	pass
	lookup_field = 'pk'
	serializer_class = BlogPostSerializer
	# queryset= BlogPost.objects.all()

	def get_queryset(self):
		return BlogPost.objects.all()


	def get_serializer_context(self, *args, **kwargs):
		return {'request': self.request}








	# """docstring for ClassName"""
	# def __init__(self, arg):
	# 	super(ClassName, self).__init__()
	# 	self.arg = arg

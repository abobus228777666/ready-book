from reviews.models import Review
from django.shortcuts import render
from django.views import View
from reviews.forms import ReviewForm

class ReviewsView(View):
    def get(self, request):
        form = ReviewForm()
        reviews = Review.objects.all()
        return render(request,'pelmeni.html',{'form': form,'reviews': reviews})
    def post(self, request):
        form=ReviewForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            name=data.get('name')
            bobamail=data.get('email')
            review=data.get('review')
            stars=data.get('stars')
            Review.objects.create(name=name, email=bobamail, review=review, stars=stars)
            reviews = Review.objects.all()
            return render(request,'pelmeni.html',{'form':form, 'reviews':reviews})
def pelmeni(request):
    if request.method == 'GET':    
        form = ReviewForm()
        return render(request,'pelmeni.html',{'form':form})
    elif request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            name=data.get('name')
            bobamail=data.get('email')
            review=data.get('review')
            stars=data.get('stars')
            Review.objects.create(name=name, email=bobamail, review=review, stars=stars)
            reviews = Review.objects.all()
            return render(request,'pelmeni.html',{'form':form, 'reviews':reviews})
          #  return render(request,'pelmeni.html',{'aboba':name,'bobamail':bobamail,'boba_review':review,'stars':stars,"form":form})
    name=request.GET.get("aboba"),
    bobamail=request.GET.get("gmailboba"),
    review=request.GET.get("boba_review"),
    stars=request.GET.get("stars"),
    review_1=Review.objects.get(id=1)
    print(review_1.name)
    reviews = Review.objects.all()
    return render(request,'pelmeni.html',{'form':form, 'reviews':reviews})
from django.shortcuts import render
from reviews.forms import ReviewForm

def pelmeni(request):
    if request.method == 'GET':    
        form = ReviewForm()
        return render(request,'pelmeni.html',{'form':form})
    elif request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
    name=request.GET.get("aboba"),
    bobamail=request.GET.get("gmailboba"),
    review=request.GET.get("boba_review"),
    return render(request,'pelmeni.html',{'aboba':name,'bobamail':bobamail,'boba_review':review,"form":form})
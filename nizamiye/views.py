import sys
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .forms import UserDataForm, CikisForm
from .models import UserData

@login_required
def create_data(request):
    if request.method == "POST":
        form = UserDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user  # attach logged-in user automatically
            data.save()
            return redirect("list_data")  # replace with your page
    else:
        form = UserDataForm()
    return render(request, "nizamiye/create_data.html", {"form": form})

@login_required
def edit_data(request, pk):
    data = get_object_or_404(UserData, pk=pk, user=request.user)  
    # ensures only the owner can access

    if request.method == "POST":
        form = UserDataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()  # user is already set, no need to reattach
            return redirect("list_data")  # change to your list/detail view
    else:
        form = UserDataForm(instance=data)

    return render(request, "nizamiye/edit_data.html", {"form": form})

@login_required
def list_data(request):
    user_entries = UserData.objects.filter(user=request.user).order_by("-giris")
    return render(request, "nizamiye/list_data.html", {"entries": user_entries})


@login_required
def delete_data(request, pk):
    data = get_object_or_404(UserData, pk=pk, user=request.user)
    if request.method == "POST":
        data.delete()
        messages.success(request, "Entry deleted successfully.")
        return redirect("list_data")
    return render(request, "nizamiye/delete_data.html", {"entry": data})


def cikis(request):
    if request.method == "POST":
        form = CikisForm(request.POST)
        if form.is_valid():
            tcno = form.cleaned_data["tckn"]
            data = UserData.objects.filter(tckn=tcno).filter(cikis=None).order_by('-giris').first()

            if data:
                data.cikis=timezone.now()
                data.save()
                data.refresh_from_db()
                print(data.cikis, file=sys.stderr)
                return redirect("list_data")
            else:
                print("böyle birii yok", file=sys.stderr)
                messages.error(request, 'Yanlış TCKN')
    else:
        form = CikisForm()
    return render(request, "nizamiye/cikis.html", {"form": form})
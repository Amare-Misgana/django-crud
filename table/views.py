from django.shortcuts import render, redirect
from .models import MarkList


def create_table(request):
    if request.method == "POST":
        student = request.POST.get("student")
        mark = request.POST.get("mark")
        MarkList.objects.create(student_name=student, mark=mark)
        return redirect("table_url")

def pre_edit_table(request, id):
    student = MarkList.objects.get(id=id)
    return render(request, "table/edit_table.html", {"student": student})
def edit_table(request, id):
    student = MarkList.objects.get(id=id)
    if request.method == "POST":
        student_name = request.POST.get("student")
        mark = request.POST.get("mark")
        student.student_name = student_name
        student.mark = mark
        student.save()
        return redirect("table_url")

def delete_table(request, id):
    print("I am being deleted")
    if request.method == "POST":
        student = MarkList.objects.get(id=id)
        student.delete()
        return redirect("table_url")


def table(request):
    
    students = MarkList.objects.all()
    return render(request, "table/table.html", {"students": students})

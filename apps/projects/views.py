from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Project, Task
from .forms import ProjectForm, TaskForm

# Project Views
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully.')
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})

def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully.')
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/update_project.html', {'form': form})

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.delete()
    messages.success(request, 'Project deleted successfully.')
    return redirect('project_list')

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.tasks.all()
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks
    })

# Task Views
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'projects/task_list.html', {'tasks': tasks})

def add_task(request):
    project_id = request.GET.get('project_id')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully.')
            return redirect('task_list')
    else:
        form = TaskForm(initial={'project': project_id} if project_id else None)
    return render(request, 'projects/add_task.html', {'form': form})

def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'projects/update_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully.')
    return redirect('task_list')

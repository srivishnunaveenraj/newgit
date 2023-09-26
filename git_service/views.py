from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
import git

# views.py
from django.http import JsonResponse
import git


def get_git_history(request):
    try:
        repo = git.Repo("/path/to/your/git/repository")  # Replace with the actual path to your Git repository
        commit_history = []

        for commit in repo.iter_commits():
            commit_info = {
                'name': commit.author.name,
                'message': commit.message,
                'date': commit.authored_datetime.strftime("%Y-%m-%d"),
                'time': commit.authored_datetime.strftime("%H:%M:%S"),
                'sha': commit.hexsha
            }
            commit_history.append(commit_info)

        return JsonResponse({'history': commit_history})
    except Exception as e:
        return JsonResponse({'error': str(e)})


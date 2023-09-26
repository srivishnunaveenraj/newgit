from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
import git


def view_git_history(request):
    try:
        repo_url = "https://github.com/Sriman-narayanan-S/newgit.git"

        # Open a connection to the remote Git repository
        repo = git.Repo(repo_url)

        # Fetch the commit history
        commit_history = []
        for commit in repo.iter_commits():
            commit_info = {
                "hash": commit.hexsha,
                "author": commit.author.name,
                "date": commit.committed_datetime.isoformat(),
                "message": commit.message,
            }
            commit_history.append(commit_info)

        return JsonResponse({"commit_history": commit_history})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

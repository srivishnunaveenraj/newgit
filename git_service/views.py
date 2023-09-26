from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
import git


def view_git_history(request):
    try:
        # Replace 'repo_url' with the URL of the Git repository you want to view
        repo_url = "https://github.com/Sriman-narayanan-S/newgit.git"

        # Clone the Git repository to a local directory (optional)
        # This step fetches the repository if it's not already cloned locally
        local_repo_path = "E:\git\services\.git"  # Replace with your desired local path
        repo = git.Repo.clone_from(repo_url, local_repo_path, branch="main")

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

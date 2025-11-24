import os
import shutil
import subprocess


def remove_path(path: str) -> None:
    """Remove a file or directory if it exists."""

    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.exists(path):
        os.remove(path)


def main() -> None:
    ci_provider = "{{ cookiecutter.__ci }}"
    project_dir = os.path.realpath(os.curdir)

    github_path = os.path.join(project_dir, ".github")
    gitlab_path = os.path.join(project_dir, ".gitlab-ci.yml")

    if ci_provider != "github":
        remove_path(github_path)

    if ci_provider != "gitlab":
        remove_path(gitlab_path)

    try:
        subprocess.run(["git", "init", "--initial-branch", "main"], check=True)
    except Exception as exc:
        print(f"Skipping git init: {exc}")


if __name__ == "__main__":
    main()

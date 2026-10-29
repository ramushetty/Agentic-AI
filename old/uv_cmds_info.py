#  uv #

# 1.package manager (which helps to install packages)

# 2.project manager  (can have different projects with different python versions)
# (project1 can have 3.10 and project2 can have 3.13)

# $ uv venv --python 3.12.11
# $ source .venv/bin/activate
# $ uv pip install requests fastapi  (uv add fastapi)
# $ uv init my-first-project

# uv create list of files

# 1.pyproject.toml (replacement of requirement.txt)
# 2. .python-verion


# $ uv pip list 
# $ uv add -r requirement.txt
# $ uv sync (creates uv.lock if not present but syncs with dependencies in pyproject.toml)
# $ uv lock 

# no need to activate venv, uv is smart to detect





from github import Github
import sys

def print_commit_info(branch):
    first_commit = branch.commit
    print(f"Branch Name: {branch.name}")
    print(f"Commit ID (SHA): {first_commit.sha}")
    print(f"Commit Author Name: {first_commit.commit.author.name}")
    print(f"Commit Date: {first_commit.commit.author.date}")
    print(f"Commit Message: {first_commit.commit.message}")
    print("-" * 50)

def main():
    if len(sys.argv) != 4:
        print("not enough parameters,should be <repo-owner> <repo-name> <branch-name>")
        sys.exit(1)

    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]
    branch_name = sys.argv[3]

    g = Github()
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    branch = repo.get_branch(branch_name)
    print_commit_info(branch)

if __name__ == "__main__":
    main()
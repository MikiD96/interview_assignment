from github import Github
import sys

def print_commit_info(commit):
    print(f"Commit ID (SHA): {commit.sha}")
    print(f"Commit Author Name: {commit.commit.author.name}")
    print(f"Commit Date: {commit.commit.author.date}")
    print(f"Commit Message: {commit.commit.message}")
    print("-" * 50)

def main():
    if len(sys.argv) != 4:
        print("not enough parameters,should be <repo-owner> <repo-name> <branch-name>")
        sys.exit(1)
    #intialize required parameters
    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]
    branch_name = sys.argv[3]

    git = Github()
    repo = git.get_repo(f"{repo_owner}/{repo_name}")
    branch = repo.get_branch(branch_name)
    all_commits = repo.get_commits(sha=branch.commit.sha)
    
    #commits works as a queue, latest is at index 0 
    for commit in all_commits[:5]:
        print_commit_info(commit)

if __name__ == "__main__":
    main()
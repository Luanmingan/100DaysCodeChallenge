from collections import namedtuple

from github import Github, InputFileContent


Repo = namedtuple('Repo', 'name stars forks')
gh = Github()

pb = gh.get_user('superyang713')


def get_repo_stats(user, n=20):
    repos = []
    for repo in user.get_repos():
        if repo.fork:
            continue

        repos.append(Repo(
            name=repo.name,
            stars=repo.stargazers_count,
            forks=repo.forks_count
        ))

    return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]


for repo in get_repo_stats(pb):
    print(repo)
    import pdb; pdb.set_trace()

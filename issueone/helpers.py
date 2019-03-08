from github import Github


def language(lang_name):
    search(language, lang_name)
    return


def user(username):
    search(user, username)
    return


def repository(repo_name):
    search(repository, repo_name)
    return


def topic(topic_name):
    search(topic, topic_name)
    return


def search(search_type, search_param):
    github = Github(per_page=5)
    print(github.get_rate_limit())
    if(search_type == "repository"):
        repository = github.search_repositories(search_param)
        for repo in repository:
            print(repo.name)
    else:
        search_query = search_type + ':' + search_param
        repositories = github.search_repositories(query=search_query + ' good-first-issues:>0', sort="stars")
        for repo in repositories:
            print(repo.name)
    return

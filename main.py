import os
import subprocess
import requests
import json
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

current_dir = []

def join_dir(dir_list):
    return os.path.join(*dir_list) if dir_list else '.'

def show_dir_tree():
    joined_dir = join_dir(current_dir)
    try:
        items = os.listdir(joined_dir)
        print(f"Directory of {joined_dir}")
        for item in items:
            print(item)
    except FileNotFoundError:
        print("Directory not found")

def make_dir(name):
    joined_dir = join_dir(current_dir)
    try:
        new_dir = os.path.join(joined_dir, name)
        os.mkdir(new_dir)
        print(f"Directory {name} created")
    except FileExistsError:
        print("Directory already exists")
    except FileNotFoundError:
        print("Directory not found")

def change_dir(name):
    joined_dir = join_dir(current_dir + [name])
    if os.path.isdir(joined_dir):
        current_dir.append(name)
    else:
        print("Invalid directory")

def go_up():
    if current_dir:
        current_dir.pop()
    else:
        print("Already at the root directory")

def run_git_command(git_command):
    try:
        result = subprocess.run(git_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("\033[92m" + result.stdout + "\033[0m")  # Green for success
    except subprocess.CalledProcessError as e:
        print("\033[91m" + e.stderr + "\033[0m")  # Red for error

def show_github_stats():
    username = input("Enter the GitHub username: 🧑‍💻 ")

    # Fetch user details for linked accounts
    user_url = f"https://api.github.com/users/{username}"
    user_response = requests.get(user_url)
    user_data = json.loads(user_response.text)
    
    page = 1
    total_repos = 0
    total_stars = 0
    languages = []

    # ANSI escape codes for text colors
    green = "\033[92m"
    yellow = "\033[93m"
    red = "\033[91m"
    cyan = "\033[96m"  # Added for contact info
    reset = "\033[0m"

    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url)
        
        if response.status_code == 200 and response.json():
            repos = json.loads(response.text)
            print(f"🔍 Repositories of {username} (Page {page}) 🔍")

            for repo in repos:
                total_repos += 1
                total_stars += repo['stargazers_count']
                if repo['language']:
                    languages.append(repo['language'])

                repo_name = f"{green}📦 {repo['name']}{reset}"
                stars = f"{yellow}⭐ {repo['stargazers_count']}{reset}"
                language = f"{red}⚙️ {repo['language']}{reset}"

                print(f"{repo_name} | {stars} | {language}")

            page += 1
        else:
            break

    # Show total stats
    print(f"\n📊 Total Repos: {green}{total_repos}{reset}")
    print(f"🌟 Total Stars: {yellow}{total_stars}{reset}")

    # Show top 3 languages
    top_languages = Counter(languages).most_common(3)
    print("🔝 Top 3 Languages:")
    for lang, count in top_languages:
        print(f"{red}{lang}{reset} ({count} repos)")

    # Display linked accounts in a standout design
    print(f"\n{cyan}💼 Contact Information for {username} 💼{reset}")
    if user_data.get('email'):
        print(f"{cyan}📧 Email:{reset} {user_data['email']}")
    if user_data.get('blog'):
        print(f"{cyan}🌐 Website:{reset} {user_data['blog']}")
    if user_data.get('twitter_username'):
        print(f"{cyan}🐦 Twitter:{reset} https://twitter.com/{user_data['twitter_username']}")


def fetch_user_details(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def fetch_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def compare_users():
    username1 = input("Enter first GitHub username: ")
    username2 = input("Enter second GitHub username: ")

    details1 = fetch_user_details(username1)
    details2 = fetch_user_details(username2)

    repos1 = fetch_user_repos(username1)
    repos2 = fetch_user_repos(username2)

    if not details1 or not details2:
        print("Error fetching user details!")
        return

    if not repos1 or not repos2:
        print("Error fetching repos!")
        return

    total_stars1 = sum([repo['stargazers_count'] for repo in repos1])
    total_stars2 = sum([repo['stargazers_count'] for repo in repos2])

    attributes = ['public_repos', 'followers', 'following']
    values1 = [details1[attr] for attr in attributes] + [total_stars1]
    values2 = [details2[attr] for attr in attributes] + [total_stars2]

    attributes.append('total_stars')
    
# Extract languages
    languages1 = [repo['language'] for repo in repos1 if repo['language']]
    languages2 = [repo['language'] for repo in repos2 if repo['language']]
    top_languages1 = Counter(languages1).most_common(3)
    top_languages2 = Counter(languages2).most_common(3)

    # Bar chart for comparison
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 5))
    bar_width = 0.35
    index = np.arange(len(attributes))

    bar1 = ax1.bar(index, values1, bar_width, label=username1)
    bar2 = ax1.bar(index + bar_width, values2, bar_width, label=username2)

    ax1.set_xlabel('Attributes')
    ax1.set_ylabel('Counts')
    ax1.set_title(f'Comparison between {username1} and {username2}')
    ax1.set_xticks(index + bar_width / 2)
    ax1.set_xticklabels(attributes)
    ax1.legend()

    # Pie chart for top languages of username1
    labels1, sizes1 = zip(*top_languages1)
    ax2.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    ax2.set_title(f"Top Languages of {username1}")

    # Pie chart for top languages of username2
    labels2, sizes2 = zip(*top_languages2)
    ax3.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=90)
    ax3.axis('equal')
    ax3.set_title(f"Top Languages of {username2}")

    plt.tight_layout()
    plt.show()


def fetch_commit_activity(username, repo_name):
    
    url = f"https://api.github.com/repos/{username}/{repo_name}/stats/commit_activity"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching commit activity for {repo_name}.")
        return None
    return response.json()

def fetch_contributors_stats(username, repo_name):
    
    url = f"https://api.github.com/repos/{username}/{repo_name}/stats/contributors"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching contributor stats for {repo_name}.")
        return None
    return response.json()

def display_repository_analytics():
    username = input("Enter the GitHub username: ")
    repo_name = input("Enter the repository name: ")

    # Fetch commit activity
    commit_activity = fetch_commit_activity(username, repo_name)
    if commit_activity:
        print("\nCommit Activity over the past year (grouped by weeks):\n")
        for week_data in commit_activity:
            total_commits = week_data['total']
            week_start = week_data['week']
            week_start_str = datetime.fromtimestamp(week_start).strftime('%Y-%m-%d')
            print(f"Week starting on {week_start_str}: {total_commits} commits")

    # Fetch contributors stats
    contributor_stats = fetch_contributors_stats(username, repo_name)
    if contributor_stats:
        print("\nContributor Stats:\n")
        for contributor in contributor_stats:
            commits = contributor['total']
            user = contributor['author']['login']
            added_lines = sum([week['a'] for week in contributor['weeks']])
            removed_lines = sum([week['d'] for week in contributor['weeks']])
            print(f"{user}: {commits} commits, {added_lines} lines added, {removed_lines} lines removed")
def get_repo_branches(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/branches"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching branches for {repo_name}.")
        return None

    branches = [branch['name'] for branch in response.json()]
    return branches
           
def compare_branches():
    username = input("Enter the GitHub username: ")
    repo_name = input("Enter the repository name: ")
    
    # Get and display branches
    branches = get_repo_branches(username, repo_name)
    if not branches:
        return

    print("Available branches:")
    for index, branch_name in enumerate(branches, 1):
        print(f"{index}. {branch_name}")

    # Get user input for the branches to compare
    base_branch = input("Enter the base branch from the list above: ")
    compare_branch = input("Enter the branch to compare from the list above: ")
    
    # Fetching branch comparison
    url = f"https://api.github.com/repos/{username}/{repo_name}/compare/{base_branch}...{compare_branch}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error fetching branch comparison for {repo_name}.")
        return
    
    data = response.json()
    
    # Display basic comparison details
    print(f"Base branch: {base_branch}")
    print(f"Compare branch: {compare_branch}")
    print(f"Commits ahead: {data['ahead_by']}")
    print(f"Commits behind: {data['behind_by']}")
    
    # Display detailed commit differences
    print("\nCommit Differences:\n")
    for commit in data['commits']:
        sha = commit['sha'][:7]  # Taking first 7 characters of the commit SHA for brevity
        message = commit['commit']['message'].split('\n')[0]  # Taking the first line of commit message
        author = commit['commit']['author']['name']
        date = commit['commit']['author']['date']
        print(f"SHA: {sha}, Message: {message}, Author: {author}, Date: {date}")
def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching repositories for {username}.")
        return None
    return response.json()

def get_main_languages(repos):
    languages = [repo['language'] for repo in repos if repo['language']]
    return set(languages)

def search_repositories_by_language(language):
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching repositories for language {language}.")
        return None
    return response.json()['items'][:5]  # top 5 repositories by stars in the specified language

def recommend_repositories():
    username = input("Enter the GitHub username: ")

    # Fetch user repos
    repos = get_user_repos(username)
    if not repos:
        return

    # Extract main languages
    main_languages = get_main_languages(repos)

    recommendations = []
    for language in main_languages:
        recommendations.extend(search_repositories_by_language(language))

    # ANSI Colors
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    # Display Recommendations
    print(CYAN + "Recommended repositories based on your main languages:" + RESET)
    for repo in recommendations:
        print(GREEN + f"Name: {repo['name']}," + YELLOW + f" ⭐: {repo['stargazers_count']}," + BLUE + f" URL: {repo['html_url']}" + RESET)

def analyze_commit_messages():
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    
    username = input("Enter the GitHub username: ")
    repos = fetch_user_repos(username)
    if not repos:
        print(RED + f"Error fetching user repositories!" + "\033[0m")
        return

    commit_messages = []

    for repo in repos:
        repo_name = repo["name"]
        commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits?per_page=100"  # Maximum limit for per_page is 100
 
        response = requests.get(commits_url)

        if response.status_code == 200:
            commits_data = response.json()
            for commit in commits_data:
                commit_messages.append(commit["commit"]["message"])

    # Count the commit messages
    commit_message_counts = Counter(commit_messages)
    most_common_messages = commit_message_counts.most_common(10)  # Get top 10 common commit messages

    print("\nTop 10 most common commit messages:")
    for message, count in most_common_messages:
        print(GREEN + f"{message} - {count} times" + "\033[0m")

    return most_common_messages


def show_help():
    help_dict = {
        'dir': 'Show directory tree',
        'mkdir': '[Directory Name] : Create a new directory',
        'cd': '[Directory Name] : Change to subdirectory',
        'up': 'Go to parent directory',
        'git': '[Git Command] : Execute Git commands',
        'showgithub': 'Show GitHub stats for a specific user',      
        'compare': 'Compare GitHub stats between two users', 
        'diff': 'Compare two branches of a repository',
        'commitmsg': "Displays top most committd commit messages",
        'help': 'Show this help text',
        'exit': 'Exit the terminal'
       
    }

    print("Available Commands:")
    for command, description in help_dict.items():

        print(f"\033[92m{command}\033[0m : \033[0m{description}")


while True:

    command = input(">>> ").strip().split(' ', 1)
    action = command[0]

    if action == 'dir':
        show_dir_tree()
    elif action == 'mkdir':
        if len(command) > 1:
            make_dir(command[1])
        else:
            print("Specify the directory name")
    elif action == 'cd':
        if len(command) > 1:
            change_dir(command[1])
        else:
            print("Specify the directory name")
    elif action == 'up':
        go_up()
    elif action == 'git':
        if len(command) > 1:
            git_command = ['git'] + command[1].split()
            run_git_command(git_command)
        else:
            print("Specify the git command")
    elif action == 'exit':
        break
    elif action == 'help':
        show_help()
    elif action == 'showgithub':
        show_github_stats()
    elif action == 'compare':
        compare_users()
    elif action == 'repoanalytics':
        display_repository_analytics()
    elif action == 'diff':
        compare_branches()    
    elif action == 'searchgit':
        recommend_repositories()
    elif action == 'commitmsg':
        analyze_commit_messages()

    else:
        print("Invalid command")
   

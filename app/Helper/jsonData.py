from datetime import datetime

def jsonDataParser(data , webhook_event):

    author = data.get('sender', {}).get('login', 'Unknown')
    action = data.get('action', 'Unknown')

    time = str(datetime.now())

    if webhook_event == 'pull_request':
        pr_data = data.get('pull_request', {})
        from_branch = pr_data.get('base', {}).get('ref', 'Unknown')
        to_branch = pr_data.get('head', {}).get('ref', 'Unknown')
        timestamp = data.get('repository', {}).get('created_at', time)
    elif webhook_event == 'push':
            ref = data.get('ref', 'Unknown')
            from_branch = ref.split('/')[-1] if '/' in ref else 'Unknown'
            
            # Check if any commit message indicates a merge
            commits = data.get('commits', [])
            is_merge = any('Merge' in commit.get('message', '') for commit in commits)
            to_branch = 'Unknown'
            
            if is_merge:
                action = 'merge'
                to_branch = from_branch  # Placeholder, adjust as needed
            else:
                action = 'push'
            
            # timestamp = datetime.utcnow()
            timestamp = time
    else:
        # Default values for other events
        from_branch = 'Unknown'
        to_branch = 'Unknown'
        # timestamp = datetime.utcnow()
        timestamp = time
        print("*****"+timestamp)
    
    # Prepare data for MongoDB
    document = {
        'request_id': data.get('repository', {}).get('id', 'Unknown'),
        'author': author,
        'action': action,
        'from_branch': from_branch,
        'to_branch': to_branch,
        'timestamp': timestamp
    }

    return document
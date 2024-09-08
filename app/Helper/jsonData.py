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
            
            
            commits = data.get('commits', [])
            is_merge = any('Merge' in commit.get('message', '') for commit in commits)
            to_branch = 'Unknown'
            
            if is_merge:
                action = 'merge'
                to_branch = from_branch  
            else:
                action = 'push'
            
           
            timestamp = time
    else:
        
        from_branch = 'Unknown'
        to_branch = 'Unknown'
        
        timestamp = time
        print("*****"+timestamp)
    
   
    document = {
        'request_id': data.get('repository', {}).get('id', 'Unknown'),
        'author': author,
        'action': action,
        'from_branch': from_branch,
        'to_branch': to_branch,
        'timestamp': timestamp
    }

    return document
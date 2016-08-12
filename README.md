# TulipDeployerHelper

## Setup

### Slack Token:
The `testToken` variable in `messageController.py` should be set mannually

### Python dependency:

```sh
#install requests
$ pip install requests
```

## Usage

### Deploy origin/master
```sh
$ ./dp.sh 'server' 'git-repo' 'slack-channel'
```

### Deploy origin/branch
```sh
$ ./dp.sh 'server' 'git-repo' 'slack-channel' 'branch'
```

### Notification for Done
```sh
$ ./dp.sh 'server' 'git-repo' 'slack-channel' 'branch' done
```

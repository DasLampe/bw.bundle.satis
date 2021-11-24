# Create self-hosted Composer Repository (Satis)

## Config
```python
'metadata': {
    'satis': {
        'name': 'composer/internal-repo',
        'directory': '/var/www/satis',
        'url': 'https://composer.example.org',
        'repositories': [
            {'type': 'vcs', 'url': 'git@git.example.org:foo/bar.git'},
        ],
        'required': {
            'foo/bar': '~3.0',
        },
        'required_all': True,
        'skip_dev': False,
    },
}
   

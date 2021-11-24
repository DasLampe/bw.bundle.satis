import json

satis_config = node.metadata.get('satis', {})
composer = satis_config.get('composer_path', '/usr/bin/composer')
satis_dir = satis_config.get('directory', '/var/www/satis')

git_deploy = {
    satis_dir: {
        'repo': 'https://github.com/composer/satis.git',
        'rev': 'main',
        'tags': [
           'satis-preInstall',
        ]
    },
}

actions = {
    'composer_install': {
        'command': f"cd {satis_dir} && {composer} install",
        'needs': [
            'tag:satis-preInstall'
            'bundle:composer'
        ],
        'tags': [
            'satis-install',
        ]
    },
    'build_satis': {
        'command': f"cd {satis_dir} && php bin/satis build",
        'tags': [
            'satis-build',
        ],
        'needs': [
            f'file:{satis_dir}/satis.json',
        ]
    },
}


files = {
    f'{satis_dir}/satis.json': {
        'source': 'satis.json.mako',
        'content_type': 'mako',
        'context': {
            "name": satis_config.get('name', 'composer/internal-repo'),
            "url": satis_config.get('url', 'composer.example.org'),
            "repositories": json.dumps(satis_config.get('repositories', [])),
            "skip_dev": json.dumps(satis_config.get('skip_dev', False)),
            "required": json.dumps(satis_config.get('required', {})),
            'require_all': json.dumps(satis_config.get('require_all', True)),
        },
        'needs': [
            'tag:satis-install'
        ]
    }
}


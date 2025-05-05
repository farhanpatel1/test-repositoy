import os

pr_title = os.environ.get('PR_TITLE', '')
with open('VERSION', 'r') as f:
    version = f.read().strip()
major, minor, patch = map(int, version.split('.'))

if '[BUMP_MAJOR]' in pr_title:
    major += 1
    minor = 0
    patch = 0
elif '[BUMP_MINOR]' in pr_title:
    minor += 1
    patch = 0
else:
    patch += 1

new_version = f"{major}.{minor}.{patch}"
with open('VERSION', 'w') as f:
    f.write(new_version)

print(f"::set-output name=version::{new_version}")

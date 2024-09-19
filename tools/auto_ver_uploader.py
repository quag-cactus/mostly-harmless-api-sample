import sys

import subprocess
import semver

from version import __version__


def get_git_tag():
    result = subprocess.run(["git", "tag"], stdout=subprocess.PIPE)
    tags = result.stdout.decode("utf-8").split()
    return tags


def get_lastest_sember(tags):
    sember_tags = [tag for tag in tags if semver.VersionInfo.is_valid(tag)]

    if len(sember_tags) > 0:
        latest_version = max(sember_tags, key=lambda v: semver.VersionInfo.parse(v))
        return latest_version
    else:
        return "-"


tags = get_git_tag()
latest_version = get_lastest_sember(tags)
print(tags)
print(latest_version)

if __version__ == latest_version:
    sys.exit(0)
else:
    with open("version.py", "w") as fs:
        fs.write(f'__version__ = "{latest_version}"\n')
    sys.exit(1)

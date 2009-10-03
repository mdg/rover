#
# Copyright (c) 2009 Wireless Generation, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import unittest
import rover.config


class RepoInfoTest(unittest.TestCase):
    def test_github_repo_info(self):
        repo = rover.config.RepoInfo("github, git, git://github.com/")
        self.assertEqual("github", repo.name)
        self.assertEqual("git", repo.vcs)
        self.assertEqual("git://github.com/", repo.uri)

    def test_repo_info_comment_stripping(self):
        try:
            repo = rover.config.RepoInfo("  # comment line")
        except Exception, x:
            self.assertEqual('Cannot initialize RepoInfo for commented line' \
                    , str(x))
        else:
            self.fail("should have thrown an exception")

class ConfigInfoTest(unittest.TestCase):
    def test_git_config_line(self):
        conf = rover.config.ConfigInfo("rover.git, master, git")
        self.assertEqual("rover.git", conf.path)
        self.assertEqual("master", conf.branch)
        self.assertEqual("git", conf.repo)


BASIC_REPOS_TEST_CASE = """
  # comment line
github, git, git://github.com/
tigris, svn, svn://tigris.com/
sourceforge, cvs, :pserver:cvs.sourceforge.net:2401/cvsroot/
"""

class ParseRepoTest(unittest.TestCase):
    def test_basic_parse_repos(self):
        repos = rover.config.parse_repos(BASIC_REPOS_TEST_CASE.splitlines())

        self.assertEqual(3, len(repos))


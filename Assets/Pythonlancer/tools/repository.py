import os
import pygit2


class Repository(object):
    def __init__(self):
        pygit2.option(pygit2.GIT_OPT_SET_OWNER_VALIDATION, 0)

        self.repo = pygit2.Repository(os.path.abspath(os.path.dirname(__file__)))

    def sync(self):
        branch_name = self.repo.head.shorthand

        remote_name = 'origin'
        remote = self.repo.remotes[remote_name]

        remote.fetch()

        local_branch_ref = f'refs/heads/{branch_name}'
        local_branch = self.repo.lookup_reference(local_branch_ref)

        remote_reference = f'refs/remotes/{remote_name}/{branch_name}'
        remote_commit = self.repo.revparse_single(remote_reference)

        merge_result, _ = self.repo.merge_analysis(remote_commit.id)

        if merge_result & pygit2.GIT_MERGE_ANALYSIS_UP_TO_DATE:
            print("Already up-to-date")
        elif merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:
            local_branch.set_target(remote_commit.id)
            self.repo.head.set_target(remote_commit.id)
            self.repo.checkout_tree(self.repo.get(remote_commit.id))
            self.repo.reset(local_branch.target, pygit2.GIT_RESET_HARD)
            print("Fast-forward merge")
        elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:
            print("Update failed - Did you modify any file?")

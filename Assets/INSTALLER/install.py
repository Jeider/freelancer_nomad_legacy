import os
import pygit2
import pathlib
from tqdm import tqdm
import time


# 1. Use root folder
# 2. Crate Embed python with pygit2 and tqdm libraries
# 3. init git:
# git init 
# git remote add origin https://github.com/Jeider/freelancer_nomad_legacy.git
# 4. start script in root folder


class FetchProgressCallback(pygit2.RemoteCallbacks):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def transfer_progress(self, stats):
        self.pbar.total = stats.total_objects
        self.pbar.n = stats.indexed_objects
        self.pbar.refresh()


class CheckoutProgressCallback(pygit2.CheckoutCallbacks):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def checkout_progress(self, path, completed_steps, total_steps):
        self.pbar.total = total_steps
        self.pbar.n = completed_steps
        self.pbar.refresh()


def install():
    print('Init install script')

    cur_path = str(pathlib.Path().resolve()) + '\\'

    pygit2.option(pygit2.GIT_OPT_SET_OWNER_VALIDATION, 0)
    repo = pygit2.Repository(os.path.abspath(os.path.dirname(__file__)))
    remote_name = 'origin'
    remote = repo.remotes[remote_name]

    print('Fetch repository')
    remote.fetch(callbacks=FetchProgressCallback())

    branch_name = 'master'

    local_branch_ref = f'refs/heads/{branch_name}'

    try:
        repo.head
    except Exception:
        print('New branch')
        index = repo.index
        tree = index.write_tree()
        repo.create_reference_direct(local_branch_ref, tree, False)

    local_branch = repo.lookup_reference(local_branch_ref)

    remote_reference = f'refs/remotes/{remote_name}/{branch_name}'
    remote_commit = repo.revparse_single(remote_reference)

    print('Checkout branch master -- sync repository data with game')

    local_branch.set_target(remote_commit.id)
    repo.head.set_target(remote_commit.id)
    repo.checkout_tree(repo.get(remote_commit.id), strategy=pygit2.GIT_CHECKOUT_FORCE, callbacks=CheckoutProgressCallback())
    repo.reset(local_branch.target, pygit2.GIT_RESET_HARD)


current_path = pathlib.Path().resolve()
freelancer_exe = current_path / 'EXE' / 'Freelancer.exe'
dacom_dll = current_path / 'EXE' / 'dacom.dll'

if freelancer_exe.is_file() and dacom_dll.is_file():
    install()
    print('\n\nUpdate done! Exiting...')
    time.sleep(3)
else:
    print('\n\nFreelancer not found! Exiting...')
    time.sleep(3)

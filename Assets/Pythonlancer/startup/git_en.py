import os
import pygit2
import pathlib
from tqdm import tqdm
import time


# git init
# git remote add origin https://github.com/Jeider/freelancer_nomad_legacy.git


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

    branch_name = 'master_english'

    local_branch_ref = f'{remote_name}/{branch_name}'
    local_branch_ref2 = f'refs/heads/{branch_name}'

    print(f'Checkout branch {branch_name} -- load initial data')

    branch = repo.branches['origin/' + branch_name]
    branch_ref = repo.lookup_reference(branch.name)
    repo.checkout(branch_ref, strategy=pygit2.GIT_CHECKOUT_FORCE, callbacks=CheckoutProgressCallback())

    local_branch = branch_ref

    remote_reference = f'refs/remotes/{remote_name}/{branch_name}'
    remote_commit = repo.revparse_single(remote_reference)

    print(f'\n\nCheckout branch {branch_name} -- sync last repository data with game')

    local_branch.set_target(remote_commit.id)
    repo.head.set_target(remote_commit.id)
    repo.checkout_tree(repo.get(remote_commit.id), strategy=pygit2.GIT_CHECKOUT_FORCE,
                       callbacks=CheckoutProgressCallback())
    repo.reset(local_branch.target, pygit2.GIT_RESET_HARD)


current_path = pathlib.Path().resolve()
freelancer_exe = current_path / 'EXE' / 'Freelancer.exe'
dacom_dll = current_path / 'EXE' / 'dacom.dll'

if dacom_dll.is_file():
    install()
    print('\n\nUpdate done! Exiting...')
    time.sleep(3)
else:
    print('\n\nFreelancer not found! Exiting...')
    time.sleep(3)

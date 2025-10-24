import os
import sys
import pygit2
import pathlib
from tqdm import tqdm
import time
import subprocess
import ctypes

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

    git_path = pathlib.Path().resolve() / '.git'
    if not git_path.exists():
        print('This is not git repository. Cannot auto-update')
        return True

    cur_path = str(pathlib.Path().resolve()) + '\\'

    pygit2.option(pygit2.GIT_OPT_SET_OWNER_VALIDATION, 0)
    repo = pygit2.Repository(os.path.abspath(os.path.dirname(__file__)))
    remote_name = 'origin'
    remote = repo.remotes[remote_name]

    print('Fetch repository')
    remote.fetch(callbacks=FetchProgressCallback())

    branch_name = 'master'

    local_branch_ref = f'{remote_name}/{branch_name}'
    local_branch_ref2 = f'refs/heads/{branch_name}'
    
    print(f'Checkout branch {branch_name} -- load initial data')
    
    branch = repo.branches['origin/' + branch_name]
    branch_ref = repo.lookup_reference(branch.name)
        
    try:    
        if repo.head.target == branch_ref.target:
            print('No changes. Skip update')
            return True
    except pygit2.GitError:
        pass  # have no head, do nothing

    repo.checkout(branch_ref, strategy=pygit2.GIT_CHECKOUT_FORCE, callbacks=CheckoutProgressCallback())
    
    local_branch = branch_ref

    remote_reference = f'refs/remotes/{remote_name}/{branch_name}'
    remote_commit = repo.revparse_single(remote_reference)
    
    print(f'\n\nCheckout branch {branch_name} -- sync last repository data with game')

    local_branch.set_target(remote_commit.id)
    repo.head.set_target(remote_commit.id)
    repo.checkout_tree(repo.get(remote_commit.id), strategy=pygit2.GIT_CHECKOUT_FORCE, callbacks=CheckoutProgressCallback())
    repo.reset(local_branch.target, pygit2.GIT_RESET_HARD)


current_path = pathlib.Path().resolve()
freelancer_exe = current_path / 'EXE' / 'Freelancer.exe'
dacom_dll = current_path / 'EXE' / 'dacom.dll'

if dacom_dll.is_file():
    install()
    try:
        install()
    except Exception as e:
        print(f'Cannot install FL! Error: {e}')
        time.sleep(3)
        raise
    
    print('\n\nUpdate done! Run launcher...')
        
    launcher_file = 'run_ru.py'
    if len(sys.argv) > 1 and sys.argv[1] == 'en':
        launcher_file = 'run_en.py'
    
    file_root = os.getcwd()
    os.chdir(f'{file_root}\\Assets\\Pythonlancer\\')
    
    run_params = ['.\..\..\python\python.exe', f'.\{launcher_file}']
    
    debug = False
    if len(sys.argv) > 2 and sys.argv[2] == 'debug':
        debug = True

    if not debug:  
        kernel32 = ctypes.WinDLL('kernel32')

        user32 = ctypes.WinDLL('user32')

        SW_HIDE = 0

        hWnd = kernel32.GetConsoleWindow()
        user32.ShowWindow(hWnd, SW_HIDE)
            
    result = subprocess.run(run_params)

else:
    print('\n\nFreelancer not found! Exiting...')
    time.sleep(1)



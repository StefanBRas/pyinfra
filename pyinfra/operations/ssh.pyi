def keyscan(hostname, force=False, port=22, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def command(hostname, command, user=None, port=22, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def upload(
    hostname,
    filename,
    remote_filename=None,
    port=22,
    user=None,
    use_remote_sudo=False,
    ssh_keyscan=False,
    _sudo = None,
    _sudo_user = None,
    _use_sudo_login = None,
    _use_sudo_password = None,
    _preserve_sudo_env = None,
    _su_user = None,
    _use_su_login = None,
    _preserve_su_env = None,
    _su_shell = None,
    _doas = None,
    _doas_user = None,
    _shell_executable = None,
    _chdir = None,
    _env = None,
    _success_exit_codes = None,
    _timeout = None,
    _get_pty = None,
    _stdin = None,
    name = None,
    _ignore_errors = None,
    _precondition = None,
    _postcondition = None,
    _on_success = None,
    _on_error = None,
    _parallel = None,
    _run_once = None,
    _serial = None,
):...

def download(
    hostname,
    filename,
    local_filename=None,
    force=False,
    port=22,
    user=None,
    ssh_keyscan=False,
    _sudo = None,
    _sudo_user = None,
    _use_sudo_login = None,
    _use_sudo_password = None,
    _preserve_sudo_env = None,
    _su_user = None,
    _use_su_login = None,
    _preserve_su_env = None,
    _su_shell = None,
    _doas = None,
    _doas_user = None,
    _shell_executable = None,
    _chdir = None,
    _env = None,
    _success_exit_codes = None,
    _timeout = None,
    _get_pty = None,
    _stdin = None,
    name = None,
    _ignore_errors = None,
    _precondition = None,
    _postcondition = None,
    _on_success = None,
    _on_error = None,
    _parallel = None,
    _run_once = None,
    _serial = None,
):...
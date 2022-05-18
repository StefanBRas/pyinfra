def reboot(delay=10, interval=1, reboot_timeout=300, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def wait(port=None, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def shell(commands, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def script(src, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def script_template(src, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None, **data):...

def modprobe(module, present=True, force=False, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def mount(
    path,
    mounted=True,
    options=None,
    # TODO: do we want to manage fstab here?
    # update_fstab=False, device=None, fs_type=None,
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

def hostname(hostname, hostname_file=None, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def sysctl(
    key,
    value,
    persist=False,
    persist_file="/etc/sysctl.conf",
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

def service(
    service,
    running=True,
    restarted=False,
    reloaded=False,
    command=None,
    enabled=None,
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

def packages(
    packages,
    present=True,
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

def crontab(
    command,
    present=True,
    user=None,
    cron_name=None,
    minute="*",
    hour="*",
    month="*",
    day_of_week="*",
    day_of_month="*",
    special_time=None,
    interpolate_variables=False,
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

def group(group, present=True, system=False, gid=None, _sudo = None, _sudo_user = None, _use_sudo_login = None, _use_sudo_password = None, _preserve_sudo_env = None, _su_user = None, _use_su_login = None, _preserve_su_env = None, _su_shell = None, _doas = None, _doas_user = None, _shell_executable = None, _chdir = None, _env = None, _success_exit_codes = None, _timeout = None, _get_pty = None, _stdin = None, name = None, _ignore_errors = None, _precondition = None, _postcondition = None, _on_success = None, _on_error = None, _parallel = None, _run_once = None, _serial = None):...

def user(
    user,
    present=True,
    home=None,
    shell=None,
    group=None,
    groups=None,
    public_keys=None,
    delete_keys=False,
    ensure_home=True,
    system=False,
    uid=None,
    comment=None,
    add_deploy_dir=True,
    unique=True,
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
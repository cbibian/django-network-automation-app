import subprocess
from pathlib import Path
from .models import PlaybookJob

def run_playbook(job_id):
    job = PlaybookJob.objects.select_related("device").get(id=job_id)
    device = job.device

    group_name = device.group.name if device.group else "devices"

    inventory_content = f"""
[{group_name}]
{device.hostname} ansible_host={device.mgmt_ip} ansible_user={device.username} ansible_password={device.password}

[{group_name}:vars]
nsible_connection=network_cli
ansible_network_os=ios
ansible_network_cli_ssh_type=paramiko
ansible_ssh_extra_args=-oKexAlgorithms=+diffie-hellman-group14-sha1 -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa -oStrictHostKeyChecking=no
"""

    inventory_path = Path("inventory.ini")
    inventory_path.write_text(inventory_content)

    cmd = [
        "ansible-playbook",
        f"playbooks/{job.playbook_name}",
        "-i", str(inventory_path),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    job.output = result.stdout + "\n\n" + result.stderr
    job.status = "success" if result.returncode == 0 else "failed"
    job.save()
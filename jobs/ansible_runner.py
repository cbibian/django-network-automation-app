import subprocess
from pathlib import Path
from .models import PlaybookJob

def run_playbook(job_id):
    job = PlaybookJob.objects.select_related("device").get(id=job_id)
    device = job.device

    inventory_path = Path("inventory.ini")
    inventory_path.write_text(f"""
[{device.group.name if device.group else "devices"}]
{device.hostname} ansible_host={device.mgmt_ip} ansible_user={device.username} ansible_password={device.password}
""")

    cmd = [
        "ansible-playbook",
        f"playbooks/{job.playbook_name}",
        "-i", str(inventory_path),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    job.output = result.stdout + "\n\n" + result.stderr
    job.status = "success" if result.returncode == 0 else "failed"
    job.save()

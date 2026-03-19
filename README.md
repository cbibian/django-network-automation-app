```
• Django Network Automation Demo (Django + Ansible + Cisco IOSv)
  This project is a lightweight but production‑style network automation platform built with Django, Django REST Framework, and Ansible. It exposes a REST API for running playbooks against Cisco IOSv routers, dynamically generates inventories, executes automation jobs, and returns structured results.
  The goal is to demonstrate real NetDevOps patterns in a minimal, easy‑to‑run environment.

🚀 Features
✔ REST API for Network Automation
• 	Trigger Ansible playbooks via - POST /api/jobs/<id>/run/
• 	Retrieve job results via - GET /api/jobs/<id>/run/
• 	Stores job metadata, status, timestamps, and full Ansible output
✔ Dynamic Inventory Generation
• 	Inventory is generated per job from database‑stored device records
• 	Supports multiple device groups
• 	Injects required SSH parameters for legacy Cisco IOSv crypto
✔ Ansible Integration
• 	Uses network_cli with forced Paramiko transport
• 	Supports legacy KEX algorithms (diffie-hellman-group14-sha1, ssh-rsa)
• 	Successfully gathers IOS facts and executes network modules
✔ Device Connectivity
• 	Tested against Cisco IOSv running in CML
• 	Handles WSL2 routing, Windows interface forwarding, and SSH compatibility issues

🛠 Tech Stack
• 	Backend: Django, Django REST Framework
• 	Automation: Ansible (network_cli + Paramiko)
• 	Devices: Cisco IOSv (CML)
• 	Environment: Windows 11 + WSL2
• 	Database: SQLite (demo)

📡 Example Workflow
1. 	Add a device via Django admin or API
2. 	Create a job referencing a playbook (e.g., ios_facts.yml)
3. 	Run the job:
    POST /api/jobs/1/run/
4. 	Retrieve results:
    GET /api/jobs/1/
5. 	View full Ansible output and parsed facts

🔧 Key Engineering Challenges Solved
• 	WSL2 → CML reachability via routing and Windows interface forwarding
• 	Legacy Cisco SSH compatibility using Paramiko + SHA‑1 KEX algorithms
• 	Prevented Ansible from rewriting SSH variables by generating stable inventory files
• 	Built a reliable end‑to‑end automation pipeline with structured job storage

📁 Project Structure
  /api
  ├── models.py
  ├── views.py
  ├── serializers.py

/devices
  ├── models.py
  ├── serializers.py
  ├── views.py

/jobs
  ├── models.py
  ├── serializers.py
  ├── views.py

/cml_integration
  ├── models.py        # CMLSettings model
  ├── serializers.py   # CMLSettings serializer
  ├── views.py         # CRUD API for CML settings

/playbooks
  ├── ios_facts.yml
ansible_runner.py       # Executes playbooks via subprocess
inventory.ini           # Auto-generated per job

Example Output:

PLAY [Gather IOS facts] ********************************************************

TASK [Collect facts] ***********************************************************
ok: [R1]

TASK [debug] *******************************************************************

```json

ok: [R1] => {
    "facts": {
        "ansible_facts": {
            "ansible_net_api": "cliconf",
            "ansible_net_gather_network_resources": [],
            "ansible_net_gather_subset": [
               "default"
            ],
            "ansible_net_hostname": "R2",
            "ansible_net_image": "flash0:/vios-adventerprisek9-m",
            "ansible_net_iostype": "IOS",
            "ansible_net_model": "IOSv",
            "ansible_net_operatingmode": "autonomous",
            "ansible_net_python_version": "3.12.3",
            "ansible_net_serialnum": "9EUBP1OZNMIDE54MZ3A8N",
            "ansible_net_system": "ios",
            "ansible_net_version": "15.9(3)M9",
            "ansible_network_resources": {}
        },
        "changed": false,
        "deprecations": [
            {
                "collection_name": "ansible.builtin",
                "deprecator": {
                    "resolved_name": "ansible.builtin",
                    "type": null
                },
                "msg": "The paramiko connection plugin is deprecated.",
                "version": "2.21"
            },
            {
                "collection_name": "ansible.builtin",
                "deprecator": {
                    "resolved_name": "ansible.builtin",
                    "type": null
                },
                "msg": "Passing `warnings` to `exit_json` or `fail_json` is deprecated.",
                "version": "2.23"
            }
        ],
        "failed": false
    }
}



PLAY RECAP *********************************************************************
R1: ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


📌 Future Enhancements
• 	Web UI for job execution and history
• 	RBAC and user profiles
• 	Scheduled jobs

📜 License
MIT
```
